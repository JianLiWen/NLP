import jieba
# 结巴分词
jieba.add_word('南开大学计算机学院')  # 添加词库
seg_list = jieba.cut(
    "我是来自南开大学计算机学院的硕士研究生文建丽", cut_all=True
)
print()
print("全模式: " + "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut(
    "我是来自南开大学计算机学院的硕士研究生文建丽"
)
print("精确模式："+"/".join(seg_list))  # 默认为精确模式
seg_list = jieba.cut_for_search(
    "我是来自南开大学计算机学院的硕士研究生文建丽"   # 搜索引擎模式
)
print("搜索引擎模式:"+"/".join(seg_list))

# 去除停用词
# 分好词的数据
fenci_list = [['我', '是', '来自', '南开大学计算机学院', '的', '学生', '文建丽'],['目前', '研究', '自然语言处理方向', '的', '东西', '呀']]
# 停用词表
stopwords = ['是', '的', '呀']
# 去掉文本中的停用词


def drop_stopwords(contents, stopwords):
    contents_clean = []
    for line in contents:
        line_clean = []
        for word in line:
            if word in stopwords:
                continue
            line_clean.append(word)
        contents_clean.append(line_clean)
    return contents_clean


print(drop_stopwords(fenci_list, stopwords))
