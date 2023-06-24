#"""Count the frequency of each word in a text."""

text = """\
You'll see output showing the number of times each word appears in the text. Word splitting works in
the same way as before, but now, each time a word is examined, the program checks to find out whether the word has
appeared before. If it has not, then a new entry is made in the dict with a value of one. If it has (if it is already found in the
freq dict), the current count is incremented."""

for punc in "(),?;.":
    text = text.replace(punc, "")
freq = {}
for word in text.lower().split():
    freq[word] = freq.get(word, 0)+1
for word in sorted(freq.keys()):
    print(word, freq[word])