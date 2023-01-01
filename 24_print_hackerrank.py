# Enter your code here. Read input from STDIN. Print output to STDOUT

def print_cone(ch:str="H", max_width:int=9, reverse:bool=False, offset:str=""):
    """
        prints a cone shape with given charactor, we can customize the printing of cone by passing some extra arguments.
        Arguments (everything is optional):
            ch - charactor to print, by default 'H'
            max_width - maximum size of the cone, final char size. by default 9
            reverse - boolean value which determine the upward cone or downward cone.
            offset - use it, if we want to offset the cone with some string.
    """
    if reverse:
        for_range = range(max_width, 0, -2)
    else:
        for_range = range(1, max_width+1, 2)
    for width in for_range:
        print(offset + (ch*width).center(max_width, ' '))


def print_rect(ch:str="H", width:int=5, height:int=6, reverse:bool=False, prefix:str="  ", midfix:str=" "*13, postfix:str=" ", repeat:int=1):
    for _ in range(height):
        print((prefix + ch*width + midfix) * repeat + postfix)


def draw_h(i:int=5):
    print_cone(max_width=(i*2)-1)
    print_rect(width=i, height=i+1, midfix=" "*((i*3)-2), repeat=2)
    print_rect(width=i*5, height=i-2)
    print_rect(width=i, height=i+1, midfix=" "*((i*3)-2), repeat=2)
    print_cone(max_width=i+4, reverse=True, offset=" "*i*4)


if __name__ == "__main__":
    i = int(input("Enter the input: "))
    draw_h(i)
