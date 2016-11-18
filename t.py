import sys
import time

with open(sys.argv[1]) as ifile:
    ofile = open(sys.argv[2], 'w')
    ofile.write(ifile.readline())
    for line in ifile.readlines():
        line = line.strip().split(',')
        t = time.strptime(line[-2], '%Y-%m-%d %H:%M:%S')
        t = time.mktime(t)
        t = int(t)
        line[-2] = str(t)
        line = ','.join(line)
        ofile.write(line+'\n')

ofile.close()
