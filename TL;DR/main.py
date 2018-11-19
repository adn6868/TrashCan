f = open('b.txt','r')
para = []
for line in f:
	para.append(line.strip('\n'))

f.close()
sentance = []

for line in para:
	sentance += line.split(".")

adict = {}
for sent in sentance:
	for word in sent.split(" "):
		if word not in adict:
			adict[word] = 1
		else:
			adict[word] += 1
bdict ={}
for sent in sentance:
	cur = 0
	for word in sent.split(" "):
		cur += adict[word]
	bdict[cur] = sent

for k in sorted(bdict.keys(),reverse = False):
	print(bdict[k]+'\n')