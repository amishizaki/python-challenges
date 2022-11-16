# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# option 1 (worked)
for element in reversed('reverse_me'):
    print(element)

# option 2 (didn't work)
test = ['reverse_me']
test.reverse()
print(test)

# option 3 (worked)
def reverse(d):
    str = ''
    for i in d:
        str = i + str    
    return str

d = 'reverse_me'

print(reverse(d))