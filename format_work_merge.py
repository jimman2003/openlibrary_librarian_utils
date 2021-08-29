import re
start_string=input("enter string with work olids: ")   
olids=[match.group(0) for match in re.finditer(r"OL\d+W",start_string)]
print(f"https://testing.openlibrary.org/works/merge?records={','.join(olids)}")
