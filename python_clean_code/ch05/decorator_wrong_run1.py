from decorator_wrong_1 import process_with_delay


def print_hello():
    print("hello")


if __name__ == "__main__":
    process_with_delay(print_hello, 1)
    process_with_delay(print_hello, 1)
    process_with_delay(print_hello, 1)
