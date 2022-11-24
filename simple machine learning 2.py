from sklearn.neighbors import NearestCentroid

#database: gerbang logika AND
#x = data, y = target
x = [{0,0}, [0,1], [0,2], [1,0], [2,0], [1,1], [1,2], [2,1], [2,2], [3,3]]
y = [0,1,2,3,4,5,6,7,8,9]

#training and classify
clf = NearestCentroid()
clf = clf.fit(x,y)

#prediksi
print ("logika AND metode K. Nearest Neighbors (KNN)")
print ("logika = prediksi")
print ("00 = ", clf.predict([[0,0]]))
print ("01 = ", clf.predict([[0,1]]))
print ("02 = ", clf.predict([[0,2]]))
print ("10 = ", clf.predict([[1,0]]))
print ("20 = ", clf.predict([[2,0]]))
print ("11 = ", clf.predict([[1,1]]))
print ("12 = ", clf.predict([[1,2]]))
print ("21 = ", clf.predict([[2,1]]))
print ("22 = ", clf.predict([[2,2]]))
print ("33 = ", clf.predict([[3,3]]))
