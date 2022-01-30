from datetime import datetime


def format_time(rawtime: datetime):
    """
    Formats the time to a readable format.
    """
    return rawtime.strftime("%Y-%m-%d %H:%M:%S")
