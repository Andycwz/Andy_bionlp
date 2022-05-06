target_pubtator = open('D:/Desktop/nlp课程/rice.txt','r',encoding='utf-8')
sent_report = open('D:/Desktop/nlp课程/drought_resistance_ab.txt','w',encoding='utf-8')

def filter_sent(keyword1,keyword2):
#因为我们只需要知道抗旱性的性状和gene在一篇摘要中就好，所以只需要两个参数
    abstract_all = []
    for line in target_pubtator:#获取摘要
        if line[8:11] == '|a|':
            abstract = line.strip().split('|a|')[-1]
            abstract_all.append(abstract)
            continue
    i=0
    for each_abstract in abstract_all:
        if keyword1 in each_abstract and keyword2 in each_abstract:
            i=i+1
            print(i)
    print(i)
keyword1 = input("Please put in the keyword1:")
keyword2 = input("Please put in the keyword2:")
filter_sent(keyword1,keyword2)
