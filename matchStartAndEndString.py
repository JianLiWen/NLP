#匹配起始和结尾字符串
import re
text_String = '文本最重要的来源无疑是网络。我们要把网络的文本获取形成一个文本数据库。' \
              '利用爬虫抓取网络中的信息。爬取得策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分'
regex = '^文本'
p_String = text_String.split('。')
for line in p_String:
    if(re.search(regex,line)) is not None:
        print(line)