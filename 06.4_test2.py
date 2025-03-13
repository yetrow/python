users={
    'tom':{
        'color':'blue',
        'phone':'apple',
        'location':'west',
    },
    'jerry':{
        'color':'black',
        'phone':'huawei',
        'location':'east',
    }
}
for i,j in users.items():
    print(f"username:{i}")
    things=f"{j['color']} {j['phone']}"
    location=j['location']
    print(f"Things:{things}")
    print(location)