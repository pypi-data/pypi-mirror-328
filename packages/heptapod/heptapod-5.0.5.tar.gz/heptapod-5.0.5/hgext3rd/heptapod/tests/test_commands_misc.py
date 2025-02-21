# Copyright 2019-2020 Georges Racinet <georges.racinet@octobus.net>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
#
# SPDX-License-Identifier: GPL-2.0-or-later
from __future__ import absolute_import

import json
from mercurial import (
    error,
    scmutil,
)
import os
import pytest
import re

from heptapod.testhelpers import (
    RepoWrapper,
)
from heptapod.testhelpers.gitlab import (
    GitLabMirrorFixture,
    GitLabStateMaintainerFixture,
)
from heptapod.testhelpers.git import GitRepo
from .utils import common_config

from .. import (
    versions as hpd_versions,
    branch as hpd_branch,
    special_ref,
    keep_around,
)


@pytest.fixture
def wrapper(tmpdir):
    repo_path = tmpdir.join('repo')
    yield RepoWrapper.init(repo_path, config=common_config(tmpdir))


def test_hpd_unique_successor(wrapper, monkeypatch):
    ctx = wrapper.write_commit('foo', message="default0",
                               return_ctx=True)
    repo_path = wrapper.path
    repo_path.join('foo').write('amend 1')
    wrapper.command('amend', message=b'amend1')
    repo_path.join('foo').write('amend 2')
    wrapper.command('amend', message=b'amend2')

    records = []

    def write(*args, **opts):
        records.append((args, opts))

    wrapper.repo.ui.write = write
    wrapper.command('hpd-unique-successor', rev=ctx.hex())
    out = records[0][0][0]

    succ_ctx = scmutil.revsingle(wrapper.repo, out)
    assert succ_ctx.description() == b'amend2'


def test_hpd_unique_successor_divergence(tmpdir, monkeypatch):
    repo_path = tmpdir.join('repo')
    config = common_config(tmpdir)
    config.setdefault('experimental', {})['evolution.allowdivergence'] = 'yes'
    wrapper = RepoWrapper.init(repo_path, config=config)
    ctx = wrapper.write_commit('foo', message="default0",
                               return_ctx=True)
    repo_path.join('foo').write('amend 1')
    wrapper.command('amend', message=b'amend1')

    # let's create the divergence
    wrapper.update(ctx.hex(), hidden=True)
    repo_path.join('foo').write('amend 2')
    wrapper.command('amend', message=b'amend2')

    with pytest.raises(error.Abort) as exc_info:
        wrapper.command('hpd-unique-successor', rev=ctx.hex())
    assert 'divergent' in exc_info.value.args[0]


def test_hpd_ensure_gitlab_branches(wrapper):
    # test almost trivial because all the logic is in HeptapodGitHandler
    wrapper.command('hpd-ensure-gitlab-branches')
    assert hpd_branch.read_gitlab_branches(wrapper.repo) == {}


def test_hpd_ensure_gitlab_default_branch(wrapper):
    # initially we don't have any default_gitlab_branch file
    assert not hpd_branch.get_default_gitlab_branch(wrapper.repo)
    # run command to create the file
    wrapper.command('hpd-ensure-gitlab-default-branch')
    assert hpd_branch.get_default_gitlab_branch(wrapper.repo) == b'master'
    # if already exists, running again shouldn't make any difference
    wrapper.command('hpd-ensure-gitlab-default-branch')
    assert hpd_branch.get_default_gitlab_branch(wrapper.repo) == b'master'


def test_hpd_ensure_gitlab_tags(wrapper):
    # test almost trivial because all the logic is in HeptapodGitHandler
    wrapper.command('hpd-ensure-gitlab-tags')
    assert hpd_branch.read_gitlab_tags(wrapper.repo) == {}


def test_hpd_ensure_gitlab_special_refs(wrapper):
    # test almost trivial because all the logic is in HeptapodGitHandler
    wrapper.command('hpd-ensure-gitlab-special-refs')
    assert special_ref.special_refs(wrapper.repo) == {}


def test_hpd_ensure_gitlab_keep_arounds(wrapper):
    # test almost trivial because all the logic is in HeptapodGitHandler
    wrapper.command('hpd-ensure-gitlab-keep-arounds')
    assert list(keep_around.iter_keep_arounds(wrapper.repo)) == []


def test_hpd_ensure_all_gitlab_specific_state_files(wrapper):
    # test almost trivial because all the logic is in HeptapodGitHandler
    wrapper.command('hpd-ensure-all-gitlab-specific-state-files')
    assert special_ref.special_refs(wrapper.repo) == {}
    assert hpd_branch.read_gitlab_tags(wrapper.repo) == {}
    assert hpd_branch.read_gitlab_tags(wrapper.repo) == {}
    assert list(keep_around.iter_keep_arounds(wrapper.repo)) == []
    assert hpd_branch.get_default_gitlab_branch(wrapper.repo) == b'master'


def test_hpd_unique_successor_missing_rev(wrapper, monkeypatch):
    with pytest.raises(error.Abort) as exc_info:
        wrapper.command('hpd-unique-successor')
    assert b'specify a revision' in exc_info.value.args[0]


def test_hpd_versions_with_hg_git(tmpdir, monkeypatch):
    # using RepoWrapper is pure lazyness on our part: they  give us the easiest
    # access to fully set up `ui` objects, with activated extensions
    config = common_config(tmpdir)
    config['extensions']['hggit'] = ''
    ui = RepoWrapper.init(tmpdir, config=config).repo.ui
    records = []

    def write(*args, **opts):
        assert all(isinstance(a, bytes) for a in args)
        records.append((args, opts))

    monkeypatch.setattr(ui, 'write', write)
    hpd_versions(ui)
    out = json.loads(records[0][0][0].decode())
    assert set(out.keys()) == {'python', 'mercurial',
                               'topic', 'hggit', 'evolve'}
    # for hggit it looks like: x.y.z (dulwich a.b.c)
    # for Mercurial, it can be just x.y
    version_re = re.compile(r'\d+[.]\d+([.]\d+)?')
    assert all(v is None or version_re.match(v) is not None
               for v in out.values())
    out.pop('hggit', None)  # hggit won't be shipped in some future
    assert all(v is not None for v in out.values())


@pytest.fixture()
def git_mirror_fixture(tmpdir, monkeypatch):
    with GitLabMirrorFixture.init(tmpdir, monkeypatch,
                                  hg_config=common_config(tmpdir)) as fixture:
        yield fixture


def test_git_resync_existing_git_repo(git_mirror_fixture):
    fixture = git_mirror_fixture
    wrapper = fixture.hg_repo_wrapper

    base_ctx = wrapper.commit_file('foo', message='Commit 0')

    # Adding various repo content
    wrapper.command('tag', b'v1.2.3', rev=base_ctx.hex())
    wrapper.commit_file('foo', message='Commit 1')
    # special refs and keep-arounds are added later in this test
    wrapper.command('gitlab-mirror')
    git_repo = fixture.git_repo

    wrapper.set_config('heptapod', 'native', 'yes')

    def assert_initial_git_state():
        assert git_repo.branch_titles() == {b'branch/default': b'Commit 1'}
        assert git_repo.tags() == {b'v1.2.3'}
        # checking ref targets, we don't care about the hashes
        base_git_sha, base_git_title = git_repo.commit_hash_title('v1.2.3')
        assert base_git_title == b'Commit 0'
        return base_git_sha

    # first call does not break anything, and moves Git repo to the dedicated
    # location
    wrapper.command('hpd-git-resync')
    fixture.reload_git_repo()
    assert fixture.git_repo.path != git_repo.path
    git_repo = fixture.git_repo
    assert_initial_git_state()

    # now adding a new commit to check basic incrementality
    # (adding another branch just to spice it a bit)
    wrapper.commit_file('foo', message='Commit 2')
    wrapper.commit_file('bar', parent=base_ctx, branch='other',
                        message='Commit 3')
    wrapper.command('gitlab-mirror')

    # Mirroring to Git did not happen (validity of test hypothesis)
    assert git_repo.branch_titles() == {b'branch/default': b'Commit 1'}

    wrapper.command('hpd-git-resync')
    assert git_repo.branch_titles() == {b'branch/default': b'Commit 2',
                                        b'branch/other': b'Commit 3'}
    assert git_repo.tags() == {b'v1.2.3'}


@pytest.fixture()
def native_fixture(tmpdir, monkeypatch):
    with GitLabStateMaintainerFixture.init(
            tmpdir, monkeypatch,
            hg_config=common_config(tmpdir)) as fixture:
        fixture.hg_repo_wrapper.set_config('heptapod.native', True)
        yield fixture


def test_git_resync_creates_git_repo(native_fixture):
    fixture = native_fixture
    wrapper = fixture.hg_repo_wrapper

    base_ctx = wrapper.commit_file('foo', message='Commit 0')

    # Adding various repo content
    wrapper.command('tag', b'v1.2.3', rev=base_ctx.hex())
    wrapper.commit_file('foo', message='Commit 1')
    # TODO special ref
    # TODO keep around
    wrapper.command('gitlab-mirror')
    wrapper.command('hpd-export-native-to-git')
    git_repo = GitRepo(
        fixture.base_path / '+hgitaly/hg-git'
        / wrapper.path.basename.replace('.hg', '.git')
    )
    assert git_repo.branch_titles() == {b'branch/default': b'Commit 1'}
    assert git_repo.tags() == {b'v1.2.3'}
    # checking ref targets, we don't care about the hashes
    base_git_sha, base_git_title = git_repo.commit_hash_title('v1.2.3')
    assert base_git_title == b'Commit 0'
    return base_git_sha


def test_move_out_of_gitaly_reach(git_mirror_fixture):
    fixture = git_mirror_fixture
    wrapper = fixture.hg_repo_wrapper
    orig_path = fixture.git_repo.path

    with pytest.raises(error.Abort):
        wrapper.command('move-hg-git-repo-out-of-gitaly-reach')

    wrapper.set_config('heptapod', 'native', True)
    wrapper.command('move-hg-git-repo-out-of-gitaly-reach')

    fixture.reload_git_repo()
    git_repo = fixture.git_repo
    assert git_repo.path != orig_path
    assert not os.path.exists(orig_path)
    assert os.path.exists(git_repo.path)
    # would not work if it were not a Git repo
    assert git_repo.branches() == {}
