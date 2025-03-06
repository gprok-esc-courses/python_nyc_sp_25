
def read_integer(msg: str) -> int:
    """
    Read an integer from the keyboard. 
    In case of error repeat
    """
    while True:
        try: 
            n = int(input(msg))
            return n
        except ValueError as ve:
            print("Please give an integer")