from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import base64


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """

    proxies = {
    "http": "http:one.proxy.att.com:8080",
    "https": "https:one.proxy.att.com:8080",
    }

    try:
        #with closing(get(url, stream=True, proxies=proxies)) as resp:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

thestart="""<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet"> 
<style>
h1 h2 body {
    font-family: 'EB Garamond', serif;
}

h3 {
  display: none;
}

div.footnotes {
  display: none;
}

span.chapternum {
    display: none;
}

sup.versenum {
    display: none;
}

sup.footnote {
    display: none;
}

div.publisher-info-bottom-with-single {
    display:none;
}

</style>


</head>

<body>
"""
theend="""</body>
</html>"""

raw_html = simple_get('https://www.biblegateway.com/passage/?search=Amos+1:1-5,1:13-2:8&version=CEV')
#raw_html = open('rawhtml.html', mode="r", encoding="utf-8").read()
html = BeautifulSoup(raw_html, 'html.parser')
#print(html)fi
passages=html.find_all(class_="passage-text")
for li in passages:
     print(type(li))
     #thewebpage=thestart + str(li).replace('publisher-info-bottom with-single','publisher-info-bottom-with-single') + theend
#print(thewebpage)
#print(li.find('span',{"id" : lambda L: L and L.startswith('en')}))
#print(type(li))
#for i, v in enumerate(li.find_all('span',{"class" : lambda L: L and L.startswith('text')})):
#    print(i, v.decode)
     message = str(li)
     message_bytes = message.encode('UTF-8')
     base64_bytes = base64.b64encode(message_bytes)
     base64_message = base64_bytes.decode('UTF-8')
     print(base64_message)
     print(base64.b64decode(base64_message.encode('UTF-8')).decode('UTF-8'))




