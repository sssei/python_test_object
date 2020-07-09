res = []
with open("input.txt", "r") as f:
    for s_line in f:
        res.append(s_line.strip("\n"))
m = int(res.pop(-1))
mydict = {}
flag = False

for s_line in res:
    tmp = s_line.split(":")
    i = int(tmp[0])
    s = tmp[1]
    if m % i == 0 :
        mydict[i] = s
        flag = True

if __name__ == "__main__":
    if flag:
        for k, v in sorted(mydict.items()):
            print(str(v), end='')
    else:
        print(m, end='')
    print()

