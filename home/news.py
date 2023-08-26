import feedparser


def getFeed(location):
    feedUrl = determineUrl(location)
    feed = feedparser.parse(feedUrl)
    posts = feed.entries
    wildfireNews = []

    for post in posts:
        if "wildfire" in post.title.lower():
            temp = dict()
            temp["Title"] = post.title
            temp["Time Published"] = post.published
            temp["Link"] = post.link
            temp["Summary"] = post.summary
            wildfireNews.append(temp)

    return wildfireNews


# Returns RSS feed link for a given location
# Parameter: the end of the string from the regional news list from this site: https://www.cbc.ca/rss/
# Return: full RSS feed link
def determineUrl(location):
    if location == "canada":
        return "https://www.cbc.ca/webfeed/rss/rss-canada"
    return "https://www.cbc.ca/webfeed/rss/rss-canada-" + location
