import re
import urllib.request
try:
    import feedparser
    main()
except ModuleNotFoundError:
    print("Feedparser not found.\nPlease install Feedparser and execute again.")

def main():
    awwPics = feedparser.parse('https://www.reddit.com/r/aww/top/.rss?sort=top&t=week')
    # Iterate through each post fetched from RSS
    for x in range(0,len(awwPics.entries)):
    # Dig image links out from RSS feed junk. Only finds JPEG links for now, could expand to other formats later
        awwPicsImage = re.search('https:\/\/i\.redd\.it\/.*\.jpg|https:\/\/i\.redd\.it\/.*\.gif|https:\/\/i\.imgur\.com\/.*\.gifv', awwPics.entries[x].content[0].value)
        try:
            print(awwPicsImage.group(0))
    # Split filename from image link
            file = awwPicsImage.group(0).rsplit('/')[-1]
    # Special case for .gifv files. Redirect to .gif download link instead of direct link.
            if (file.rsplit('.')[-1] == 'gifv'):
                gifvURL = 'https://imgur.com/download/'+file.rsplit('.')[-2]
                print(gifvURL)
                urllib.request.urlretrieve(gifvURL, file.rsplit('v')[-2])
            else:
                urllib.request.urlretrieve(awwPicsImage.group(0), file)
            print('Downloaded!')
        except AttributeError:
            continue
