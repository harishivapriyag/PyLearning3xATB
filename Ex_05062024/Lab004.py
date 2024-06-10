print()


# self --oops concept, means itself
# __init__ -- constructor
# __del__ -- destructor
# __str__ -- used to print the object in a string format

class Computer:
    def __init__(self):
        self.name = 'Hari'
        self.age = 21

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


# *args -- unlimited number of arguments --int, str, float, boolean....
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# sep --- used to separate the arguments
print('Hari', 'Shivapriya', sep='*', end='\n')

# end -- '\n' - in the end of a statement what user wants to print

print('Hari', 'Shivapriya', sep=' ', end='\n')

# file --used to redirect the output to a file
# flush -- used to flush the output to a file

# print('Hari', 'Shivapriya', file=open('abc.txt', 'w'), flush=True)
