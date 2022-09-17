def Compute(score):


  if score<0.0 or score>1.0:
    print('Bad score')
    quit()
  if score>=0.9:
    print('A')
  elif score>=0.8:
    print('B')
  elif score>=0.7:
    print('C')
  elif score>=0.6:
    print('D')
  elif score<0.6:
    print('F')


score=input('Enter a score:')
try:
    fscore=float(score)
except:
    print('Bad score')
    quit()
Compute(fscore)