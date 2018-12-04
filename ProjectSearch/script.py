f1 = open("HourTransaction.txt",'r')

joblevel ={}
for line in f1:
	top = line[0:5]
	if top not in joblevel:
		joblevel[top] = True
f1.close()
f2 = open("AllProject,txt",'r')
for line in f2:
	line = line.strip("\n")
	if line not in joblevel:
		print("Found: ",line)
