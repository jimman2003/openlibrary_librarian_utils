from format_merge_common import match_records

url_query='&key='.join(match_records("A"))
print(f"https://openlibrary.org/authors/merge?key={url_query}")
