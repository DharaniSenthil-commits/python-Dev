sentence = "This is a common interview questions"
char_frequency = {}
for i in sentence.lower():
    if i == " ":
        continue
    if i in char_frequency:
        char_frequency[i] = char_frequency[i]+1
    else:
        char_frequency[i] = 1

print(char_frequency)
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])
