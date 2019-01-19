#! /usr/local/bin/python
# -*- coding: utf-8 -*-


def a2bits(chars):
    """
    Converts a string to its bits representation as a string of 0's and 1's.

    >>> a2bits("Hello World!")
    '010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001'
    """
    return bin(reduce(lambda x, y : (x<<8)+y, (ord(c) for c in chars), 1))[3:]

def a2bits_list(chars):
    """
    Convert a string to its bits representation as a list of 0's and 1's.

    >>>  a2bits_list("Hello World!")
    ['01001000',
    '01100101',
    '01101100',
    '01101100',
    '01101111',
    '00100000',
    '01010111',
    '01101111',
    '01110010',
    '01101100',
    '01100100',
    '00100001']
    >>> "".join(a2bits_list("Hello World!"))
    '010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001'
    """
    return [bin(ord(x))[2:].rjust(8,"0") for x in chars]

def bs(s):
    """
    Converts an int to its bits representation as a string of 0's and 1's.
    """
    return str(s) if s<=1 else bs(s>>1) + str(s&1)

def setlsb(component, bit):
    """
    Set Least Significant Bit of a colour component.
    """
    return component & ~1 | int(bit)

def n_at_a_time(items, n, fillvalue):
    """
    Returns an iterator which groups n items at a time.
    Any final partial tuple will be padded with the fillvalue

    >>> list(n_at_a_time([1, 2, 3, 4, 5], 2, 'X'))
    [(1, 2), (3, 4), (5, 'X')]
    """
    it = iter(items)
    return its.izip_longest(*[it] * n, fillvalue=fillvalue)

def binary2base64(binary_file, output_file):
    """
    """
    # use mode = "rb" to read binary file
    fin = open(binary_file, "rb")
    binary_data = fin.read()
    fin.close()

    # encode binary to base64 string (printable)
    b64_data = base64.b64encode(binary_data)

    fout = open(output_file, "w")
    fout.write(b64_data)
    fout.close

def base642binary(b64_fname):
    """
    """
    # read base64 string
    fin = open(b64_fname, "r")
    b64_str = fin.read()
    fin.close()

    # decode base64 string to original binary sound object
    return base64.b64decode(b64_str)
  		    