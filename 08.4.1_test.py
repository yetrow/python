def shows(message,sent_message):
    for i in message:
        print(i)
    while message:
        currents=message.pop()
        sent_message.append(currents)
message=['hello','how are you']
sent_message=[]
#shows(message,sent_message)
#print(sent_message)
#print(message)
#print("----")


shows(message[:],sent_message)#通过[:]实现消息归档
print(message)
print(sent_message)



