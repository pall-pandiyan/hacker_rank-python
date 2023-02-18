# inputs = input().split(' ')
inputs = '7 21'.split(' ')
first_digit = int(inputs[0])
second_digit = int(inputs[1])
mid_digit = first_digit // 2

line_char = '-'
line_width = second_digit
design_word = '.|.'
welcome_word = 'WELCOME'
# center_line = f'{welcome_word}:{line_char}^{line_width}'
center_line = welcome_word.center(line_width, line_char)

def draw_a_segment(reverse=False):
    result_string = ''
    for i in range(1, first_digit, 2):
        if not result_string:
            result_string = (design_word * i).center(line_width, line_char)
        else:
            if reverse:
                result_string = (design_word * i).center(line_width, line_char) + '\n' + result_string
            else:
                result_string = result_string + '\n' + (design_word * i).center(line_width, line_char)
    return result_string

print(draw_a_segment())
print(center_line)
print(draw_a_segment(reverse=True))
