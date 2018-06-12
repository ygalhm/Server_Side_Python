import feedparser
from bottle import route, run, get
import bottle as b
import json

feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
new_list = []
counter = 0

for item in range(len(feed)):
    title = feed["entries"][item]["title"]
    new_list.append(title)

print(new_list)


@route('/')
def index():
    return b.template('RSS.html')


@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')


@get('/rss')
def rss():
    return json.dumps(new_list)


def main():
    run(host='localhost', port=7001)


if __name__ == '__main__':
    main()