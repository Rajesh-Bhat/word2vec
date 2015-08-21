import nltk
import gensim
import os
import sys

def tokenizer(path,filename):
	'''returns tokens obtained from the dataset'''
	
	with open(path+filename) as dataset:
		tokens=[nltk.word_tokenize(sentence) for sentence in nltk.sent_tokenize(dataset.read().lower())]
	
	
			
	return tokens			


if __name__=='__main__':
	tokens=tokenizer("datasets/","data.txt")

	#print tokens
	#print len(tokens)
	model = gensim.models.Word2Vec(tokens,size=32)

	
	print "---------vector representation of word---------"
	print "abdul:",model['abdul']
	print "kalam:",model['kalam']
	
	print "--------------most similar words---------------"
	print "abdul",model.most_similar('abdul')
	print "india",model.most_similar('india')
	print "politician",model.most_similar('politician')
	print "modi",model.most_similar('modi')
			
