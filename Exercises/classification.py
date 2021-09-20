import csv
from sklearn import tree

x=[]
y=[]
with open ('file.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[1:4])
        y.append(line[4])

clf = tree.DecisionTreeClassifier()
clf = clf.fit (x,y)
new_data = [[190, 89, 43],[160, 56, 39]]
answer = clf.predictO(new_data)
print(answer[0])
print(answer[1])