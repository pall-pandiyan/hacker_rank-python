def print_formatted(number):
    word_width = len(str(bin(number))[2:])
    result = ('1'.rjust(word_width) + ' ') * 4
    
    for i in range(2, number+1, 1):
        result = result + '\n' + str(i).rjust(word_width) + ' ' + str(oct(i))[2:].rjust(word_width)  + ' ' + str(hex(i))[2:].upper().rjust(word_width)  + ' ' + str(bin(i))[2:].rjust(word_width)
        
    print(result)

if __name__ == '__main__':
    # n = int(input())
    # print_formatted(n)
    print_formatted(17)
