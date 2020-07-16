中文文件 = open(r'C:\Users\wuyudi\Desktop\新建文本文档 (3).txt',
            encoding='utf-8').readlines()
英文文件 = open(r'C:\Users\wuyudi\Desktop\34.txt',
            encoding='utf-8').readlines()
中文 = [j for i, j in enumerate(中文文件) if i % 4 == 2]

newfile = []

for i, j in enumerate(英文文件):
    newfile.append(j)
    if i % 4 == 2:
        newfile.append(中文[i//4])

with open(r'C:\Users\wuyudi\Desktop\34 - 副本.txt', 'w') as f:
    for j in newfile:
        f.write(j)
