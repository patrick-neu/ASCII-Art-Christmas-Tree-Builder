# programm that draws a christmas tree as ASCII-art

def draw_tree(lines, star):
    """draw a tree of a hight defined by number of lines"""

    # construct the star of the tree wit "*", if wanted.
    if star == True:
        print(((lines - 1) * " ") + "*")

    # determine the number of x-elements needed per line. per line the
    # x-elements increase in an 1 + (2 * i) pattern, where i = 0 in line 1.
    # i is incremented each line.
    x_elements_per_line = []
    for i in range(0, lines):
        x_elements = 1 + (2 * i)
        x_elements_per_line.append(x_elements)
    x_elements_per_line.reverse()

    # determine the number of whitespace elements (w-elements) needed to add
    # to the x-elements on the left and on the right. the w-elements on each
    # side of the x-elements relate to the hight of the tree defined by number
    # of lines. the number of w-elements needed on each side equals: lines - 1.
    w_elements_per_line = list(range(0, lines))

    # construct the tree by adding the left w-elements, the x-elements and
    # the right w-elements.
    while w_elements_per_line:
        w_number = w_elements_per_line.pop()
        x_number = x_elements_per_line.pop()
        print((w_number * " ") + (x_number *"X") + (w_number*" "))

    # construct the stem of the tree with an "I"
    print(((lines - 1) * " ") + "I")

    # insert a line of spacing
    print("\n")

# store the height value for the tree and transfer the input to integer
lines = int(input("\nEnter the height in lines for your tree: "))

# store the star value
star = input("\nDo you want a star on top? [yes/no]: ")
if star == "yes":
    star = True

# insert some spacing
print("\n")

# call the function with the user input
draw_tree(lines, star)
