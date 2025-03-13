""" num=1
while num<=10:
    num+=1
    print(num) """

question="tell me somthing,i will repeat  back to you:"
question+="\nEnter 'quit' to end of program"
active=True
while True:
    message=input(question)
    if message=='quit':
        break
    else:
        print(message)