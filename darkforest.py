import random
def Get_Index_Can_Find(frange,self_index,index_sum):
	ans = []
	if self_index + frange < index_sum:
		for i in xrange(self_index + 1,self_index + frange + 1):
			if i != self_index:
				ans.append(i)
	else:
		for i in xrange(self_index + 1,index_sum):
				ans.append(i)
	return ans
Civilization_Attitude = []
Civilization_Technology = []
Civilization_Extinct = []
save_log = False
Continnue = "y"
print "Welcome to the Dark Forest..."
if raw_input("Do you want to save log[y/n]:") == "y":
	save_log = True
	f = open("details.log", "w")
	log_text = ""
Civilization_Number = input("Please set the number of civilizations:\n")
print "Set successfully."
if save_log:
	log_text += "number of civilizations: " + str(Civilization_Number) + "\n"
Attitude_Set = raw_input("Please set attitude to the alien of each civilization. If you want to be random, input:random. Other behaviors are considered manual input:\n")
if Attitude_Set != "random" and Civilization_Number <= 10:
	print "Please set attitude to the alien of each civilization. 0 stands for neutrality, 1 stands for friendly, and -1 stands for aggressively."
	for i in xrange(1,Civilization_Number+1):
		Civilization_Attitude.append(input("Set civilization" + str(i) + ":"))
		if save_log:
			if Civilization_Attitude[i-1] == -1:
				log_text += "civilization" + str(i+1) + ": aggressively\n"
			if Civilization_Attitude[i-1] == 0:
				log_text += "civilization" + str(i+1) + ": neutrality\n"
			if Civilization_Attitude[i-1] == 1:
				log_text += "civilization" + str(i+1) + ": friendly\n"
		Civilization_Technology.append(10)
		Civilization_Extinct.append(False)
	print "Set successfully."
else:
	if Civilization_Number > 10:
		print "The number of civilizations is too large."
	print "Begin to random the attitudes..."
	for i in xrange(0,Civilization_Number):
		Civilization_Attitude.append(random.randint(-1,1))
		if save_log:
			if Civilization_Attitude[i] == -1:
				log_text += "civilization" + str(i+1) + ": aggressively\n"
			if Civilization_Attitude[i] == 0:
				log_text += "civilization" + str(i+1) + ": neutrality\n"
			if Civilization_Attitude[i] == 1:
				log_text += "civilization" + str(i+1) + ": friendly\n"
		Civilization_Technology.append(10)
		Civilization_Extinct.append(False)
	print "Set successfully."
print "Start..."
while Continnue == "y":
	Skip_Years = input("Set years to skip:\n")
	if save_log:
		log_text += "After " + str(Skip_Years) + " years\n"
	for i in xrange(0,Skip_Years+1):
		for j in xrange(0,Civilization_Number):
			if Civilization_Extinct[j] == False:
				Civilization_Technology[j] += random.randint(5,15)
				ICF = Get_Index_Can_Find(Civilization_Technology[j]/100,i,Civilization_Number)
				if Civilization_Attitude[j] == 1:
					for m in ICF:
						if Civilization_Extinct[m] != True:
							if Civilization_Attitude[m] == 0 or Civilization_Attitude[m] == 1:
								Civilization_Technology[m] += Civilization_Technology[j]/100
								Civilization_Technology[j] += Civilization_Technology[m]/100
								if save_log:
									log_text += "civilization" + str(j+1) + " ally with civilization" + str(m+1) + "\n"
							else:
								if(Civilization_Technology[m] > Civilization_Technology[j]):
									Civilization_Technology[m] += Civilization_Technology[j]/20
									Civilization_Extinct[j] = True
									if save_log:
										log_text += "civilization" + str(j+1) + " has been destroyed by civilization" + str(m+1) + "\n"
									break
				elif Civilization_Attitude[j] == -1:
					for m in ICF:
						if Civilization_Extinct != True:
							if(Civilization_Technology[m] < Civilization_Technology[j]):
								Civilization_Technology[j] += Civilization_Technology[m]/20
								Civilization_Extinct[m] = True
								if save_log:
									log_text += "civilization" + str(m+1) + " has been destroyed by civilization" + str(j+1) + "\n"
							else:
								if Civilization_Attitude[m] != 1:
									Civilization_Technology[m] += Civilization_Technology[j]/20
									Civilization_Extinct[j] = True
									if save_log:
										log_text += "civilization" + str(j+1) + " has been destroyed by civilization" + str(m+1) + "\n"
									break
	Rest_Neutrality = 0
	Rest_Friendly = 0
	Rest_Aggressively = 0
	Rest_Neutrality_Technology = 0
	Rest_Friendly_Technology = 0
	Rest_Aggressively_Technology = 0
	Extinct_Number = 0
	for i in xrange(0,Civilization_Number):
		if Civilization_Extinct[i] == True:
			Extinct_Number += 1
		elif Civilization_Attitude[i] == -1:
			Rest_Aggressively += 1
			Rest_Aggressively_Technology += Civilization_Technology[i]
		elif Civilization_Attitude[i] == 0:
			Rest_Neutrality += 1
			Rest_Neutrality_Technology += Civilization_Technology[i]
		elif Civilization_Attitude[i] == 1:
			Rest_Friendly += 1
			Rest_Friendly_Technology += Civilization_Technology[i]
	print "There are " + str(Rest_Friendly) + " friendly civilizations left. They have " + str(Rest_Friendly_Technology) + " Technology points in all."
	print "There are " + str(Rest_Neutrality) + " neutrality civilizations left. They have " + str(Rest_Neutrality_Technology) + " Technology points in all."
	print "There are " + str(Rest_Aggressively) + " aggressively civilizations left. They have " + str(Rest_Aggressively_Technology) + " Technology points in all."
	print str(Extinct_Number) + " civilizations have been extincted."
	if save_log:
		log_text += "There are " + str(Rest_Friendly) + " friendly civilizations left. They have " + str(Rest_Friendly_Technology) + " Technology points in all.\nThere are " + str(Rest_Neutrality) + " neutrality civilizations left. They have " + str(Rest_Neutrality_Technology) + " Technology points in all.\nThere are " + str(Rest_Aggressively) + " aggressively civilizations left. They have " + str(Rest_Aggressively_Technology) + " Technology points in all.\n" + str(Extinct_Number) + " civilizations have been extincted.\n"
	Continnue = raw_input("Are you sure to Continnue?[y/n]:")
if save_log:
	f.write(log_text)
	f.close()