import cPickle as p

f=open('Test_data','r+')
o=open('Test_result','w')

shoplistfile = 'shoplist.data' 							                     		  
f1 = file(shoplistfile, 'w')
                                                                                                                                   

data={}

for line in f:
	
	for word in line.strip().split():
		word=word.lower()
		print '%s\t%s' %(word,1)
		o.write('%s\t%s\n' %(word,1))
		data[word]=1
		

p.dump(data, f1) 
f.close()
f1.close()
o.close()
