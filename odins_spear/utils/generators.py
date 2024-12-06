def generate_timestamp():
    """Generates a timestamp of the current time in string format.

    Returns:
        str: Timestamp of existing time when called.
    """
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
