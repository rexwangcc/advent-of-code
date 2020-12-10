from config import fname

fopen = open(fname, 'r')
lines = fopen.readlines()

decode = lambda x: [x[0].split("-"), x[1][:-1], x[2][:-1]]
data = [decode(line.split(" ")) for line in lines]

#monkey writing kmp
def kmp(string, s):
    def cal_next(s):
        s_len = len(s)
        next = list()
        k = -1
        for i in range(s_len):
            while k > -1 and s[i] != s[k]:
                k = next[k]
            next.append(k)
            if k == -1 or s[i] == s[k]:
                k += 1
        return next

    string_len = len(string)
    s_len = len(s)
    next = cal_next(s)
    j = 0
    for i in range(string_len):
        while j > 0 and string[i] != s[j]:
            j = next[j]
        if j==-1 or string[i] == s[j]:
            j += 1
        if j == s_len:
            return i - s_len + 1
    return -1

def count_kmp(string, s):
    ind = 0
    while True:
        pos = kmp(string, s)
        if pos == -1:
            break
        ind += 1
        string = string[pos + len(s):]
    return ind

ind = 0
for len_pair, s, string in data:
    len_min = int(len_pair[0])
    len_max = int(len_pair[1])
    count = count_kmp(string, s)
    if count >= len_min and count <= len_max:
        ind += 1

print(ind)

ind = 0
for len_pair, s, string in data:
    len_min = int(len_pair[0])
    len_max = int(len_pair[1])
    count = count_kmp(string, s)
    if (string[len_min - 1] == s) + (string[len_max - 1] == s) == 1:
        ind += 1
print(ind)
