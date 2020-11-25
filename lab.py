from collections import Counter
import re
import math
import jiagu

#jiagu.init() # 可手动初始化，也可以动态初始化

f = open(u"E:/lab/12.分词聚类实体抽取/Q.txt", "r", encoding = 'utf-8')
#f_result1 = open("C:/Users/admin/Desktop/Q_result1.txt", "w", encoding = 'utf-8')
#f_result2 = open("C:/Users/admin/Desktop/Q_result2.txt", "w", encoding = 'utf-8')
f_result3 = open("C:/Users/admin/Desktop/Q_result3.txt", "w", encoding = 'utf-8')

text=[]
line = f.readline()
while line:
    text.append(line)
    line=f.readline()
    
#文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
text = re.sub(pattern, '', text)

#分词
words = []
for line in text:
    word = jiagu.seg(line[:-1])
    words.append(word)
    
    
''' 
#分词并做词性标注输出到文件
words = []
for line in text:
    word = jiagu.seg(line)
#    f_result1.write(str(word))
#    f_result1.write("\n")
#    words.append(word)
    pos = jiagu.pos(word)
#    f_result3.write(str(word))
#    f_result3.write("\n")
    for i in range(len(pos)-1):
        if(pos[i] == 'n'):
            f_result3.write(word[i])
        else:
            f_result3.write(pos[i])
        f_result3.write(' ') 
    f_result3.write("\n")        
    
   
#print(words)

#词性标注

    
    
    

#命名实体识别
for word in words:
    ner = jiagu.ner(word)
    for i in range(len(ner)):
        if ner[i] != 'O':
            f_result3.write(word[i])
        else:
            f_result3.write('O')
        f_result3.write(' ') 
    f_result3.write("\n")
#print(ner)


#知识图谱关系抽取
#knowlwdge = jiagu.knowledge(text)
#print(knowledge)


#关键词提取
#keywords = jiagu.keywords(text, 5) # 关键词
#print(keywords)

#文本摘要
#summarize = jiagu.summarize(text, 3) # 摘要
#print(summarize)

#情感分析
#sentiment = jiagu.sentiment(text)
#print(sentiment)


#文本聚类
cluster = jiagu.text_cluster(text,features_method='tfidf', method="dbscan",k=3, max_iter=100, eps=0.5, min_pts=2)	
f_result3.write(str(cluster))
print(cluster)
'''
#词频、频繁项集


'''
features = []
for sent in tokens:
    counter = Counter(sent)
    feature = [counter.get(x, 0) for x in vocab]
    features.append(feature)

print(features)
#return features, vocab

'''

f.close()
#f_result1.close()
#f_result2.close()
f_result3.close()

