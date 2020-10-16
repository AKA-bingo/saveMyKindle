import os
import sys
import csv
import operator
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.exists("book.csv"):
    os.remove("book.csv")

try:
    execute(
        [
            'scrapy',
            'crawl',
            '--nolog',
            'sqsxs',
            '-o',
            'book.csv',
        ],
    )
except SystemExit:
    pass

reader = csv.reader(open("book.csv"), delimiter=",")

sortedlist = sorted(reader, key=operator.itemgetter(2), reverse=False)

txtBook = open('book.txt', 'w+')

for chapterContent, chapterName, chapterUrl in sortedlist[1:]:
    title = "## " + chapterName
    content = chapterContent.replace('\xa0\xa0\xa0\xa0', '\r\n')
    txtBook.write(title)
    txtBook.write(content)
    txtBook.write('\r\n')

txtBook.close()