from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.p) first p tag return

# return all tags
all_tags = soup.find_all(name="a")
print(all_tags)

# href attribute
for tag in all_tags:
    print(tag.get("href"))

# parse element with id
heading = soup.find(name="h1", id="name")

# parse element with class
class_heading = soup.find_all("h3", class_="heading")

# select_one return first element & in selector can use css selector
company_url = soup.select_one(selector="p a")
