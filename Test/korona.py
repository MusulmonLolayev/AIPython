def main():
    path = r"D:\tanlanmalar\konavirus.txt"
    res = open(r"D:\korono.txt", "w")
    with open(path, "r") as file:
        types = []
        for line in file:
            j = 0
            while j < len(line) - 1:
                val = line[j] + line[j + 1]
                qq = 0
                if val in types:
                    i = 0
                    while types[i] != val:
                        i += 1
                    qq = i
                else:
                    types.append(val)
                    qq = len(types)
                res.write(str(qq) + " ")
                j += 2
            res.write("\n")
    res.close()

if __name__ == '__main__':
    main()