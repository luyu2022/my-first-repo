
def calrate(hours,rate):
    pay=hours*rate
    return pay
hours=input('Enter Hours:')
rate=input('Enter rate:')
try:
    fh=float(hours)
    fr=float(rate)
except:
    print('Error,please enter numberic input')
    quit()
X=calrate(fr,fh)
print('Pay:',X)


