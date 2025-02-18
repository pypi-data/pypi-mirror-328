import io
import sys
import os
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from stdpipeIO.std_pipe_io import std_pipe_io


class TestPipeIO(unittest.TestCase):
    @patch('sys.stdin', new_callable=io.StringIO)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pipe_io(self, mock_stdout, mock_stdin):
        # Simulate standard input
        mock_stdin.write('Hello, World!')
        mock_stdin.seek(0)  # Reset cursor to the beginning of the file
        
        # Define a function using the pipe_io decorator
        @std_pipe_io
        def process_input(input_data):
            return input_data.upper()
        
        # Call the decorated function
        process_input()
        
        # Get the content from standard output
        output = mock_stdout.getvalue().strip()
        
        # Assert that the output matches the expected result
        self.assertEqual(output, 'HELLO, WORLD!')

if __name__ == '__main__':
    unittest.main()
