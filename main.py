import bs4 as bs
from urllib.request import Request, urlopen
import search
req = Request('https://opensea.io/assets?search[query]=galaxy%20fight%20club', headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
soup = bs.BeautifulSoup(source,'lxml')

# print(soup.title)
url_list_temp = soup.find_all(class_="styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor")
url_list = []
# get attributes:
# print(url_list_temp.__len__())
for i in url_list_temp:
    print("https://opensea.io/"+i['href'])
    url_list.append("https://opensea.io/"+i['href'])
search.search(url_list)

# print(url_list)