def main():
    quit = False

    while not quit:
        original = input('Enter a word (Q to quit): ')
        backwards = ''
        for i in reversed(original):
            backwards = backwards + i
        if original.upper() == 'Q':
            quit = True
        else:
            print(backwards)
main()
