# import urllib.request

# # Pages not working. Need to find a new page to test this code.
# page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
# # http://beans-r-us.appspot.com/
# # http://beans.itcarlow.ie/
# text = page.read().decode("utf8")
# print(text)

# New version using a text file
from io import open
with open("beansrus.html", "r") as page:
    text = page.read()
    print(text)
