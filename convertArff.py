#! /usr/bin/env python3

out = open('data/data4.arff','w')

out.write("@RELATION games\n\n")
for i in range(1,119):
    out.write("@ATTRIBUTE c" + str(i) + " {-1,0,1}\n")
out.write("@ATTRIBUTE team {100,200}\n")

out.write("\n\n@DATA\n")

for i in range(1,11):
    with open('data/data' + str(i) + '.csv', 'r') as infile:
        for line in infile:
            out.write(line[4:-1] + ',' + line[:3] + '\n')

out.close()
