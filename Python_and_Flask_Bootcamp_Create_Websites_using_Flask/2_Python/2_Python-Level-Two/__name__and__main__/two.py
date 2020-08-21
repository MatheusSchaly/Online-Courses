import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly!')
else:
    print('TWO.PY has been imported!')
    print('TWO.PY NAME:', __name__)
