def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    f.write('some data')
    # forgot to close the file
    return  # missing f.close()