#通过正则表达式匹配年份

import re
text_String = ['war of 1812','there are 5280 feet to a mile','happy new year 2016!']
regex = '[1-5][0-9]{3}'
year_strings = []
for line in text_String:
    if(re.search(regex,line)) is not None:
       year_strings.append(line)
    print(year_strings)