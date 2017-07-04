import re
import feedparser
awwPics = feedparser.parse('https://www.reddit.com/r/aww/top/.rss?sort=top&t=week')
for x in range(0,len(awwPics.entries)):
    awwPicsImage = re.search('https:\/\/i\.redd\.it\/.*\.jpg', awwPics.entries[x].content[0].value)
    try:
        print(awwPicsImage.group(0))
    except AttributeError:
        continue

