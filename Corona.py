import requests
from bs4 import BeautifulSoup

page = requests.get("http://corona.gov.bd/")

if page.status_code == 200:
    print("Request Success")
    # print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    division = soup.find_all('div', attrs={'class': 'statistic'})
    for items in division:
        lists = items.find_all('li')

        data2 = items.find_all('span')
        for key, d in enumerate(data2):
            if key == 2 or key == 5 or key == 8:
                print(d.get_text())

        # print(lists[11].find('strong'))
        for li in lists:
            data = li.find('strong')
            if data is not None:
                print(data.get_text().strip())

else:
    print("Request Failed")
