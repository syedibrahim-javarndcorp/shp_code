with open("D.txt", "r") as file:
    for line in file:
        lines = line.replace(r"[","")
        lins = lines.replace(r"]","")
        with open("D1.csv", "a") as f:
            f.writelines(lins)
            print(lins)
