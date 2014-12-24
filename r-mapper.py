import cPickle as p

f=open('Test_site','r+')
o=open('Test_res','w')

shoplistfile = 'shoplist.data' 							                     		  
f1 = file(shoplistfile, 'w')
                                                                                                                                   

data={}

for line in f:
	
	try:
		url,description=line.split('\t',1)
	
	except ValueError:
		continue;
	
	print description
	
	for word in description.strip().split():
		word=word.lower()
		
		print '%s\t%s' %(word,url)
		o.write('%s\t%s\n' %(word,url))
		data[word]=url
		
p.dump(data, f1)
f.close()
f1.close()
o.close()

