import feedparser


def getFeed():
    feedUrl = "https://www.cbc.ca/webfeed/rss/rss-canada"
    feed = feedparser.parse(feedUrl)
    posts = feed.entries
    wildfireNews = []

    for post in posts:
        if "wildfire" in post.title or "Wildfire" in post.title:
            temp = dict()
            temp["Title"] = post.title
            temp["Time Published"] = post.published
            temp["Link"] = post.link
            temp["Summary"] = post.summary
            wildfireNews.append(temp)

    return wildfireNews


print(getFeed())
