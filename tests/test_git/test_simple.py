import unittest

import os
import shutil
import subprocess as sp
import tempfile

from pyggc.git.simple import clone, get_num_commits


class Test__clone(unittest.TestCase):

    def setUp(self):
        self.url = 'https://github.com/scapeville/py-git-ghcli.git'

    def test_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            self.assertEqual(os.path.isdir(temp_dir), True)  # Debugging purposes
            clone_dir = os.path.join(temp_dir, 'py-git-ghcli')
            self.assertEqual(os.path.isdir(clone_dir), False)
            clone(self.url, temp_dir)
            self.assertEqual(os.path.isdir(clone_dir), True)
        self.assertEqual(os.path.isdir(temp_dir), False)  # Debugging purposes

    def test_already_exists(self):
        with tempfile.TemporaryDirectory() as cwd:
            
            clone_dir = os.path.join(cwd, 'py-git-ghcli')
            dummy_file = os.path.join(clone_dir, 'foo')
            
            ## Make an empty file
            os.mkdir(clone_dir)
            open(dummy_file, 'w').close()
            self.assertEqual(os.path.isfile(dummy_file), True)

            ## Test
            with self.assertRaises(sp.CalledProcessError):
                clone(self.url, cwd)


class Test__get_num_commits(unittest.TestCase):

    def setUp(self):
        self.cwd = tempfile.mkdtemp()

    def tearDown(self):
        self.assertEqual(os.path.isdir(self.cwd), True)  # Debugging purposes

        ## For Windows (ref: https://stackoverflow.com/questions/2656322/shutil-rmtree-fails-on-windows-with-access-is-denied)
        def onerror(func, path, exc_info):
            """
            Error handler for ``shutil.rmtree``.

            If the error is due to an access error (read only file)
            it attempts to add write permission and then retries.

            If the error is for another reason it re-raises the error.
            
            Usage : ``shutil.rmtree(path, onerror=onerror)``
            """
            import stat
            # Is the error an access error?
            if not os.access(path, os.W_OK):
                os.chmod(path, stat.S_IWUSR)
                func(path)
            else:
                raise

        shutil.rmtree(self.cwd, onerror=onerror)

    def test_success(self):

        ## Git init
        sp.run(['git', 'init'], cwd=self.cwd, check=True)
        sp.run(['git', 'config', 'user.name', 'foo'], cwd=self.cwd, check=True)
        sp.run(['git', 'config', 'user.email', 'bar'], cwd=self.cwd, check=True)

        self.assertEqual(get_num_commits(self.cwd), 0)

        ## Make a dummy commit
        open(os.path.join(self.cwd, 'foo.txt'), 'w').close()
        sp.run(['git', 'add', '.'], cwd=self.cwd, check=True)
        sp.run(['git', 'commit', '-m', 'init'], cwd=self.cwd, check=True)

        self.assertEqual(get_num_commits(self.cwd), 1)

        ## Make a dummy commit
        open(os.path.join(self.cwd, 'bar.txt'), 'w').close()
        sp.run(['git', 'add', '.'], cwd=self.cwd, check=True)
        sp.run(['git', 'commit', '-m', 'baz'], cwd=self.cwd, check=True)

        self.assertEqual(get_num_commits(self.cwd), 2)

    def test_dir_not_found(self):

        nonexistent_cwd = os.path.join(self.cwd, 'foobarbaz')

        ## Test
        with self.assertRaises((NotADirectoryError, FileNotFoundError)):
            get_num_commits(nonexistent_cwd)

    def test_not_a_git_repo(self):

        ## Create an empty file
        file_path = os.path.join(self.cwd, 'foo.txt')
        open(file_path, 'w').close()
        self.assertEqual(os.path.isfile(file_path), True)

        ## Test
        with self.assertRaises(ValueError) as ctx: get_num_commits(self.cwd)
        self.assertEqual(str(ctx.exception), f'Dir {repr(self.cwd)} is not a git repo.')


if __name__ == '__main__':
    unittest.main()