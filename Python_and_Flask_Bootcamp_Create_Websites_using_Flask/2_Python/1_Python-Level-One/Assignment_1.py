# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):
    return (n1+n2) == 10

print("check_ten: {} {}".format(check_ten(10,20), check_ten(10,0)))

# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    sum = n1 + n2
    if sum == 10:
        return True
    else:
        return sum

print("check_ten_sum: {} {}".format(check_ten_sum(5, 5), check_ten_sum(5, 2)))

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.

def first_upper(mystring):
    return mystring[0].upper()

print("first_upper {} {}".format(first_upper("Hello"), first_upper("1342Hs")))

# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)

def last_two(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]

print("last_two {} {} {}".format(last_two("Hello"), last_two("He"), last_two("H")))

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.

def seq_check(nums):
    for i in range(len(nums) - 2):
        seq = nums[i:i+3]
        if seq == [1,2,3]:
            return True
    return False

print("seq_check {} {} {} {} {}".format(seq_check([1,2,3,4]), seq_check([1,2,3]), seq_check([2,1,2,3,4]), seq_check([2,1,2,3]), seq_check([2,3,1,2])))

# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**

def compare_len(s1,s2):
    return abs(len(s1) - len(s2))

print("compare_len {} {} {}".format(compare_len("abcd", "ab"), compare_len("ab", "abcd"), compare_len("ab", "cd"), compare_len("", "")))

# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.

def sum_or_max(mylist):
    if len(mylist) % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)

print("sum_or_max {} {} {} {}".format(sum_or_max([1,6]), sum_or_max([3]), sum_or_max([5,2,8]), sum_or_max([])))
