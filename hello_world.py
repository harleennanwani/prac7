import os
import sys

# Check if a name is passed as a command-line argument or environment variable for CI environments
if len(sys.argv) > 1:
    name = sys.argv[1]  # Use the name from command-line argument
elif os.environ.get('JENKINS_URL'):
    name = 'Jenkins User'  # Default value for Jenkins environment
else:
    name = input("What is your name? ")  # Interactive mode for local use

print(f"Hello, {name}!")
