PDF/XMP
============

PDF/XMP v1 02 Avril 2015

by Ivance Kevin
Professor : Bertrand Frédéric

- [Introduction](#introduction)
- [ExtractionInformationPDF](#extractionInformationPDF)

## Introduction

Nous utilisons le langage **Python** à travers le package **re** (regular expressions), qui nous permet d'utiliser des expressions régulières pour **extraire** les métadonnées des documents PDF.
On utilisera également la bibliothèque [RDFlib](https://github.com/RDFLib/rdflib) pour interroger des données RDF.
- **Un ensemble de fichiers PDF** nous ont été fournit pour tester cela.

## ExtractionInformationPDF

Cette étape va nous permettre d'obtenir les informations structurelle du document PDF :
	- Le **nomnre d'ojets** dans le document.
	- Pour chaque objets : 
			- **adressse** (offset)