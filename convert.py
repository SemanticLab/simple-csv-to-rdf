import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD


input_file = csv.DictReader(open("test_sheet.csv"))


# make a graph
output_graph = Graph()


for row in input_file:

	# convert it from an OrderedDict to a regular dict
	row = dict(row)

	#{'Subject Label': 'Pearl Wilmer Booker', 'Subject URI': 'None', 'Predicate Label': 'Daughter Of', 'Predicate URI': '', 'Predicate Symmetry': 'Asymmetric', 'Object Label': 'Mary Booker', 'Object URI': 'None'}
	# make a literal and add it
	output_graph.add(  (URIRef(row['Subject URI']), RDFS.label, Literal(row['Subject Label'], lang='en')) )

	# make a triple with the object as uri
	output_graph.add(  (URIRef(row['Subject URI']), URIRef(row['Predicate URI']), URIRef(row['Object URI'])) )	



output_graph.serialize(destination='my_graph.nt', format='nt')
