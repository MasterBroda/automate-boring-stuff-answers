tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

l = max(len(j) for i in tableData for j in i)
# print l

tb = zip(*tableData)

for i in tb:
    for j in i:
        print j.rjust(l),
    print "\n"
