from email.quoprimime import body_length
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import re
import requests
import hashlib
import os
import time
import glob
k = PyKeyboard()
m = PyMouse()
bookName = ""
nowChapter = 0
loadedChapter = 0
whetherReadOldOne = ""
finish = False
allChapters = []


def chooseBook():
    global bookName
    global nowChapter
    global whetherReadOldOne
    global loadedChapter
    with open(".\\record.txt", 'r', encoding="utf-8") as f:
        text = f.readlines()
    bookName = text[0][0:-1]
    nowChapter = int(text[1][0:-1])
    loadedChapter = int(text[2])
    whetherReadOldOne = input(f"要繼續讀{bookName}嗎(Y/N)?")


def finding():
    global bookName
    global nowChapter
    global allChapters
    driver.set_window_size(1552, 893)

    driver.get("https://www.google.com")
    query = driver.find_element("name", "q")
    query.send_keys(bookName)
    query.send_keys(" https://www.uukanshu.com/ ")
    query.send_keys(Keys.ENTER)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "rcnt"))
    )
    allQueres = driver.find_element(By.CLASS_NAME, "LC20lb")
    print(allQueres.text)
    allQueres.click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "chapterList"))
    )
    idx = driver.current_url.split("/")[-2]
    print(idx)
    driver.get(f"https://tw.uukanshu.com/b/{idx}/")
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "chapterList"))
    )
    allChapters = driver.find_elements(By.XPATH, "//ul[@id='chapterList']//a")
    allChapters.reverse()
    with open(f"url.txt", "w", encoding="utf-8") as f:
        for i in allChapters:
            f.write(f"{i}\n")
    print(len(allChapters))


def getInnerHtml(index):
    global allChapters
    url = str(allChapters[index].get_attribute("href"))
    print(url)
    html = requests.get(url)
    html.encoding = "utf-8"
    sp = BeautifulSoup(html.text, "html.parser")
    contentTags = sp.select("#contentbox")
    return str(contentTags[0])


def makeNewHtml(body, front, back):
    global loadedChapter
    bodyofIndex = ""
    head = f'''<!DOCTYPE html>
    <html lang="ch-hang-tw">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="index.css" />
        <title>{front}-{back}</title>
    </head>
    <body id = "body">
        <button id="add_size">+</button>
        <button id="sub_size">-</button>
        <h1>{front}-{back}</h1>
        '''
    tail = '''   <script src="index.js"></script>
        </body>
    </html>
    '''
    with open(f"{front}-{back}.html", "w", encoding="utf-8") as f:
        f.write(head+body+tail)
    head = f'''<!DOCTYPE html>
    <html lang="ch-hang-tw">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="index.css" />
        <title>{bookName}</title>
    </head>
    <body>
        <h1>{bookName}</h1>
        <ul>
        '''
    tail = '''   <script src="index.js"></script>
            </ul>
        </body>
    </html>
    '''
    for rec in range(1, back-1, 50):
        if(rec == front):
            continue
        bodyofIndex = bodyofIndex + \
            f'<li><a href = "{rec}-{rec+49}.html">{rec}-{rec+49}</li>'
    appList = f'<li><a href = "{front}-{back}.html">{front}-{back}</li>'
    bodyofIndex = bodyofIndex + appList
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(head+bodyofIndex+tail)


def loading(start):
    global bookName
    global nowChapter
    global loadedChapter
    global finish
    global allChapters
    prevUrl = "0"
    nowUrl = "1"

    body = ""
    finding()
    """ while prevUrl != nowUrl: """
    size = len(allChapters)
    for i in range(start, size):
        nowUrl = driver.current_url
        body = body + f"<p> 第{i+1}章 </p>" + getInnerHtml(i)
        loadedChapter += 1
        if i % 50 == 49:
            makeNewHtml(body, i-48, i+1)
            body = ""
            print(f"已載完{i+1}章")
            with open("record.txt", 'w', encoding="utf-8") as f:
                f.write(f"{bookName}\n{nowChapter}\n{loadedChapter}")
    makeNewHtml(body, loadedChapter-(loadedChapter % 50)+1, loadedChapter)
    body = ""
    print(f"已載完{i+1}章")
    with open("record.txt", 'w', encoding="utf-8") as f:
        f.write(f"{bookName}\n{nowChapter}\n{loadedChapter}")


# main

chooseBook()
driver = webdriver.Edge(executable_path="D:\\edgedriver\\msedgedriver")
if(whetherReadOldOne.lower() == "n"):
    bookName = input("請輸入小說名稱:")
    loadedChapter = 0
    nowChapter = 1
    for file in glob.glob("*.html"):
        os.remove(file)
        print("Deleted " + str(file))
    loading(0)
else:
    with open("url.txt", 'r', encoding="utf-8") as f:
        text = f.readlines()
        for i in range(len(text)):
            allChapters.append(text[i][0:-1])
    if loadedChapter < len(allChapters):
        print("繼續下載")
        loading(loadedChapter)
    else:
        driver.get("C:/Users/user/Desktop/Codes/Python/getFreeBook/index.html")
        driver.maximize_window()
        books = driver.find_elements(By.TAG_NAME, "a")
        time.sleep(2)
        print(books[int((nowChapter-1) / 50)].text)
        books[int((nowChapter-1) / 50)].click()
        k.press_key(k.control_key)
        k.tap_key("f")
        k.release_key(k.control_key)
        time.sleep(1)
        k.type_string("1")
        m.click(1749, 1056)
        time.sleep(2)
        k.type_string(str(nowChapter))

        with open("record.txt", 'w', encoding="utf-8") as f:
            nowChapter = input("看到第幾章?")
            f.write(f"{bookName}\n{nowChapter}\n{loadedChapter}")
time.sleep(1)
driver.quit()
