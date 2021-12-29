def get_part1(inp:list):
    last = 0
    c = 0
    for i, number in enumerate(inp):
        if i == 0:
            last = number
            continue
        if last < number:
            c += 1
        last = number
    return c

def get_part2(inp:list):
    c = 0
    last = 0
    for i, number in enumerate(inp):
        curr = number + inp[i+1] + inp[i+2]
        if i == 0:
            last = curr
            continue
        if last < curr:
            c += 1
        if i == len(inp)-3:
            break
        last = curr
    return c


if __name__ == "__main__":
    inp = []
    with open(r"input") as inp_file:
        for l in inp_file:
            inp.append(int(l.replace("\n", "")))
    part1 = get_part1(inp)
    print(part1) 
    part2 = get_part2(inp)
    print(part2) 
