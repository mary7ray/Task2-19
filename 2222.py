import requests
from bs4 import BeautifulSoup


# План:
# 1. Выяснить кол-во страниц
# 2.Сформировать список урлов на страницы выдачи
# 3.Собрать данные

def get_harley_davidson(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, "lxml")

    pages = soup.find("div", class_="pagination-pages").find_all("a")[-1].get("href")

def main():
    pass
    # https: // www.avito.ru / sankt - peterburg / mototsikly_i_mototehnika / mototsikly?p = 1 & q = harley + davidson


if __name__ == "__main__":
    main()