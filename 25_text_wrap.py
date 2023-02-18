import textwrap

def wrap(string, max_width):
    start_index = 0
    end_index = max_width
    last_index = len(string)
    result_string = string[start_index:end_index]
    
    while start_index < last_index and end_index <= last_index:
        start_index = start_index + max_width
        end_index = end_index + max_width
        if end_index > last_index:
            end_index = last_index
            
        result_string = result_string + '\n' + string[start_index:end_index]

    return result_string


if __name__ == '__main__':
    # string, max_width = input("string:"), int(input("max_width:"))
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)
    
