import cPickle as p

shoplistfile = 'shoplist.data' 	
f=open('Test_res','r+')
o=open('res','w')

f1 = file(shoplistfile)                                                            
data = p.load(f1)

for line in f:
	for k,v in data.items():

		try:
			word,url = line.split('\t', 1)
			word=word.lower()
			k=k.lower()
			
		except ValueError:
			continue
		
		if word == k:
			
	
for k,v in data.items():
	print k,v

	
f.close()
f1.close()
o.close()
	

