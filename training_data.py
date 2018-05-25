import csv

data = []
# title = []
cls = ['0', '1', '2']


def mtitle(num, name):
    for i in range(num):
        name.append(str(i).zfill(5))

with open("training.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        data.append(line)


tmp1 = []
tmp2 = []
tmp3 = []

title3 = []
title2 = []
title1 = []

for i in range(len(data)-1):
    if data[i][0].split(',')[15] == '2':
        tmp3.append(data[i])
    if data[i][0].split(',')[15] == '1':
        tmp2.append(data[i])
    if data[i][0].split(',')[15] == '0':
        tmp1.append(data[i])

mtitle(len(tmp3), title3)
mtitle(len(tmp2), title2)
mtitle(len(tmp1), title1)

files3 = [open('ddata/train/2/%s.txt' % s, 'w') for s in title3]
files2 = [open('ddata/train/1/%s.txt' % s, 'w') for s in title2]
files1 = [open('ddata/train/0/%s.txt' % s, 'w') for s in title1]

for i in range(len(title3)):
    files3[i].write(tmp3[i][0])
for i in range(len(title2)):
    files2[i].write(tmp2[i][0])
for i in range(len(title1)):
    files1[i].write(tmp1[i][0])
