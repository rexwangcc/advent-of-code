import re
fname = "input.txt"

fopen = open(fname, "r")
data = [line for line in fopen.readlines()]

def processing(info):
    info = info.replace("\n", " ")
    field_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = [i.split(":")[0] for i in info.split(" ")]
    vaild = 1
    print(info, fields)
    for i in field_required:
        if i not in fields:
            vaild = 0
    return vaild

def strict_processing(info):
    info = info.replace("\n", " ")
    field_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    reg_required = {'byr':'^\d{4}$', 'iyr':'^\d{4}$', 'eyr':'^\d{4}$', 'hgt':'^\d{3}cm|\d{2}in$', 'hcl':'^#[0-9a-f]{6}$',
                        'ecl':'^amb|blu|brn|gry|grn|hzl|oth$', 'pid':'^\d{9}$'}
    fields = {}
    vaild = 1
    for i in info.split(" "):
        #update information
        if i != '':
            fields.update({i.split(":")[0]:i.split(":")[1]})
    #detect missing values
    for i in field_required:
        if i not in fields.keys():
            return 0
    #check type matching
    for i in field_required:
        re_exp = reg_required[i]
        if not re.search(re_exp, fields[i]):
            print(re_exp, fields[i])
            return 0
    #check data range
    byr = int(fields['byr'])
    iyr = int(fields['iyr'])
    eyr = int(fields['eyr'])
    hgt = [fields['hgt'][-2:], int(fields['hgt'][:-2])]
    if byr < 1920 or byr >2002:
        vaild = 0
        err = 'byr'
    if iyr < 2010 or iyr>2020:
        vaild = 0
        err = 'iyr'
    if eyr < 2020 or eyr>2030:
        vaild = 0
        err = 'eyr'
    if (hgt[0] == 'cm' and (hgt[1] < 150 or hgt[1] > 193)) or (hgt[0] == 'in' and (hgt[1] < 59 or hgt[1] > 76)):
        vaild =0
        err = 'hgt'
    if vaild == 0:
        print(err, fields[err])
    return vaild

info = "" #store information
valid_count = 0
for i in data:
    if i == '\n':
        valid_count += strict_processing(info)
        info = ""
    else:
        info = info + i
valid_count += strict_processing(info)
print(f"valid reports = {valid_count}")
