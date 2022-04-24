if __name__ == "__main__":
    a = dict()
    try:
        a["b"]
    except KeyError as e:
        breakpoint()
        print(e)
