import feedparser
from bottle import route, run, get, request, response
import bottle as b
import json
from datetime import datetime

feed = feedparser.parse("http://www.fifa.com/rss/index.xml")
new_list = []

for item in feed["entries"]:
    new_dict = {}
    title = item['title']
    link = item['link']
    new_dict['title'] = title
    new_dict['link'] = link
    new_list.append(new_dict)

print(new_list)


@route('/')
def index():
    return b.template('RSS.html')


@get('/cookie')
def cookie():
    last_visited = request.get_cookie("last_visited")
    if last_visited:
        my_dict = {
            "last_visited_at": last_visited
        }
        response.set_cookie(name="last_visited",
                            value=str(datetime.now()))
        return "Hello again! You last visited us on {}".format(json.dumps(my_dict["last_visited_at"]))
    else:
        my_dict = {
            "last_visited_at": "now"
        }
        response.set_cookie(name="last_visited",
                            value=str(datetime.now()))
        return "Hello again! You last visited us on {}".format(json.dumps(my_dict["last_visited_at"]))


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