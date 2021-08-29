import re
import sys 
def match_records(type_string):
    start_string=sys.argv[1]   
    return [match.group(0) for match in re.finditer(rf"OL\d+{type_string}",start_string)]

