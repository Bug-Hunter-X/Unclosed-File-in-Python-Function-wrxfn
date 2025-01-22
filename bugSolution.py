def function_with_closed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
        for line in f:
            # process each line
            print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        if 'f' in locals() and f:
            f.close() # Close the file even if errors occur
        print("File closed successfully")
        # Alternatively, use 'with' statement for automatic closing
        # with open(filename, 'r') as f:
        #     for line in f:
        #         print(line.strip()) 