"""
This is a debug test in python
"""


def main():
    """ For do a debug """
    # import pdb; pdb.set_trace()
    dicty = {'name': 'Daniel', 'age': 12}
    n = dicty['name']

    return dicty, n


if __name__ == '__main__':
    di, n = main()

    print(di['name'])
    if 'age' in di:
        print(di['age'])

    print(n)
