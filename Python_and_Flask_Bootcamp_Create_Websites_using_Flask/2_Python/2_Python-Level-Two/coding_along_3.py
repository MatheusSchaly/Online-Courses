def hello(name='Jose'):
    print('The hello() func has been run')

    def greet():
        return "    The greet() func has been run"

    def welcome():
        return "    The welcome() func has been run"

    if name == 'Jose':
        return greet
    else:
        return welcome


x = hello(name='Sammy')
print(x())

def hello():
    return 'Hi Jose'

def other(func):
    print('Some other code')
    # Assume that func passed in is a function!
    print(func())

other(hello)

def new_decorator(func):

    def wrap_func():
        print('Some code BEFORE executing func()')
        func()
        print('Some code AFTER executing func()')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!")

# Same as @new_decorator
# func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()
