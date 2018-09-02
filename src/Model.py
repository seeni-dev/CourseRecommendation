import sklearn.cluster as cluster


model = None
def Init():
	global model
	model = cluster.KMeans(n_clusters=4)

def Train(data):
	model.fit(data)
	print(model.labels_)

def getClusterCenters():
	return model.cluster_centers_
