class A:
    def __init__(self):
        print("class A")


class B(A):
    pass


if __name__ == "__main__":
    b = B()
