import json
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


def main():
    pages = 20
    data = []

    for pages in range(1, pages + 1):
        url_ = f'https://tradeit.gg/api/v2/inventory/data?gameId=730&offset={pages}&limit=200&sortType=Popularity&searchValue=&minPrice=0&maxPrice=100000&minFloat=0&maxFloat=1&type=6&showTradeLock=true&colors=&fresh=false'
        r = requests.get(url_, headers=headers)
        my_data = r.json()
        items = my_data.get('items')
        print(f"{pages}/20")


    for i in items:
        try:
            data.append(
                {
                    "NAME": i['name'],
                    "Price": str(i['price'])[:-2]+'$',
                    "_ID": i['_id'],
                    "steamInventoryLink": i['steamInventoryLink'],
                    "float": i['floatValue']
                }
            )
        except KeyError:
            pass
    with open('data.json', 'w', encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()