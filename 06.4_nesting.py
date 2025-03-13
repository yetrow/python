""" alien0={'color':'green','speed':'fast'}
alien1={'color':'white','speed':'medium'}
alien2={'color':'bluek','speed':'slow'}
alien=[alien0,alien1,alien2]
print(alien) """

alien=[]
for  i in range(10):
    alien1={'color':'blue','speed':'fast','points':'5'}
    alien.append(alien1)
for i in alien[:3]:
    print(i)
print(".......")