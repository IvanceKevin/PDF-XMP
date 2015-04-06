PDF/XMP
============

PDF/XMP v1 02 Avril 2015

by Ivance Kevin

Professor : Bertrand Frédéric

- [Introduction](#introduction)
- [ExtractionInformationPDF](#extractionInformationpdf)

## Introduction

Nous utilisons le langage **Python** à travers le package **re** (regular expressions), qui nous permet d'utiliser des expressions régulières pour **extraire** les métadonnées des documents PDF.
On utilisera également la bibliothèque [RDFlib](https://github.com/RDFLib/rdflib) pour interroger des données RDF.
- **Un ensemble de fichiers PDF** nous ont été fournit pour tester cela.

## ExtractionInformationPDF

Cette étape va nous permettre d'obtenir les informations structurelle du document PDF :

	- Le **nomnre d'ojets** dans le document.

	- Pour chaque objets : 

			- **adressse** (offset)

Nous avons rangé ces informations dans un **dictionnaire** dont la **clé** sera le numéro de l'objets et la **valeur** son adresse.

Exemple, pour le document articleCISP2008.pdf on doit obtenir :

![structure](./images/exempledico.png "structure du projet")