def convert_to_strsid(binsid):
    if len(binsid) < 24:
        return None

    dashes = int(binsid[2:4])
    list_sid = ["S", "1"]
    range_parts = range(16, dashes*8+16, 8)
    list_sid.append(str(int(binsid[4:16], 16)))
    for i in range_parts:
        list_sid.append(str(int(invert_endian(binsid[i:i+8]), 16)))
    
    return "-".join(list_sid)

def convert_to_binsid(strsid):
    if not strsid[0:8] == "S-1-5-21":
        return None
    
    list_strsid = strsid.split("-")[2:]
    list_sid = ["01", "{:02d}".format(len(list_strsid) - 1), "{:012X}".format(int(list_strsid[0]))]
    
    for n in list_strsid[1:]:
        list_sid.append(invert_endian("{:08X}".format(int(n))))

    return "".join(list_sid)

def invert_endian(number):
    s = ""
    for i in range(len(number) + 1 if len(number) % 2 == 1 else len(number), -1, -2):
        s += number[i:i+2]
    return s

def print_list(l):
    if type(l).__name__ in ['list', 'tuple']:
        for r in l:
            print(r)
    elif type(l).__name__ == 'dict':
        for k, v in l:
            print(f'{k} => {v}')
    else:
        print(l)