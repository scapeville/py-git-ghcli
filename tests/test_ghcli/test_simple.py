import unittest

from pyggc.ghcli.simple import total_stargazers, get_stargazers


OWNER = 'scapeville'
REPO = 'py-git-ghcli'


class Test__total_stargazers(unittest.TestCase):

    def test(self):
        self.assertGreaterEqual(total_stargazers(OWNER), 0)


class Test__get_stargazers(unittest.TestCase):

    def test(self):
        self.assertGreaterEqual(get_stargazers(OWNER, REPO), 0)


if __name__ == '__main__':
    unittest.main()