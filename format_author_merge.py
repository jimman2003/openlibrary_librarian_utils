import re
start_string=input("enter string with author olids: ")   
olids=[match.group(0) for match in re.finditer(r"OL\d+A",start_string)]
url_query='&key='.join(olids)
print(f"https://openlibrary.org/authors/merge?key={url_query}")
