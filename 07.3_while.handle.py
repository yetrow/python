users={'alicec','brain','candace'}
confirmed_users=[]
while users:
    current_user=users.pop()
    print(f"verifying user:{current_user}")
    confirmed_users.append(current_user)
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("--------")

while 'brain' in confirmed_users:
    #del confirmed_users[confirmed_users.index('brain')]
    confirmed_users.remove('brain')
print(confirmed_users)