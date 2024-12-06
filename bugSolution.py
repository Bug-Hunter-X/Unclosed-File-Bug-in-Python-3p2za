def function_with_closed_file(filename):
    try:
        f = open(filename, 'w')
        f.write('some data')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close() # always close the file
        print("File closed")
    return