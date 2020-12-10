from config import fname

data = list()
file_node = open(filename, 'r')
lines = file_node.readlines()
for line in lines:
    data.append(int(line))
print(data)

data_temp = list()
for i in range(len(data)):
    data_temp.append(0)

def sort(data):
    data_len = len(data)
    if data_len == 1:
        return data
    if data_len == 2:
        return [min(data), max(data)]
    else:
        left_half = data[0:int(data_len/2)]
        right_half = data[int(data_len/2):]
        return merge(sort(left_half), sort(right_half))

def merge(d1, d2):
    data = list()
    max_len = len(d2)
    index = 0
    if max_len == 0:
        return d1
    for i in range(len(d1)):
        while (index < max_len) and (d1[i] >= d2[index]):
            data.append(d2[index])
            index += 1
        data.append(d1[i])
    if index < max_len:
        data = data + d2[index:]
    if (len(d1) + len(d2) -len(data)) != 0:
        print(d1, d2, data)
    return data

data_temp = sort(data)

# https://kknews.cc/code/qyobyab.html
j = len(data_temp) - 1
for i in range(len(data_temp)):
    if data_temp[i] > 2020:
        continue
    for j in range(len(data_temp)):
        if data_temp[i] + data_temp[j] > 2020:
            continue
        k = len(data_temp) - 1
        while k > 0 and (data_temp[i] + data_temp[j] + data_temp[k] > 2020):
            k -=1
        if (data_temp[i] + data_temp[j] + data_temp[k] == 2020):
            print(data_temp[i],data_temp[j],data_temp[k],data_temp[i]*data_temp[j]*data_temp[k])
            break
