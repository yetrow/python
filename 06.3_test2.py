favorite_language={
    'jen':'python',
    'tom':'c',
    'jerry':'rust',
    'nike':'c++',
}

friends=['jen','nike']

for name in favorite_language.keys():
    print(f"Hi,{name.title()}")
    if name in friends:
        language=favorite_language[name].title()
        print(f"{name},you love {language}")

print("--------------")
for language in favorite_language.values():#通过values()访问键值
    print(language)