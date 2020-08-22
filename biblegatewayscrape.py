import html
import logging
import re
#from http.client import HTTPConnection
import requests
#import aiohttp
from bs4 import BeautifulSoup

import bibleutils

def get_result(query, version, headings, verse_numbers):
    query = query.replace("|", " ")

    url = f"https://www.biblegateway.com/passage/?search={query}&version={version}&interface=print"
    print(url)

    resp = requests.get(url)
    print(resp)
    if resp is not None:
        soup = BeautifulSoup(resp.text, "lxml")
        soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))

        for div in soup.find_all("div", {"class": "result-text-style-normal"}):
            text = ""
            title = ""

            if headings == "disable":
                for heading in div.find_all("h3"):
                    heading.decompose()

                for heading in div.find_all(True, {"class": "inline-h3"}):
                    heading.decompose()
            else:
                for heading in div.find_all("h3"):
                    title += f"{heading.get_text()} / "

            for inline in div.find_all(True, {"class": "inline-h3"}):
                inline.decompose()

            for footnote in div.find_all(True, {"class": "footnotes"}):
                footnote.decompose()

            if verse_numbers == "disable":
                for num in div.find_all(True, {"class": ["chapternum", "versenum"]}):  # noqa: E501
                    num.replace_with(" ")
            else:
                # turn chapter numbers into "1" otherwise the verse numbers
                # look strange
                for num in div.find_all(True, {"class": "chapternum"}):
                    num.replace_with("<**1**> ")

                for num in div.find_all(True, {"class": "versenum"}):
                    num.replace_with(f"<**{num.text[0:-1]}**> ")

            for meta in div.find_all(True, {"class": ["crossreference", "footnote"]}):  # noqa: E501
                meta.decompose()

            for paragraph in div.find_all("p"):
                text += paragraph.get_text()

            print(text)

            verse_object = {
                "passage": div.find(True, {"class": "passage-display-bcv"}).string,  # noqa: E501
                "version": div.find(True, {"class": "passage-display-version"}).string,  # noqa: E501
                "title": title[0:-3],
                "text": bibleutils.purify_text(text)
            }

            return verse_object


thistext = get_result('Mark 2:8-15', 'NRSV', 'enable', 'enable')

print(thistext)
