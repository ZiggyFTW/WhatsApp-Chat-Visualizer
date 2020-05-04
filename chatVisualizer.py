import matplotlib.pyplot as plt
import pandas as pd
from math import pi

class Message():
	"""Message class
	each msg is a single line from a person
	param: string the msg
	param: int number of words
	param: string the date"""
	def __init__(self, sender, msg, date, time):
		self.sender = sender
		self.msg = msg
		self.date = date
		self.time = time
		
	def calcWords(self):
		count = 0
		for x in msg.split():
			count +=1
		return count

	def calcCharacters(self):
		"""Does NOT include spaces, does include syntax"""
		count = 0
		for x in msg.split():
			count += len(x)
		return count

	def getTime(self):
		"""using 1200 hour system, no AM/PM"""
		if "pm" in time:
			if len(time) > 7:
				hour = (int(time[0:-6]) *100 + 1200) + int(time[3:-3])
			else:
				hour = (int(time[0:-6]) *100 + 1200) + int(time[2:-3])
		else:
			if len(time) > 7:
				hour = (int(time[0:-6]) *100) + int(time[3:-3])
			else:
				hour = (int(time[0:-6]) *100) + int(time[2:-3])
		return hour

	def getSender(self):
		return sender
	
	def __repr__(self):
		return ("%s %s %s 	 %s"%(sender, date, time, msg))


usr1 = []
usr2 = []
timeCountUsr1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
timeCountUsr2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
chat = open("whats app text data file",'r')
for x in chat.readlines():
	line = x.split()
	print(line)
	if(line[4][0:].endswith(":")):
		sender = "%s" % (line[4][0:-1])
	else:
		sender = "%s" % (line[4][0:])
	msg = ""
	for y in range(5,len(line)):
		msg = msg + line[y] + " "
	date = "%s" % (line[0])
	time = "%s %s" % (line[1],line[2])
	a= Message(sender, msg, date, time)
	curTime = a.getTime()
	if a.getSender() == "person1":
		usr1 += [curTime]
		if curTime < 100 and curTime > 0:
			timeCountUsr1[0] +=1
		if curTime < 200 and curTime > 100:
			timeCountUsr1[1] +=1
		if curTime < 300 and curTime > 200:
			timeCountUsr1[2] +=1
		if curTime < 400 and curTime > 300:
			timeCountUsr1[3] +=1
		if curTime < 500 and curTime > 400:
			timeCountUsr1[4] +=1
		if curTime < 600 and curTime > 500:
			timeCountUsr1[5] +=1
		if curTime < 700 and curTime > 600:
			timeCountUsr1[6] +=1
		if curTime < 800 and curTime > 700:
			timeCountUsr1[7] +=1
		if curTime < 900 and curTime > 800:
			timeCountUsr1[8] +=1
		if curTime < 1000 and curTime > 900:
			timeCountUsr1[9] +=1
		if curTime < 1100 and curTime > 1000:
			timeCountUsr1[10] +=1
		if curTime < 1200 and curTime > 1100:
			timeCountUsr1[11] +=1
		if curTime < 1300 and curTime > 1200:
			timeCountUsr1[12] +=1
		if curTime < 1400 and curTime > 1300:
			timeCountUsr1[13] +=1
		if curTime < 1500 and curTime > 1400:
			timeCountUsr1[14] +=1
		if curTime < 1600 and curTime > 1500:
			timeCountUsr1[15] +=1
		if curTime < 1700 and curTime > 1600:
			timeCountUsr1[16] +=1
		if curTime < 1800 and curTime > 1700:
			timeCountUsr1[17] +=1
		if curTime < 1900 and curTime > 1800:
			timeCountUsr1[18] +=1
		if curTime < 2000 and curTime > 1900:
			timeCountUsr1[19] +=1
		if curTime < 2100 and curTime > 2000:
			timeCountUsr1[20] +=1
		if curTime < 2200 and curTime > 2100:
			timeCountUsr1[21] +=1
		if curTime < 2300 and curTime > 2200:
			timeCountUsr1[22] +=1


	if a.getSender() == "person2":
		usr2 += [curTime]
		if curTime < 100 and curTime > 0:
			timeCountUsr2[0] +=1
		if curTime < 200 and curTime > 100:
			timeCountUsr2[1] +=1
		if curTime < 300 and curTime > 200:
			timeCountUsr2[2] +=1
		if curTime < 400 and curTime > 300:
			timeCountUsr2[3] +=1
		if curTime < 500 and curTime > 400:
			timeCountUsr2[4] +=1
		if curTime < 600 and curTime > 500:
			timeCountUsr2[5] +=1
		if curTime < 700 and curTime > 600:
			timeCountUsr2[6] +=1
		if curTime < 800 and curTime > 700:
			timeCountUsr2[7] +=1
		if curTime < 900 and curTime > 800:
			timeCountUsr2[8] +=1
		if curTime < 1000 and curTime > 900:
			timeCountUsr2[9] +=1
		if curTime < 1100 and curTime > 1000:
			timeCountUsr2[10] +=1
		if curTime < 1200 and curTime > 1100:
			timeCountUsr2[11] +=1
		if curTime < 1300 and curTime > 1200:
			timeCountUsr2[12] +=1
		if curTime < 1400 and curTime > 1300:
			timeCountUsr2[13] +=1
		if curTime < 1500 and curTime > 1400:
			timeCountUsr2[14] +=1
		if curTime < 1600 and curTime > 1500:
			timeCountUsr2[15] +=1
		if curTime < 1700 and curTime > 1600:
			timeCountUsr2[16] +=1
		if curTime < 1800 and curTime > 1700:
			timeCountUsr2[17] +=1
		if curTime < 1900 and curTime > 1800:
			timeCountUsr2[18] +=1
		if curTime < 2000 and curTime > 1900:
			timeCountUsr2[19] +=1
		if curTime < 2100 and curTime > 2000:
			timeCountUsr2[20] +=1
		if curTime < 2200 and curTime > 2100:
			timeCountUsr2[21] +=1
		if curTime < 2300 and curTime > 2200:
			timeCountUsr2[22] +=1

print(usr1)
print(usr2)


print(timeCountUsr1)
print(timeCountUsr2)


df = pd.DataFrame({
'group': ['A','B','C','D'],
'0000': [int(timeCountUsr1[0]), timeCountUsr2[0], 30, 4],
'0100': [int(timeCountUsr1[1]), timeCountUsr2[1], 40, 34],
'0200': [int(timeCountUsr1[2]), timeCountUsr2[2], 23, 24],
'0300': [int(timeCountUsr1[3]), timeCountUsr2[3], 33, 14],
'0400': [int(timeCountUsr1[4]), timeCountUsr2[4], 32, 14],
'0500': [int(timeCountUsr1[5]), timeCountUsr2[5], 30, 4],
'0600': [int(timeCountUsr1[6]), timeCountUsr2[6], 9, 34],
'0700': [int(timeCountUsr1[7]), timeCountUsr2[7], 23, 24],
'0800': [int(timeCountUsr1[8]), timeCountUsr2[8], 33, 14],
'0900': [int(timeCountUsr1[9]), timeCountUsr2[9], 32, 14],
'1000': [int(timeCountUsr1[10]), timeCountUsr2[10], 30, 4],
'1100': [int(timeCountUsr1[11]), timeCountUsr2[11], 9, 34],
'1200': [int(timeCountUsr1[12]), timeCountUsr2[12], 23, 24],
'1300': [int(timeCountUsr1[13]), timeCountUsr2[13], 33, 14],
'1400': [int(timeCountUsr1[14]), timeCountUsr2[14], 32, 14],
'1500': [int(timeCountUsr1[15]), timeCountUsr2[15], 30, 4],
'1600': [int(timeCountUsr1[16]), timeCountUsr2[16], 9, 34],
'1700': [int(timeCountUsr1[17]), timeCountUsr2[17], 23, 24],
'1800': [int(timeCountUsr1[18]), timeCountUsr2[18], 33, 14],
'1900': [int(timeCountUsr1[19]), timeCountUsr2[19], 32, 14],
'2000': [int(timeCountUsr1[20]), timeCountUsr2[20], 30, 4],
'2100': [int(timeCountUsr1[21]), timeCountUsr2[21], 9, 34],
'2200': [int(timeCountUsr1[22]), timeCountUsr2[22], 23, 24],
'2300': [int(timeCountUsr1[23]), timeCountUsr2[23], 33, 14]
})
 
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10], ["70"], color="grey", size=7)
plt.ylim(0,70)
 
 
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Des")
ax.fill(angles, values, 'b', alpha=0.1)

# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Elizabeth")
ax.fill(angles, values, 'r', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()
