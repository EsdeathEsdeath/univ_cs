import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

def get_total_pages(html):  # return num of pages
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find()
    total_pages
    return int(total_pages)

def main():
    url =
    base_url =
    page_part =
    query_part =
    total_pages = get_total_pages(get_html(url))
    url_gen = base_url + query_part + page_part + str(i)
    # print(url_gen)
    html = get_html(url_gen)
    get_page_data(html)


if __name__ == '__main__':
    main()