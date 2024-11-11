# Import datetime
# import datetime # this improves the whole datetime library
from datetime import datetime

# Functions are defined as follows:

def print_time(print_str):
    print(print_str)
    print(datetime.now(), '\n')

print_time('Before the loop')

for i in range(1, 100):
    print(i)

print_time('After the loop')

