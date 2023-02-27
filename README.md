---
title: "Novel Crawler"
disqus: hackmd
---

# Novel Crawler

## Table of Contents

[TOC]

## Introduction

在網路上看小說是我在空閒時間最喜歡做的事情之一。但每次在看的時候，不是有時候會點到煩人的廣告，就是不能將字體及背景調到自己喜歡的大小顏色，而且每看一下下就要換下一章。

One of my favorite things to do in my free time is reading novels online. However, every time I read, I either get annoyed by intrusive ads or cannot adjust the font size and background color to my liking. Additionally, I have to switch to the next chapter every time I finish reading a section.

## Main Function

主要是透過爬蟲 Selenium 和 BeautifulSoup 透過 Google Search 這本書在[UU 看書](https://t.uukanshu.com/)上面找有沒有我要看的書。將其載下來之後再將每 50 章製成一個 html 檔，最後將他們的連結放進 index.html。

The main objective is to use a web crawler( Selenium and BeautifulSoup) to search for a specific book on [uukanshu](https://t.uukanshu.com/) and download it. The book will then be divided into HTML files, with each file containing 50 chapters. Finally, the links to these files will be added to the index.html file.

因為將很多章節寫在一起，因此如果在一開始選擇繼續閱讀而不是讀新的書，就會自動跳出 index.html 並找尋著紀錄找出上次所讀的地方。

As multiple chapters are combined into a single file, if the user chooses to continue reading instead of starting a new book, the program will automatically bring up the index.html file and search through the records to find the last read chapter.

## Demonstration

選擇看新的書，會將舊的刪掉。
Choosing to start a new book will delete the old one.
![](https://i.imgur.com/7nLIpFR.png)
selenium 爬到該網站後，將每一章的連結存下來，之後再用 BeautifulSoup，將內容截下來。
After scraping the target website using Selenium, the program saves the links to each chapter, and subsequently uses BeautifulSoup to extract their contents.
![](https://i.imgur.com/g8ASJpn.png)

![](https://i.imgur.com/VfsZevQ.png)
按鈕是 fixed 在網頁上的可以調整字的大小。
The button is fixed on the webpage and allows for adjusting the font size.
![](https://i.imgur.com/C3aiXGl.png)

###### tags: `crawler` `selenium`
