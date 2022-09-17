import string
print('Dictionary as a set of counters')
word='brontosaurus'
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)

print('get(key:default value) return the corresponding value if the key appears in the dictionary ')
dd=dict()
for cc in word:
    dd[cc]=dd.get(cc,0)+1 
print(dd)


print('\n Dictionary and file')
fname=input('Enter the file name:  ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened',fname)
    exit()
df=dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words=line.split()
    for word in words:
        df[word]=df.get(word,0)+1

print(df)
# print(df[:6])  wrong
print('\n sorted dictionary')
x=sorted(df.items())
print(x[:15])

print('\n Sort the dictionary by value')

lst = list()
for key, val in list(df.items()):
    lst.append((val, key))  # flip the tuple


lst=sorted(lst,reverse=True)
#lst.sort(reverse=True)

print(lst[:10])
for key, val in lst[:10]:
    print(key, val)



