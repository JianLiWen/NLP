#获取包含“爬虫”这个关键字的句子

import re
text_String = '利用爬虫抓取网络中的信息。爬取得策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分'
regex = '爬虫'
p_String = text_String.split('。')
for line in p_String:
    if(re.search(regex,line)) is not None:
        print(line)