import os
import re

txtpath = os.path.join("..", "..", "..", "..", "..", "gitlab", "GWARL201808DATA3", "03-Python", "Homework", "ExtraContent", "Instructions", "PyParagraph", "raw_data", "paragraph_2.txt")

text = open(txtpath, 'r').read()
#print(text)

#words
words = text.split(" ")
numWords = len(words)

#aveerage length for words
#wordLen = (sum(len(word)) for word in words)
wordLen = 0
for word in words:
    wordLen += len(word)
#print(wordLen)
aveWordLen = wordLen / numWords

#sentences
sentences = re.split("(?<=[.!?]) +", text)
numSent = len(sentences)
aveSentLen = numWords / numSent

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {numWords}")
print(f"Approximate Sentence Count: {numSent}")
print(f"Average Letter Count: {aveWordLen}")
print(f"Average Sentence Length: {aveSentLen}")

with open('Writing_Analysis_1.txt', 'w') as filewriter:
    filewriter.write("Paragraph Analysis\n")
    filewriter.write("-----------------\n")
    filewriter.write(f"Approximate Word Count: {numWords}\n")
    filewriter.write(f"Approximate Sentence Count: {numSent}\n")
    filewriter.write(f"Average Letter Count: {aveWordLen}\n")
    filewriter.write(f"Average Sentence Length: {aveSentLen}\n")
