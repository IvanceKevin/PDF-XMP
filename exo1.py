#!/usr/bin/python
# -*- coding: latin-1 -*-

import os, sys, re,rdflib, imghdr,subprocess

def _searchXMLContent(b) :
	"""
	Extract the XMP content from the byte stream, using a regular expression search
	@param b: byte stream of the image content
	@return: RDF data as a string
	@rtype: string
	"""
	rdfpat = r"(?sm)^.*(<rdf:RDF.*</rdf:RDF>)"
	r_rdf = re.compile(rdfpat)
	q = r_rdf.search(b)
	assert q != None, "Could not find the XMP content in the file"
	return q.group(1)

####################################################################################################
#g = rdflib.Graph()
#result = g.parse("/home/elbino/Workspace/Python/tdtp03/rdflib/src/pdf/test_articleCISP2008.pdf")

# print("graph has %s statements." % len(g))
# # prints graph has 79 statements.

# for subj, pred, obj in g:
#    if (subj, pred, obj) not in g:
#        raise Exception("It better be!")

# s = g.serialize(format='n3')
file_content=""

fname = "/home/elbino/Workspace/Python/tdtp03/rdflib/src/pdf/test_articleCISP2008.pdf"
#Transformatation du fichier PDF en flux de caractères
with open(fname,"rb") as f :
	file_buffer = f.read();
for byte in file_buffer:
	file_content += chr(ord(byte))
#print file_content
motif = re.compile('(?<=startxref\s)[\d]+(?=\s%%EOF$)')
recherche = motif.search(file_content)
if recherche is not None :
	obj = int (recherche.group())

motif2 = re.compile('[0-9]{10}\s[0-9]{5}\s[n]')
recherche = motif2.findall(file_content[obj:])


i=0
map = {}
for liste in recherche:
    liste=liste.split(' ', 1 )
    num=int(liste[0])
    map[i+1] = num
    i+=1
number = len(map)

# g = rdflib.Graph()
# rdf = _searchXMLContent(fname)
# print file_buffer

with open(fname,"rb") as f :
	rdf=_searchXMLContent(f.read())
print rdf.strip()

g = rdflib.Graph()
result = g.parse(data=rdf,format="application/rdf+xml")

g.serialize(destination="./test.xml",format="xml")

# # g représente le graphe RDF
for subject,predicat,obj in g:
	print subject,predicat,obj