from collections import defaultdict


def sort_string(string: str) -> str:
    sorted_str = "".join(sorted(string))
    return sorted_str


def test_smoke():
    assert sort_string("cbc") == "bcc"


def use_defaultdict():
    group = defaultdict(list)
    group["aa"].append("aa")
    group["bb"].append("aca")

    return group


def test_use_defaultdict():
    assert list(use_defaultdict().values()) == [["aa"], ["aca"]]


if __name__ == "__main__":
    print(use_defaultdict())
