import sklearn.cluster as cluster


model = None
def Init():
	"""
		This method initializes the model
	:return:
	"""
	global model
	model=None
	model = cluster.KMeans(n_clusters=4)
	return

def getRandomState():
	"""

	:return: random state associated with current model
	"""
	global model
	#todo code to find the random state of the model
	return 	model.random_state


def Train(data):
	"""
	Trains the model with the given data
	:param data: pandas dataframe initially may be changed later
	:return:
	"""
	model.fit(data)
	return model.labels_

def Predict(data):
	"""
	Predicts the cluster labels based on the data
	:param data: pandas dataframe and may be changed later
	:return: array of labels with a label each for a record or row in data
	"""
	return  model.predict(data)


def getClusterCenters():
	"""
	Get the cluster centers of the clusters that has been  formed due to Train
	:return: Cluster centers
	"""
	return model.cluster_centers_

def getCost():
	"""
	 Get the cost of the error
	:return: the total distance between each cluster and points attached to the cluster
	"""
	return model.inertia_

def getModel():
	"""
		returns the model

	:return: model
	"""
	return model
