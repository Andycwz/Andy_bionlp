from nltk.tokenize import sent_tokenize
data = open("D:/Desktop/nlp课程/drought_resistance_ab.txt", 'r', encoding='utf_8_sig').read().lower()
file = open("D:/Desktop/nlp课程/drought_resistance_sent.txt", 'w')
sentence = sent_tokenize(data)
keywords1 = ['drought resistance','|a|']
keywords2 = ['gene ']
result = [sen for sen in sentence if any([key in sen for key in keywords1])]
result1 = [sen for sen in result if any([key in sen for key in keywords2])]
j = 0
for i in result1:
    file.write(i + '\n\n')
    j=j+1
print (j)