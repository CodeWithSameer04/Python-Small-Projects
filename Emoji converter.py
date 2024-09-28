# Import the demoji library
import demoji

# Define two sample texts
text1 = "Aaj Library thi toh pehle hi nikal gay tha mai 🤡"
text2 = "Hello! ☀️ Good morning! Let's have some coffee ☕️"

# Use demoji to find and store any emojis in the texts
meaning1 = demoji.findall(text1)
meaning2 = demoji.findall(text2)

# Print the results
print(meaning1)
print(meaning2)

