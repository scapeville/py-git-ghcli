import unittest

import subprocess as sp

from pyggc.ghcli.simple import total_stargazers, pack_stargazers, get_stargazers


OWNER = 'scapeville'
REPO = 'py-git-ghcli'

NONEXISTENT_OWNER = 'e49786230ba' + OWNER + '9863c4d86b8'
NONEXISTENT_REPO = REPO + 'c925705c2ee'


class Test__total_stargazers(unittest.TestCase):

    def test_success(self):
        self.assertGreaterEqual(total_stargazers(OWNER), 0)

    def test_owner_not_found(self):
        with self.assertRaises(sp.CalledProcessError):
            total_stargazers(NONEXISTENT_OWNER)


class Test__pack_stargazers(unittest.TestCase):

    def test_success(self):
        pack = pack_stargazers(OWNER)
        for k, v in pack.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, int)
            self.assertGreaterEqual(v, 0)

    def test_owner_not_found(self):
        with self.assertRaises(sp.CalledProcessError):
            pack_stargazers(NONEXISTENT_OWNER)


class Test__get_stargazers(unittest.TestCase):

    def test_success(self):
        self.assertGreaterEqual(get_stargazers(OWNER, REPO), 0)
    
    def test_owner_not_found(self):
        with self.assertRaises(sp.CalledProcessError):
            get_stargazers(NONEXISTENT_OWNER, REPO)

    def test_repo_not_found(self):
        with self.assertRaises(KeyError):
            get_stargazers(OWNER, NONEXISTENT_REPO)


if __name__ == '__main__':
    unittest.main()