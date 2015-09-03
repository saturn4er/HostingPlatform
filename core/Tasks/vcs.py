import os
import core.sys_config as s_config
from shutil import rmtree
from core.tools.git import Repo


log_file = os.path.join(s_config.log_folder, 'git.txt')


def git_clone(repo, repo_dir='', overwrite=True, ignore_errors=False):
    print('Cloning {repo} to {repo_dir}'.format(repo=repo, repo_dir=repo_dir))
    repository = Repo(repo_dir, log_file)
    if repository.is_repo() and overwrite:
        rmtree(repo_dir, ignore_errors)
    repository.clone(repo)


def git_checkout(repo_dir, branch):
    repository = Repo(repo_dir, log_file)
    repository.checkout(branch)
