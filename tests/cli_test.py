import unittest
from autoconfsh.cli import cli_entrypoint

class CLITestCase(unittest.TestCase):
    def return_value(self):
        self.assertEqual(cli_entrypoint(), 0)


if __name__ == '__main__':
    unittest.main()
