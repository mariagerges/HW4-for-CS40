import requests
from bs4 import BeautifulSoup

keyword = 'bike' 
results = []

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'
}

for i in range(1,11):
    r = requests.get ('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i), headers=headers)
    print('r.status_code', r.status_code)

    soup = BeautifulSoup(r.text)

    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes: 
        print ('---')
        result = {}
        titles = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for title in titles:
            print ('title', title.text)
            result['title'] = title.text
        prices  = box.select('.s-item__price')
        for price in prices: 
            print ('price=', price.text)
            result['price'] = price.text 
        statuses = box.select('.SECONDARY_INFO')    
        for status in statuses:
            print ('status=', status.text)
            result ['status'] = status.text     
        print ('result=', result) 
        results.append(result)

    print ('len(results)=', len(results))

    import json 
    j = json.dumps(results)
    with open('items.json','w') as f: 
        f.write(j)