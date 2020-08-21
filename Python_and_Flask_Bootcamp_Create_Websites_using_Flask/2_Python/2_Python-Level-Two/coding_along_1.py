# x = 'outside'
#
# def report():
#     x = 'inside'
#     return x
#
# print(x)

# LEGB RULE - LOCAL ENCLOSING GLOBAL BUILT IN

# LOCAL
# def report():
#     # LOCAL ASSIGNMENT
#     x = 'local'
#     print(x)

# ENCLOSING
# x = 'THIS IS GLOBAL LEVEL'
#
# def enclosing():
#     # ENCLOSING ASSIGNMENT
#     x = 'Enclosing Level'
#
#     def inside():
#         print(x)
#
#     inside()
#
# enclosing()
#
# # GLOBAL
# # GLOBAL ASSIGNMENT
# x = 'THIS IS GLOBAL LEVEL'

# def enclosing():
#     # ENCLOSING ASSIGNMENT
#     # x = 'Enclosing Level'
#
#     def inside():
#         # LOCAL ASSIGNMENT
#         print(x)
#
#     inside()
#
# enclosing()

# BUILT IN
# len, max, sum...

x = 'outside'

def report():
    # global x # GRABBING THE GLOBAL LEVEL X
    x = 'inside'
    return x

print(report())
print(x)
