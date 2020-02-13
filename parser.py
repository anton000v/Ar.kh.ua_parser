#site - https://ar.kh.ua/
from bs4 import BeautifulSoup

def main():
    data = []
    with open("saved_from_site.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        table = soup.find("table", {"id": "TableAddress"})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if cols and cols[2] == 'Дійсний':
                data.append([ele for ele in cols if ele])
        with open('output.txt','w') as o:
            for line in data:
                o.write(line[0] + ' | ' + line[1] + '\n')
        print('Thats all!')

if __name__ == '__main__':
    main()
