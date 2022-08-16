import re

KNOWN_SIZES = ['B', 'KiB', 'MiB', 'GiB', 'TiB']

units_regex = re.compile(r'[\d]+[ ]*(B|KiB|MiB|GiB|TiB)')


def convert_to_bytes(input_string):
    """
    Take the input_string and try and convert it to a size in bytes.
    Returns -1 on failure to convert to bytes.

    :param input_string:
    :return: An integer approximation in bytes of the input string the value is trying to describe.
    """
    result = -1
    m = units_regex.match(input_string)
    if m:
        units = m.group(1)
        power = KNOWN_SIZES.index(units)
        result = int(float(input_string.replace(units, '')) * 1024**power)
    return result
