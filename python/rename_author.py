#Warning not tested
from olclient.openlibrary import OpenLibrary
from sys import argv
ol = OpenLibrary()
author_olid = ol.Author.get_olid_by_name(argv[1]) 
author_obj = ol.get(author_olid) # or ol.get(<olid of choice>)
print(author_obj.name)
author_obj.name=argv[2]
print(author_obj.name)
#author_obj.save()
