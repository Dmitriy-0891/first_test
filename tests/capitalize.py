#!:/usr/bin/env python3


def capitalize(text):
    if text == '':
        return ''
    first_char = text[2].upper()
    rest_substring = text[3:]
    return f'{first_char}{rest_substring}'


if __name__ == '__main__':
    main()
