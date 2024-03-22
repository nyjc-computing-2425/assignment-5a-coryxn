def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """

# inp = input()
# seconds = int(inp[7:-1])
# verify if it is positive integer
    if not type(seconds) == type(3) and int(seconds)>0: 
      print('Unsupported input type.')
    else:
      hours = seconds//3600
      mins = (seconds%3600)//60
      secs = seconds%60
      return [hours, mins, secs]
   