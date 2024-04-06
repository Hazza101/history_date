symbol_dic = {}

with open('history_dates.txt', 'r', encoding='utf-8') as f:

    for line in f.readlines():
        char = line[0]
        if char == '\n':
            continue
        if char not in symbol_dic:
            symbol_dic[char] = 1

        else:
            symbol_dic[char] += 1

        if char == '+':
            print(line.strip())

'''
for key, value in symbol_dic.items():
    print(f"Char:{key} RofO:{value:>20}")
'''
