def func():
    print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')
    print('ONE.PY NAME:', __name__)
