import subprocess as _sp


def clone(url:str, cwd:str, *, git_bin:str='git') -> None:
    """
    Run `git clone <url>`

    ---

    ## Params
    - `url`: Clone URL
    - `cwd`: Current working directory

    ## Docs
    - If `cwd='/foo/bar'`, the clone will be at `/foo/bar/clone`.
    """
    cmd = [git_bin, 'clone', url]
    _sp.run(cmd, cwd=cwd, check=True)


def get_num_commits(repo_root_dir:str, *, git_bin:str='git') -> int:
    """
    Run `git rev-list --count HEAD`

    ---

    ## Params
    - `repo_root_dir`: Absolute path to the repository root directory (where `.git` folder lives)
    """
    cmd = [git_bin, 'rev-list', '--count', 'HEAD']
    res = _sp.check_output(cmd, cwd=repo_root_dir, text=True)
    return int(res.strip())