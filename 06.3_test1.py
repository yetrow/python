informations={
    'firstname':'tom',
    'lastname':'james',
    'age':15,
    'city':'london',
}
print(informations)
for i,j in informations.items():
    print(f"首项是{i},尾项是{j}")
for i in informations.keys():
    print(i.title())
