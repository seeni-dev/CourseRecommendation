import sklearn.cluster as cluster


model = None
def Init():
	global model
	model = cluster.KMeans(n_clusters=4,max_iter=100000,random_state=30)

def Train(data):
	model.fit(data)
	return model.labels_

def getClusterCenters():
	return model.cluster_centers_

def getCost():
	return model.inertia_
