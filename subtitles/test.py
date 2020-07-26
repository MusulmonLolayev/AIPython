reader = open("Jumanji_The_Next_Level_2019_HC_1080p.txt", 'r')
writer = open("res.txt", 'w')

i = 1

s = reader.readline()

sep = ' --> '
change = -10000

def convert(part):
    part = part.split(':')
    second = int(part[0]) * 3600000 + int(part[1]) * 60000 + float(part[2].replace(',', '.')) * 1000
    return second

def convert_str(time):
    # 34255
    hour = time // 3600000
    time = time % 3600000
    minute = time // 60000
    time = time % 60000
    second = time / 1000

    return str(int(hour)) + ":" + str(int(minute)) + ":" + str(second).replace('.', ',')

while s:
    try:
        j = int(s)
        print(s, file=writer, end='')
        s = reader.readline()
        array = s.split(sep=sep)
        print(array)

        begin = convert(array[0])
        end = convert(array[1])

        begin = convert_str(begin + change)
        end = convert_str(end + change)
        print(begin, end)

        print(begin + sep + end, file=writer)
        s = reader.readline()
        i += 1
    except:
        print(s, file=writer, end='')
        s = reader.readline()

reader.close()
writer.close()