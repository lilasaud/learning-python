f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("the wors twinkle is present in the content")

else:
    print(" the word twinkle is not present in the content")

f.close()