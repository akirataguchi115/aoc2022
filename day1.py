f = open("input", "r")
lines = f.readlines()
temp = 0
list = []
for line in lines:
    if not line.strip():
        list.append(temp)
        temp = 0
    else:
        temp += int(line.strip())
list.sort(reverse=True)
print(list[0] + list[1] + list[2])
f.close()