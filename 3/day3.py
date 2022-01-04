def get_part1(inp:list):
    most, least = "", "";
    for i in range(len(inp[0])):
        z = 0
        o = 0
        for j in range(len(inp)):
            if inp[j][i] == "0":
                z += 1
                continue
            o += 1
        if z > o:
            most += "0"
            least += "1"
        else:
            most += "1"
            least += "0"
        
    return int(most.lstrip("0"), 2) * int(least.lstrip("0"), 2)

def get_part2(inp:list):
    pass


if __name__ == "__main__":
    inp = []
    with open(r"test") as inp_file:
        for l in inp_file:
            inp.append(l.replace("\n", ""))
    part1 = get_part1(inp)
    print(part1) 
    part2 = get_part2(inp)
    print(part2) 