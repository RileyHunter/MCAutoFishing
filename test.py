import numpy

base = [109.09504132, 102.69214876, 127.65082645]

neg = [
    [120.08264463, 100.20041322, 119.35743802],
    [106.9607438, 90.41735537, 114.60330579],
    [108.09710744, 98.01033058, 122.0785124 ],
    [115.62396694, 101.52892562, 123.04338843]
]

pos = [
    [ 51.87396694, 85.08057851, 139.71487603],
    [ 60.61363636, 103.97520661, 162.98966942],
    [ 54.36157025, 92.1053719, 149.88016529],
    [ 45.24173554, 80.33057851, 143.57438017]
]

for line in neg:
    line = numpy.array(line)
    diffs = line - base
    squares = numpy.square(diffs)
    sumSquaredDiff = numpy.sum(squares)
    print(sumSquaredDiff)

for line in pos:
    line = numpy.array(line)
    diffs = line - base
    squares = numpy.square(diffs)
    sumSquaredDiff = numpy.sum(squares)
    print(sumSquaredDiff)