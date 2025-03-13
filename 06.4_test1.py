favorite_language={
    'tom':['python','c++'],
    'jerry':['rust','c'],
    'james':['java','shell']
}
for name,languages in favorite_language.items():
    print(f"{name}喜欢的编程语言是:")
    for language in languages:
        print(f"{language}")

for name in favorite_language.keys():
    print(f"{name} love:")
    for languages in favorite_language.values():
        print(f"{languages}")