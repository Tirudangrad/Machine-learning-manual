from sklearn import tree

#database: gerbang logika
# x = data, y = target
x = [[0,0,0], [0,0,1], [1,0,0], [2,0,1], [1,0,2], [0,1,1], [1,1,0], [1,1,1], [2,0,0], [0,0,2]]
y = [1,2,3,4,5,6,7,8,9,0]

#training and classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#prediksi
print ("logika AND metode decision tree")
print ("logika = prediksi")
print ("boss turu = ", clf.predict([[0,0,0]]))
print ("boss diam = ", clf.predict([[0,0,1]]))
print ("boss menyerang = ", clf.predict([[1,0,0]]))
print ("boss terlalu kuat = ", clf.predict([[2,0,1]]))
print ("boss terlalu lemah = ", clf.predict([[1,0,2]]))
print ("boss memberi celah = ", clf.predict([[0,1,1]]))
print ("boss membuatmu sekarat = ", clf.predict([[1,1,0]]))
print ("boss menghabiskan tenagamu = ", clf.predict([[1,1,1]]))
print ("boss mati = ", clf.predict([[2,0,0]]))
print ("kamu mati = ", clf.predict([[0,0,2]]))
