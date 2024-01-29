!pip install python-Levenshtein
from nltk.corpus import wordnet as wn
import pandas as pd

count = 0
for w in wn.words():
  count=count+1

correct_spellings = []
incorrect_spellings = []
file_ = open('brikbeck.txt', 'r')
Lines = file_.readlines()
l=[]


for current_line_number, line in enumerate(Lines, start=1):
    if '$' in line:
        crr_spell = line.replace('$', '').replace('\n', '').lower()
        correct_spellings.append(crr_spell)
        l.append(current_line_number+1)
        
for i in l:
    a=(Lines[i-1])
    incrr_spell = a.replace('\n', '').lower()
    incorrect_spellings.append(incrr_spell)

data = {
  "incorrect": incorrect_spellings,
  "correct": correct_spellings
}

df = pd.DataFrame(data)


from Levenshtein import distance as lev
x=incorrect_spellings[0:500]
y=correct_spellings[0:500]
s1=0
s5=0
s10=0

d=dict()
for i in range(0,len(x)):
    for w in wn.words():
        d[w]=lev(x[i],w)

    res = {key: val for key, val in sorted(d.items(), key = lambda ele: ele[1])}
    first_pair = {k: res[k] for k in list(res)[:1]}
    first5pairs = {k: res[k] for k in list(res)[:5]}
    first10pairs = {k: res[k] for k in list(res)[:10]}
   
    if y[i] in list(first_pair.keys()):
        s1=s1+1
    if y[i] in list(first5pairs.keys()):
        s5=s5+1

    if y[i] in list(first10pairs.keys()):
        s10=s10+1
    

    
print('Total of S@1',s1)
print('Total of S@5',s5)
print('Total of S@10',s10)

#calculating averages of all success at k s@k k=[1,5,10]

print('Average of s@1',s1/500)
print('Average of s@5',s5/500)
print('Average of s@10',s10/500)
