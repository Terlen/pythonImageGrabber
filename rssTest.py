import re, pip
import urllib.request
# Check for feedparser dependency. If missing, offer installation.
try:
    import feedparser
except ModuleNotFoundError:
    print("Feedparser not found.\nWould you like to install Feedparser now? (y/n)")
    if input().lower() == "y":
        pip.main(["install", "feedparser"])
    else:
        exit()

def redditSelect():
    subReddit = input("Please enter the subreddit you want to pull images from: ")
    return subReddit.lower()

def main():
    target = redditSelect()
    awwPics = feedparser.parse('https://www.reddit.com/r/'+target+'/top/.rss?sort=top&t=week')
    # Iterate through each post fetched from RSS
    for x in range(0,len(awwPics.entries)):
    # Dig image links out from RSS feed junk. Only finds JPEG, gif, and Imgur gifv links for now, could expand to other formats later
        awwPicsImage = re.search('https:\/\/i\.redd\.it\/.*\.jpg|https:\/\/i\.redd\.it\/.*\.gif|https:\/\/i\.imgur\.com\/.*\.gifv', awwPics.entries[x].content[0].value)
        try:
            print(awwPicsImage.group(0))
    # Split filename from image link
            file = awwPicsImage.group(0).rsplit('/')[-1]
    # Special case for .gifv files. Redirect to .gif download link instead of direct link.
            if (file.rsplit('.')[-1] == 'gifv'):
                gifvURL = 'https://imgur.com/download/'+file.rsplit('.')[-2]
                print(gifvURL)
                try:
                    urllib.request.urlretrieve(gifvURL, file.rsplit('v')[-2])
                except urllib.error.URLError as e:
                    print("Download error: ",e.reason)
                    continue
            else:
                try:
                    urllib.request.urlretrieve(awwPicsImage.group(0), file)
                except urllib.error.URLError as e:
                    print("Download error: ",e.reason)
                    continue
            print('Downloaded!')
        except AttributeError:
            continue
# Main function call
if __name__ == "__main__":
    main()
