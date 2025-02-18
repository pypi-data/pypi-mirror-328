# pipe_io.py
import sys
import functools

def std_pipe_io(func):
    """
    Decorator: Reads data from standard input, passes it to the function,
    and writes the result to standard output.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Read data from standard input
        input_data = sys.stdin.read().strip()
        
        # Process the data using the decorated function
        result = func(input_data, *args, **kwargs)
        
        # Write the result to standard output
        if result is not None:
            sys.stdout.write(str(result) + "\n")
    
    return wrapper

