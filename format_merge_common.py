import re
def match_records(type_string):
    start_string=input("enter string with work olids: ")   
    return [match.group(0) for match in re.finditer(rf"OL\d+{type_string}",start_string)]

