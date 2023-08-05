# Py-Git-GhCli

[![Run tests](https://github.com/scapeville/py-git-ghcli/actions/workflows/run-tests.yml/badge.svg)](https://github.com/scapeville/py-git-ghcli/actions/workflows/run-tests.yml)
[![PyPI Version](https://img.shields.io/pypi/v/pyggc.svg)](https://pypi.org/project/pyggc/)

Bunch of Python functions for Git and GitHub CLI tasks.


## Install

```shell
pip install pyggc
```


## Usage

```python
from pyggc.git.simple import clone

clone(
    url='https://github.com/scapeville/py-git-ghcli.git',
    cwd='/projects'
)
```

```python
from pyggc.git.simple import get_num_commits

num = get_num_commits('/projects/my-project')
print(num)
```

```python
from pyggc.ghcli.simple import get_stargazers

stars = get_stargazers(owner='scapeville', repo='py-git-ghcli')
print(stars)
```


## License

The scripts and documentation in this project are released under the MIT License.