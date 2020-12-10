from random import randint, random
import math
import time
civils = []
def distance(pos1, pos2):
	return math.ceil(math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2+(pos1[2]-pos2[2])**2))
def share(n1, n2):
	for c in civils[n2].known_civil:
		if c not in civils[n1].known_civil:
			civils[n1].new_civil(c)
class Civilization(object):
	number = 0
	tech_points = 10
	position = (0, 0, 0)
	attitude = 0
	extinct = False
	known_civil = []
	def __init__(self):
		super(Civilization, self).__init__()
		self.number = len(civils)
		self.position = (randint(-10000,10000), randint(-10000,10000), randint(-10000,10000))
		self.attitude = randint(-1,1)
	def dev(self):
		self.tech_points = int((self.tech_points + randint(5, 15))*1.05)
	def search_range(self):
		return max(int(2**int((self.tech_points)/7000)), int((self.tech_points)/100), 10)
	def search(self):
		for i, c in enumerate(civils):
			d = distance(self.position, c.position)
			if d < self.search_range() and d != 0 and i not in self.known_civil and c.extinct != True:
				self.new_civil(i)
	def new_civil(self, number):
		self.known_civil.append(number)
		if self.attitude == -1:
			self.attack(number)
		elif self.attitude == 1:
			self.ally(number)
	def attack(self, number):
		if self.tech_points > civils[number].tech_points:
			civils[number].extinct = True
			self.tech_points += int(civils[number].tech_points*random()/2)
			share(self.number, number)
		elif self.tech_points < civils[number].tech_points and civils[number].attitude != 1:
				self.extinct = True
				civils[number].tech_points += int(self.tech_points*random()/2)
				share(number, self.number)
	def ally(self, number):
		if civils[number].attitude != -1:
			total_points = self.tech_points + civils[number].tech_points
			self.tech_points += int(total_points*random()/40)
			civils[number].tech_points += int(total_points*random()/40)
			share(number, self.number)
			share(self.number, number)
		else:
			civils[number].attack(self.number)
	def grow(self):
		if self.extinct == False:
			self.dev()
			self.search()
			if self.attitude == -1:
				for i in self.known_civil:
					if civils[i].extinct != True and distance(self.position, civils[i].position) < self.search_range():
						self.attack(i)
			elif self.attitude == 1:
				for i in self.known_civil:
					if civils[i].extinct != True and distance(self.position, civils[i].position) < self.search_range():
						self.ally(i)

for i in range(0, 1000):
	civils.append(Civilization())
cnt = 0
while True:
	put = input("Continue?(y/n/int)")
	try:
		a = max(1, int(put))
	except:
		if put == 'n':
			quit()
		else:
			a = 1
	for i in range(a):
		t = time.time()
		if randint(1, 10) == 5:
			civils.append(Civilization())
		tmp = 0
		outon = False	
		for c in civils:
			tmp += 1
			c.grow()
			if outon == False:
				if time.time() - t > 60:
					outon = True
			else:
				print(tmp)
		snum = 0
		alive_point = 0
		alive_number = 0
		f_num = 0
		n_num = 0
		a_num = 0
		for c in civils:
			if c.extinct != True:
				if c.tech_points > civils[snum].tech_points:
					snum = c.number
				alive_number += 1
				alive_point += c.tech_points
				if c.attitude == 1:
					f_num += 1
				elif c.attitude == 0:
					n_num += 1
				else:
					a_num += 1
		if a != 1:
			print("[" + str(i+1), "/", str(a) + "]")
		cnt += 1
	print("[*]Century:", cnt)
	print("[*]Total Alive:",f_num + n_num + a_num, "of", len(civils))
	print("[*]Friendly Civilizations:", f_num)
	print("[*]Neutrally Civilizations:", n_num)
	print("[*]Aggressively Civilizations:", a_num)
	print("[*]Strongest Civilization:", snum)
	print("[*]Attitude:", civils[snum].attitude)
	print("[*]Technology Points:", civils[snum].tech_points)
	print("[*]Average Technology Points:", int(alive_point / alive_number))