import sys

if __name__ == '__main__':
    args = sys.argv
    if 3 <= len(args):
        print(args[0])
        print(args[1])
        print(args[2])

    else:
        print('Arguments are too short')
