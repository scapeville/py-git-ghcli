import json as _json
import subprocess as _sp
from typing import (
    Dict as _Dict
)


def total_stargazers(owner:str, *, gh_cli_bin:str='gh') -> int:
    """
    Get the total stargazers count for all `owner` GitHub public repos

    ---

    ## Params
    - `owner`: GitHub username

    ## Exceptions
    - `subprocess.CalledProcessError`: if `owner` is not found
    """

    cmd = [gh_cli_bin, 'repo', 'list', owner, '--visibility', 'public', '--json', 'stargazerCount']
    output = _sp.check_output(cmd, text=True)

    parsed = _json.loads(output)
    num_stargazers = sum([d['stargazerCount'] for d in parsed])

    return num_stargazers


def pack_stargazers(owner:str, *, gh_cli_bin:str='gh') -> _Dict[str, int]:
    """
    Return a dictionary of stargazer counts for every repository

    ---

    ## Params
    - `owner`: GitHub username

    ## Exceptions
    - `subprocess.CalledProcessError`: if `owner` is not found
    """

    cmd = [gh_cli_bin, 'repo', 'list', owner, '--visibility', 'public', '--json', 'name,stargazerCount']
    output = _sp.check_output(cmd, text=True)

    parsed = _json.loads(output)
    pack = {d['name']: d['stargazerCount'] for d in parsed}

    return pack


def get_stargazers(owner:str, repo:str, *, gh_cli_bin:str='gh') -> int:
    """
    Get GitHub repo stargazers count.

    ---

    ## Params
    - `owner`: GitHub username
    - `repo` : GitHub repository name

    ## Exceptions
    - `subprocess.CalledProcessError`: if `owner` is not found
    - `KeyError`: if `repo` is not found
    """
    pack = pack_stargazers(owner)
    num_stargazers = pack[repo]
    return num_stargazers