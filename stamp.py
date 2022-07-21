bookName = ""
nowChapter = ""
loadedChapter = ""
with open("record.txt", 'r', encoding="utf-8") as f:
    text = f.readlines()
    bookName = text[0][0:-1]
    nowChapter = text[1][0:-1]
    loadedChapter = text[2]
with open("record.txt", 'w', encoding="utf-8") as f:
    nowChapter = input("看到第幾章?")
    f.write(f"{bookName}\n{nowChapter}\n{loadedChapter}")
