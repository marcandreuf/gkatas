class IHT:	
	ht :dict = dict()
	
	def set(self, data :int, hsvalue=None):
		hs = hash(data)
		if ht[hs] == None:
			ht[hs] = IhtNode(data)
		else:
			ht[hs].set(data, hs)


class IhtNode:
	data :int = None

	def __init__(value):
		self.data = value
		self.iht = IHT()






		



