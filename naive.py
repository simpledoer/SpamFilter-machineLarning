import random
stopword = ('a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am','an','and','any','are','aren',"aren't",'as','at','be','because','been','before','being','below','between','both','but',
            'by',
            'can',
            'couldn',
            "couldn't",
            'd',
            'did',
            'didn',
            "didn't",
            'do',
            'does',
            'doesn',
            "doesn't",
            'doing',
            'don',
            "don't",
            'down',
            'during',
            'each',
            'few',
            'for',
            'from',
            'further',
            'had',
            'hadn',
            "hadn't",
            'has',
            'hasn',
            "hasn't",
            'have',
            'haven',
            "haven't",
            'having',
            'he',
            'her',
            'here',
            'hers',
            'herself',
            'him',
            'himself',
            'his',
            'how',
            'i',
            'if',
            'in',
            'into',
            'is',
            'isn',
            "isn't",
            'it',
            "it's",
            'its',
            'itself',
            'just',
            'll',
            'm',
            'ma',
            'me',
            'mightn',
            "mightn't",
            'more',
            'most',
            'mustn',
            "mustn't",
            'my',
            'myself',
            'needn',
            "needn't",
            'no',
            'nor',
            'not',
            'now',
            'o',
            'of',
            'off',
            'on',
            'once',
            'only',
            'or',
            'other',
            'our',
            'ours',
            'ourselves',
            'out',
            'over',
            'own',
            're',
            's',
            'same',
            'shan',
            "shan't",
            'she',
            "she's",
            'should',
            "should've",
            'shouldn',
            "shouldn't",
            'so',
            'some',
            'such',
            't',
            'than',
            'that',
            "that'll",
            'the',
            'their',
            'theirs',
            'them',
            'themselves',
            'then',
            'there',
            'these',
            'they',
            'this',
            'those',
            'through',
            'to',
            'too',
            'under',
            'until',
            'up',
            've',
            'very',
            'was',
            'wasn',
            "wasn't",
            'we',
            'were',
            'weren',
            "weren't",
            'what',
            'when',
            'where',
            'which',
            'while',
            'who',
            'whom',
            'why',
            'will',
            'with',
            'won',
            "won't",
            'wouldn',
            "wouldn't",
            'y',
            'you',
            "you'd",
            "you'll",
            "you're",
            "you've",
            'your',
            'yours',
            'yourself', 'yourselves')
'''fil=open('D:\study\sem 6\machine learning\dataset_NB.txt','a')
fil.write(" ")
fil.close()'''
file = open('D:\study\sem 6\machine learning\dataset_NB.txt')  #opening the specified dataset
lines = file.readlines()
if lines[-1][-1]!=" ":
    lines[-1]+=" "

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
spam_dict = {}
Nonspam_dict = {}

def processor1(text, num):
    for i in text:
        if i in punc:
            text = text.replace(i, "")
    wordslist = text.split()
    for word in wordslist:
        if word in stopword:
            pass
        else:
            if num == '0':
                if word in spam_dict:
                    spam_dict[word] = spam_dict[word] + 1
                else:
                    spam_dict[word] = 1
            if num == '1':
                if word in Nonspam_dict:
                    Nonspam_dict[word] = Nonspam_dict[word] + 1
                else:
                    Nonspam_dict[word] = 1

acuarr=[]
randarr=[]
for i in range(1000):
    randarr.append(i)

random.shuffle(randarr)

randarr=[randarr[i::7] for i in range(7)]

fold=0
for k in range(7):
    for i in range(7):
        if i!=k:
            for j in randarr[i]:
                processor1(lines[j][0:-3].lower(), lines[j][-2])

    accuracy=0
    for l in randarr[k]:
        test_dict = {}
        testline=lines[l][0:-3].lower()
        for i in testline:
            if i in punc:
                testline = testline.replace(i, "")
        wordslist = testline.split()
        for word in wordslist:
            if word in stopword:
                pass
            else:
                if word in test_dict:
                    test_dict[word] = test_dict[word] + 1
                else:
                    test_dict[word] = 1
        spamscore = 1
        nonspamscore = 1
        for word in test_dict.keys():
            spamprob = 1
            nonspamprob = 1

            if word in spam_dict:
                spamprob=spam_dict[word]
            if word in Nonspam_dict:
                nonspamprob=Nonspam_dict[word]


            spamscore=spamscore*(spamprob/(spamprob+nonspamprob))
            nonspamscore=nonspamscore*(nonspamprob/(spamprob+nonspamprob))

        if spamscore>nonspamscore:
            id=0
        else:
            id=1
        if id==int(lines[l][-2]):
            accuracy+=1
    fold+=1
    print(accuracy/len(randarr[k]),'fold number :',fold)
    acuarr.append(accuracy/len(randarr[k]))

print(sum(acuarr)/7,'final acuuracy')




