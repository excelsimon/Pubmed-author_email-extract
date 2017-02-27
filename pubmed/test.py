emailList = []
f = open('test.txt','r')
for ln in f:
	if ' ' in ln:
		continue
	emailList.append(ln)
print 'emailList: ',emailList
