# stdpipeIO

stdpipeIO is a simple Python decorator for receiving and sending data via the standard pipe. It allows you to easily read input from standard input (stdin) and write output to standard output (stdout).

## Installation

To install stdpipeIO, you can use the following command:

```sh
pip install stdpipeIO
```

## Usage
To use the pipe_io decorator, simply import it and apply it to your function. The decorated function will read input from stdin, process it, and write the result to stdout.

```sh
from stdpipeIO.std_pipe_io import std_pipe_io

@std_pipe_io
def process_input(input_data):
    return input_data.upper()

if __name__ == '__main__':
    process_input()
```

You can then run your script and provide input via stdin:

```sh
echo "Hello, World!" | python your_script.py
```

The output will be:

```sh
HELLO, WORLD!
```

## Testing
To run the tests for stdpipeIO, you can use the following command:

```sh
python -m unittest discover tests
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Greendog - x6reend0g@foxmail.com 