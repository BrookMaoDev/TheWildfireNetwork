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
# Possible parameters:
    # canada
    # britishcolumbia
    # kamloops
    # calgary
    # edmonton
    # saskatchewan
    # saskatoon
    # manitoba
    # thunderbay
    # sudbury
    # windsor
    # london
    # kitchenerwaterloo
    # toronto
    # hamiltonnews
    # montreal
    # newbrunswick
    # pei
    # novascotia
    # newfoundland
    # north
    # ottawa
# Return: full RSS feed link
def determineUrl(location):
    if location == "canada":
        return "https://www.cbc.ca/webfeed/rss/rss-canada"
    return "https://www.cbc.ca/webfeed/rss/rss-canada-" + location
