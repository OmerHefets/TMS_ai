def is_int(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False
