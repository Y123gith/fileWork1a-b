def print_stars_llength(file):
    with open(file,"r") as f:
        document = f.readlines()
        for line in document:
            if "\n" in line:
                line = line.replace("\n","").rstrip()
                print(f"{len(line)}**{line}**")

print_stars_llength("hello.txt")