import sklearn

model = None
def Init():
	model = cluster.KMeans(n_clusters=4)

def Train(data):
	model.fit(data)
	print(k_means.labels_)  
