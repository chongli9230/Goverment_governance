import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
import fpGrowth

f = open(u"E:/lab/12.分词聚类实体抽取/Q.txt", "r", encoding = 'utf-8')
string_data = f.read()
f.close()

#文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|，|！|？|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 自定义去除词库
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'通常',u'如果',u'我们',u'需要'] 

seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words:
        object_list.append(word) # 分词追加到列表


#########################词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
print(word_counts_top10) # 输出检查








