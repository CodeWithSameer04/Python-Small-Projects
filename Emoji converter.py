import demoji

text1 = "Aaj Library thi toh pehle hi nikal gay tha mai 🤡"

text2 = "Hello! ☀️ Good morning! Let's have some coffee ☕️"
meaning1 = demoji.findall(text1)

meaning2 = demoji.findall(text2)

print(meaning1)
print(meaning2)
