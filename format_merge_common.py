import re
import sys 
def match_records(type_string):
    args=sys.argv[1:]
    return [match.group(0) for arg in args for match in re.finditer(rf"OL\d+{type_string}",arg)] 
     

