import random as rd
from datetime import date
import time
import matplotlib.pyplot as plt


class guest:
	def __init__(self, FIO, room, price, dayIn, dayOut):
		self.fio = FIO
		self.room = room
		self.price = price
		self.dayIn = dayIn
		self.dayOut = dayOut

	def creator (person):
		tmp = person.split(";")
		return guest(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4])
		
	def __gt__(self, other):
		if self.dayIn > other.dayIn:
			return True
		elif self.dayIn == other.dayIn and self.room > other.room:
			return True
		elif self.dayIn == other.dayIn and self.room == other.room and self.fio > other.fio:
			return True
		return False

	def __ge__(self, other):
		if self.dayIn > other.dayIn:
			return True
		elif self.dayIn == other.dayIn and self.room >= other.room:
			return True
		elif self.dayIn == other.dayIn and self.room == other.room and self.fio >= other.fio:
			return True
		return False

	def __lt__ (self, other):
		if self.dayIn < other.dayIn:
			return True
		elif self.dayIn == other.dayIn and self.room < other.room:
			return True
		elif self.dayIn == other.dayIn and self.room == other.room and self.fio < other.fio:
			return True
		return False

	def __le__ (self, other):
		if self.dayIn < other.dayIn:
			return True
		elif self.dayIn == other.dayIn and self.room < other.room:
			return True
		elif self.dayIn == other.dayIn and self.room == other.room and self.fio <= other.fio:
			return True
		return False

	def __str__(self):
		return ";".join([self.fio, str(self.room), str(self.price), str(self.dayIn), str(self.dayOut)])
	
	def getRandomGuest():
		alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
		
		name = ''.join(rd.choices(alph, k=rd.randint(4, 12))).title() 
		surname = ''.join(rd.choices(alph, k=rd.randint(4, 12))).title() 
		middlename = ''.join(rd.choices(alph, k=rd.randint(4, 12))).title() 
		fio = surname + ' ' + name + ' ' + middlename
		room = rd.randint(1, 500)
		
		d = rd.randint(1,28) 
		m = rd.randint(1,12)
		y = rd.randint(1950, 2025)
		dayIn = date(y, m, d)
		
		d1 = rd.randint(1,28) 
		m1 = rd.randint(1,12)
		y1 = rd.randint(1950,2025)
		dayOut = date(y1, m1, d1)
		price = rd.randint(1000, 5000)

		return guest(fio,room,price,dayIn, dayOut)


def genGuests(N):
	filename = f"file{N}.txt"
	with open(filename, "w") as f:
		for i in range(N):    
			f.write(str(guest.getRandomGuest())+"\n")

def readGuests(N):
	filename = f"file{N}.txt"
	allGuests = []
	with open(filename, "r") as f:
		for line in f.readlines():
			p = guest.creator(line)
			allGuests.append(p)
	return allGuests

#def init():
#	allGuests = []
#	with open(file.txt, "r") as guests:
#		for line in guests.readlines():
#			p = guest.creator(line)
#			allGuests.append(p)

def insertionSort(arr): 
	for i in range(1, len(arr)): 
		m = arr[i] 
		k = i-1
		while k >= 0 and m < arr[k] : 
				arr[k + 1] = arr[k] 
				k = k - 1
		arr[k + 1] = m
	return arr


def quickSort(arr):
	if len(arr) <= 1:
		return arr
	else:
		rnd = rd.choice(arr)        
	left = []
	m = [] 
	right = [] 
	for i in arr:
		if i < rnd:
			left.append(i)             
	m = [rnd] * arr.count(rnd)            
	for i in arr:
		if i > rnd:
			right.append(i) 
	return quickSort(left) + m + quickSort(right)

def cocktailSort(data):
	left = 0
	right = len(data) - 1
	while left <= right:
		for i in range(left, right):
			if data[i] > data[i + 1]:
				data[i], data[i + 1] = data[i + 1], data[i]
		right -= 1

		for i in range(right, left, -1):
			if data[i - 1] > data[i]:
				data[i], data[i - 1] = data[i - 1], data[i]
		left += 1

def draw(text, xs, ys):
	print(text)
	fig0, ax0 = plt.subplots()
	ax0.set_xscale("log")
	ax0.set_yscale("log")
	plt.plot(xs, ys)
	plt.show()


def main():
	xs = [50, 100, 500, 1000, 5000]
	
	#for x in xs:
	#	genGuests(x)
	#return 
	
	ysQS = []
	ysCS = []
	ysIS = [] 
	data = []

	for i in range(5):
		data=readGuests(xs[i])
		start = time.time()
		insertionSort(data)
		end = time.time() - start
		ysIS.append(end)

	for i in range(5):  
		data=readGuests(xs[i])
		start = time.time()
		quickSort(data)
		end = time.time() - start
		ysQS.append(end)

	for i in range(5):
		data=readGuests(xs[i])
		start = time.time()
		cocktailSort(data)
		end = time.time() - start
		ysCS.append(end)   

	draw("Insertion Sort", xs, ysIS)
	draw("Quick Sort", xs, ysQS)
	draw("Cocktail Sort", xs, ysCS)


main()
