def find_lines_with(file,string):
    desired_lines = []
    with open(file,"r") as f:
        document = f.readlines()
        for line in document:
            if string in line:
                if " " in line:
                    temp = line.split(" ")[0]
                    if temp == string:
                        desired_lines.append(line)
                else:
                    desired_lines.append(line)
        return desired_lines
    
print(find_lines_with("hello.txt","Hello"))