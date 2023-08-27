import feedparser


def getFeed(location):
    feedUrl = determineUrl(location)
    feed = feedparser.parse(feedUrl)
    posts = feed.entries
    wildfireNews = []

    x=0
    for post in posts:
        if "wildfire" in post.title.lower():
            x+=1
            temp = dict()
            temp["Title"] = post.title
            temp["TimePublished"] = post.published
            temp["Link"] = post.link
            temp["Image"] = getImage(post.summary)
            wildfireNews.append(temp)
        if x >= 3:
            break

    return wildfireNews


def getImage(summaryLink):
    startIndex = summaryLink.index('src="')
    slice1 = summaryLink[startIndex + 5 :]
    startIndex = slice1.index('"')
    slice2 = slice1[:startIndex]
    return slice2


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
