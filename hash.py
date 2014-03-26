import random

class Hash:
	
	def __init__(self, m, t):
		self.m = m
		self.t = t
		self.fail = 0

		self.T1, self.T2 = [], []
		for x in range(0,m):
			self.T1.append(None)
			self.T2.append(None)

		self.h1 = lambda x: x % self.m
		self.h2 = lambda x: int(m*(x*(5**0.5 - 1)/2 % 1))
	
	def insert(self, x):

		def insertInT1(x):
			i = self.h1(x)
			tmp = self.T1[i]
			self.T1[i] = x
			return tmp

		def insertInT2(x):
			i = self.h2(x)
			tmp = self.T2[i]
			self.T2[i] = x
			return tmp

		fails = 0
		probes = 0
		print self.loadT1(),'\t',self.loadT2(),'\t',self.loadTotal(),'\t',	#For testing
		while fails < self.t:
			x = insertInT1(x)
			probes += 1	#For testing
			if x:
				x = insertInT2(x)
				probes += 1	#For testing
			if x:
				fails += 1
			else:
				print probes, "\tsuccess"	#For testing
				return True
		print probes, "\tfail"	#For testing
		return False

	#For testing
	def printTables(self):
		print self.T1
		print self.T2

	#For testing
	def loadT1(self):
		tmp = 0.0
		for x in self.T1:
			if x: tmp += 1
		return round(tmp/self.m,3)

	#For testing
	def loadT2(self):
		tmp = 0.0
		for x in self.T2:
			if x: tmp += 1
		return round(tmp/self.m,3)

	#For testing
	def loadTotal(self):
		return round((self.loadT1()+self.loadT2())/2,3)

m = 139
t = 32
testdata = random.sample(xrange(m*9238),m*2)
h = Hash(m, t)
print 'T1\tT2\tTot\tProbes'
for x in testdata:
	h.insert(x)
	if h.loadT1() > .063: break
h.printTables()
