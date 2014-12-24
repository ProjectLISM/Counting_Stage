import cPickle as p

shoplistfile = 'shoplist.data' 	
f=open('Test_result','r+')
o=open('result','w')

f1 = file(shoplistfile)                                                            
data = p.load(f1)


for line in f:
	for k,v in data.items():
		word,count = line.split('\t', 1)
		word=word.lower()
		k=k.lower()
		try:
			v=int(v)
		except ValueError:
			continue
		if word == k:
			data[k]=v+1
	
for k,v in data.items():
	print k,v

	
f.close()
f1.close()
o.close()
	
