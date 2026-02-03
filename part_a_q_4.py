
def safe_writing(fille_name):
    try:
        with open(fille_name,"w") as f:
            f.write("hello")
        return True
    except Exception:
        return False
    
print(safe_writing("part_a_q_1.txt"))
print(safe_writing("fake/non.txt"))