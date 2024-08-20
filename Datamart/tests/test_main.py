import unittest
import subprocess

class TestMain(unittest.TestCase):

    def test_main(self):
        """
        Test running the main script.
        """
        result = subprocess.run(['python', 'main.py', '--log_name', 'test_job', '--write_logs'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()