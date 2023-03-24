import requests
import html
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from os import listdir
from os.path import isfile, join
import csv
import time

def get_links_from_url(url,base_url, links):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        extract_links(soup, base_url,links)

    else:
        print(f"Error: {response.status_code}")
        return None

def extract_links(soup, base_url,links):
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            full_url = urljoin(base_url, href)
            links.append([full_url])
    return links              

# This script find all the links on a web page an store them to a csv finle called urls_new.csv

def main():
    sitemaps = input("Enter the urls of the sitemaps page : ");
    base_url = input("Enter the urls of the base url : ");
    links =[];

    get_links_from_url(sitemaps,base_url,links);

    with open("urls_new.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in links:
            writer.writerow(row)  
if __name__ == '__main__':
    main()


