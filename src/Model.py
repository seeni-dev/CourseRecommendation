import sklearn.cluster as cluster


model = None
def Init():
	global model
	model=None
	model = cluster.KMeans(n_clusters=4)
	return

def getRandomState():
	global model
	#todo code to find the random state of the model
	return 	model.random_state


def Train(data):
	model.fit(data)
	return model.labels_

def Predict(data):
    return  model.predict(data)


def getClusterCenters():
	return model.cluster_centers_

def getCost():
	return model.inertia_
