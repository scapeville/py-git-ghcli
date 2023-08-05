import json as _json
import subprocess as _sp


def total_stargazers(owner:str, *, gh_cli_bin:str='gh') -> int:
    """Get the total stargazers count for all `owner` GitHub public repos"""

    cmd = [gh_cli_bin, 'repo', 'list', owner, '--visibility', 'public', '--json', 'stargazerCount']
    output = _sp.check_output(cmd, text=True)

    parsed = _json.loads(output)
    num_stargazers = sum([d['stargazerCount'] for d in parsed])

    return num_stargazers


def get_stargazers(owner:str, repo:str, *, gh_cli_bin:str='gh') -> int:
    """
    Get GitHub repo stargazers count.

    ---

    ## Params
    - `owner`: GitHub username
    - `repo` : GitHub repository name
    """

    cmd = [gh_cli_bin, 'repo', 'list', owner, '--visibility', 'public', '--json', 'name,stargazerCount']
    output = _sp.check_output(cmd, text=True)

    parsed = _json.loads(output)
    transformed = {d['name']: d['stargazerCount'] for d in parsed}
    num_stargazers = transformed[repo]

    return num_stargazers