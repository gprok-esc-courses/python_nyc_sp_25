
from my_library import read_integer


def print_line_of_characters(ch: str, v: int, new_line: bool) -> None:
    """
    Prints character ch, v times. Prints a new line at the end if new_line is True
    """
    for i in range(v):
        print(ch, end=' ')
    if new_line:
        print()


print("RECTANGLE WITH ASTERISKS")
width = read_integer("Width: ")
height = read_integer("Height: ")

print_line_of_characters("*", width, True)
for i in range(height-2):
    print("*", end=' ')
    print_line_of_characters(" ", width-2, False)
    print("*")
print_line_of_characters("*", width, True)