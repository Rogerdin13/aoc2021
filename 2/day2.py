def get_part1(inp:list):
    x = 0
    y = 0
    for comm in inp:
        if comm.startswith("f"):
            x += int(comm.split(" ")[1])
            continue
        if comm.startswith("u"):
            y -= int(comm.split(" ")[1])
            continue
        if comm.startswith("d"):
            y += int(comm.split(" ")[1])
            continue
    return x * y

def get_part2(inp:list):
    x = 0
    y = 0
    a = 0
    for comm in inp:
        if comm.startswith("f"):
            x += int(comm.split(" ")[1])
            y += a * int(comm.split(" ")[1])
            continue
        if comm.startswith("u"):
            a -= int(comm.split(" ")[1])
            continue
        if comm.startswith("d"):
            a += int(comm.split(" ")[1])
            continue
    return x * y


if __name__ == "__main__":
    inp = []
    with open(r"input") as inp_file:
        for l in inp_file:
            inp.append(l.replace("\n", ""))
    part1 = get_part1(inp)
    print(part1) 
    part2 = get_part2(inp)
    print(part2) 