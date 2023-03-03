---
title: "Novel Crawler"
disqus: hackmd
---

# Novel Crawler

## Table of Contents

[TOC]

## Introduction

在網路上看小說是我在空閒時間最喜歡做的事情之一。但每次在看的時候，不是有時候會點到煩人的廣告，就是不能將字體及背景調到自己喜歡的大小顏色，而且每看一下下就要換下一章。

In my free time, I enjoy reading novels online. However, I find the experience frustrating due to intrusive ads and limited control over font size and background color. Additionally, I have to manually click on the next chapter after finishing a section.

## Main Function

主要是透過爬蟲 Selenium 和 BeautifulSoup 透過 Google Search 這本書在[UU 看書](https://t.uukanshu.com/)上面找有沒有我要看的書。將其載下來之後再將每 50 章製成一個 html 檔，最後將他們的連結放進 index.html。

To overcome these issues, I created a program that uses web crawlers, Selenium and BeautifulSoup, to search for and download specific books from [uukanshu](https://t.uukanshu.com/) as HTML files. Each file contains 50 chapters, and the program adds links to these files to the index.html file.

因為將很多章節寫在一起，因此如果在一開始選擇繼續閱讀而不是讀新的書，就會自動跳出 index.html 並找尋著紀錄找出上次所讀的地方。

Since multiple chapters are combined into a single file, the program automatically brings up the index.html file and searches for the last read chapter if the user chooses to continue reading instead of starting a new book. Starting a new book will delete the old one.

## Demonstration

選擇看新的書，會將舊的刪掉。
Choosing to start a new book will delete the old one.
![](https://i.imgur.com/7nLIpFR.png)
selenium 爬到該網站後，將每一章的連結存下來，之後再用 BeautifulSoup，將內容截下來。
After crawling the target website using Selenium, the program saves links to each chapter and uses BeautifulSoup to extract its contents.
![](https://i.imgur.com/g8ASJpn.png)

![](https://i.imgur.com/VfsZevQ.png)
按鈕是 fixed 在網頁上的可以調整字的大小。
The program also features a fixed button on the webpage that allows users to adjust the font size to their preference.
![](https://i.imgur.com/C3aiXGl.png)

###### tags: `crawler` `selenium`
