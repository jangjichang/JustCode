def validate_group_permission(sid: int) -> None:
    if sid == 1:
        return

    try:
        group = sid / sid
    except ZeroDivisionError:
        print(f"sid: {sid} does not have group")
        return

    if not sid % 2:
        raise ValueError("Test")


if __name__ == "__main__":
    validate_group_permission(2)
