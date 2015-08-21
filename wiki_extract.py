import os
import  wikipedia 


def remove_non_ascii(text):
	return ''.join([i if ord(i) < 128 else ' ' for i in text])


def get_pages(names):
	'''names is a list of names to be queried on wiki'''
	pages = []
	
	for name in names:
		page = wikipedia.page(name, auto_suggest = True)
		if page != None:
			pages.append({"name": name, "page": page})        
	
	return pages

def create_ds(names, pth):
	'''names is a list of names to be queried on wiki'''
	os.chdir(pth+"/datasets")
	pages = get_pages(names)
	
	for page in pages:
		text = page["page"].content
		f = open(page["name"], "wb")
		
		f.write(remove_non_ascii(text))
		f.close()
	return pages

if __name__ == '__main__':
	''' enter the names of wiki article in the list names to extract wiki data'''
	
	names = ["Narendra Modi", "Sonia Gandhi", "Abdul Kalam", "Abraham Lincoln",
			"Rajiv Gandhi", "Barack Obama", "George W Bush", "Hillary Clinton"]
	
	cur_dir=os.getcwd()
		        
	dir_contents=os.listdir(cur_dir)
	
	if 'datasets' not in dir_contents:
		print "creating a directory datasets"
		os.mkdir('datasets')
	
	pages = create_ds(names,cur_dir)			                	
