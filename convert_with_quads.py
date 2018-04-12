import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD


input_file = csv.DictReader(open("test_sheet.csv"))


# make a graph



for row in input_file:

	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	# print(row)
	#{'Subject Label': 'Pearl Wilmer Booker', 'Subject URI': 'None', 'Predicate Label': 'Daughter Of', 'Predicate URI': '', 'Predicate Symmetry': 'Asymmetric', 'Object Label': 'Mary Booker', 'Object URI': 'None'}
	# make a literal and add it
	# output_graph.add(  (URIRef(row['Subject URI']), RDFS.label, Literal(row['Subject Label'], lang='en')) )


	output_graph = Graph()
	# make a triple with the object as uri
	output_graph.add(  (URIRef(row['Subject URI']), URIRef(row['Predicate URI']), URIRef(row['Object URI'])) )	
	
	triple = output_graph.serialize(format='nt')	
	triple = str(triple, 'utf-8').strip()
	triple = triple.replace('.','')
	triple = f"{triple} <{row['Context']}> ."
	print(triple)


# output_graph.serialize(destination='my_graph.nt', format='nt')
