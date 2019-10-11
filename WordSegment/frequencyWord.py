# 高频词提取


# 进行数据下的读取，加载制定路径下的数据
def get_content(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()  # 移除字符串头尾指定的字符
            content += l
        return content


# 定义高频词统计的函数，输入是一个词的数组
def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0)+1  # get返回指定键的值，如果值不在字典中返回default值0
    return sorted(tf_dic.items(), key=lambda x: x[1], reverse=True)[:topK]


def main():
    import glob2
    import random
    import jieba
    files = glob2.glob('./data/news/C000013/*.text')   # 所有的路径
    corpus = [get_content(x) for x in files]    # 数组，元素为每一个text的文本内容
    sample_inx = random.randint(0, len(corpus))  # 生成随机数
    split_words = list(jieba.cut(corpus[1]))   # 分词数组
    print('样本之一'+corpus[1])
    print('样本分词效果:'+'/'.join(split_words))
    print('样本的topK词：'+str(get_TF(split_words)))


main()
