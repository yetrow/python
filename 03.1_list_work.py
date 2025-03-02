invite=['tom','jerry','mark']
for i in invite:
    print(f"{invite},一起共进晚餐。")

print("jerry无法赴约。")
invite[1]='nike'
for i in invite:
    print(f"{invite},一起共进晚餐。")
invite.insert(0,'kobe')
invite.insert(2,'jorden')
invite.append('james')
for i in invite:
    print(f"{invite},一起共进晚餐.")
while len(invite)>2:
    delman=invite.pop()
    print(f"{delman},无法邀请你")
for i in invite:
    print(f"{invite},受邀请")