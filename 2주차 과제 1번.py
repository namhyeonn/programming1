def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        first_char = s[0]
        rest_of_string = s[1:]
        
        reversed_string = reverse_string(rest_of_string) + first_char
        return reversed_string

if __name__ == '__main__':
    print(reverse_string('ABCDE'))
    print(reverse_string('Come again, Forever young!'))
    print(reverse_string('Amore, Roma'))
