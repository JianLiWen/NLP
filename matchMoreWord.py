# 使用中括号匹配多个字符
#“[bcr]at”代表的是bat,cat,rat

import re
text_String = 'b[重要的]利用爬虫抓取网络中的信息。爬取得策略有广度爬取和深度爬取。[紧要的]根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分'
regex = '^\[[重紧]..\]'
p_String = text_String.split('。')
for line in p_String:
    if(re.search(regex,line)) is not None:
        print(line)
    else:
        print('no match')