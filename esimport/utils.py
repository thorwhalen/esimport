import sys


def retrieve_file(filename):
    """
    Opens a file and returns its contents as a string after
    encoding to UTF-8
    :param filename:
    :return:
    """
    with open(filename, 'rb') as f:
        original_contents = f.read()

    decoded_contents = original_contents.decode('utf-8-sig').encode('utf-8')
    return decoded_contents


def retrieve_file_lines(filename):
    """
    Opens a file and returns its contents as an List of lines
    after encoding to UTF-8
    :param filename:
    :return:
    """
    decoded_contents = retrieve_file(filename)

    return decoded_contents.splitlines()
