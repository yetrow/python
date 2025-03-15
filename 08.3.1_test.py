def information(artist,album,num=None):
    in_dict={
        'artist':artist,
        'album':album,
    }
    if num:
        in_dict['num']=num
    return in_dict
num1=information('tom','hi')
num2=information('james','ba',9)
print(num1)
print(num2)

#通过while循环打印
while True:
    artist=input("artist is ")
    if artist =='q':
        break
    album=input("album is ")
    if album=='q':
        break
    num=input("num is ")
    if num=='q':
        break
    if num:
        info=information(artist,album,int(num))
    else:
        info=information(artist,album)
    print(info)
print("thanks")