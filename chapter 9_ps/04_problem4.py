word = "lila"

with open("file.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word, "ishika")

with open("file.txt","w") as f:
    f.write(contentnew)