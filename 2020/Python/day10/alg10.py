fname = "input.txt"

fopen = open(fname, "r")
data = [int(line) for line in fopen.readlines()]
data.sort()
data.insert(0, 0) #adjust for the zero input
data.insert(len(data), data[-1]+3) #adjust for the 3 jolt higher output

data_delta = [data[i+1] - data[i] for i in range(len(data)-1)]
print(f"length of input is {data.__len__()}, \
3-jolt differences is {data_delta.count(3)}, \
1-jolt differences is {data_delta.count(1)}", )

#find 1s
data_arrg = "".join(["1" if i == 1 else " " for i in data_delta]).split(" ")
#number of joints
joint = [1, 1, 2, 4, 7]
print(data_arrg)
arrg = 1
for i in data_arrg:
    arrg *= joint[len(i)]
print(arrg)
#111, 102, 021, 003
#1111, 1003, 1102, 1021, 0211, 0202, 0031
