def first_fifty_digits(file_name):
    with open(file_name,"r") as f:
        return f.read(50)