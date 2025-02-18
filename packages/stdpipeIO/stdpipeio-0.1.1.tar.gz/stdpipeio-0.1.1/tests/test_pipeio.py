import unittest
from unittest.mock import patch
import io
import sys
from src.pipeio import pipe_io  # Import the decorator being tested

class TestPipeIO(unittest.TestCase):
    @patch('sys.stdin', new_callable=io.StringIO)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pipe_io(self, mock_stdout, mock_stdin):
        # Simulate standard input
        mock_stdin.write('Hello, World!')
        mock_stdin.seek(0)  # Reset cursor to the beginning of the file
        
        # Define a function using the pipe_io decorator
        @pipe_io
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
