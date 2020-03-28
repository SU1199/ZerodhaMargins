import requests
from bs4 import BeautifulSoup

def equityFutures():
    j =0
    page = requests.get("https://zerodha.com/margin-calculator/Futures/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", {"class": "data futures"})
    table_rows = table.find_all('tr')
    head = 'Contract\tExpiry\tLot Size\tPrice\tNRML Margin\tNRML Margin Rate \tMWPS\n\n'
    data = ''
    for tr in table_rows:
        if j>=1:
            td = tr.find_all('td')
            row = [i.text for i in td]
            completeRow = ''
            for index, cell in enumerate(row, start=0): 
                if index <= 7 and index >=1 :
                    completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
            data = data + completeRow + '\n'
        j = j+1
    return head + data
        
def currencyFutures():
    j =0
    page = requests.get("https://zerodha.com/margin-calculator/Currency/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table", {"class": "data cds"})[1]
    table_rows = table.find_all('tr')
    head = 'Contract\tExpiry\tLot Size\tPrice\tNRML Margin\n\n'
    data = ''
    for tr in table_rows:
        if j>=1:
            td = tr.find_all('td')
            row = [i.text for i in td]
            completeRow = ''
            for index, cell in enumerate(row, start=0): 
                if index <= 5 and index >=1 :
                    completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
            data = data + completeRow + '\n'
        j = j+1
    return head + data

def equity():
    ticker = ticker+ ':EQ'
    j =0
    page = requests.get("https://zerodha.com/margin-calculator/Equity/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table", {"class": "data equity"})[1]
    table_rows = table.find_all('tr')
    head = 'Scrip\tCNC Multiplier\tMIS Multiplier\n'
    data = ''
    for tr in table_rows:
        if j>=1:
            td = tr.find_all('td')
            row = [i.text for i in td]
            completeRow = ''
            for index, cell in enumerate(row, start=0): 
                if index <= 3 and index >=1 :
                    completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
            data = data + completeRow + '\n'
        j = j+1
    return head + data

def commodity():
    j =0
    page = requests.get("https://zerodha.com/margin-calculator/Commodity/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table", {"class": "data commodity"})[1]
    table_rows = table.find_all('tr')
    head = 'Commodity\tLot Size\tPrice\tNRML Margin\tMIS Margin\n\n'
    data = ''
    for tr in table_rows:
        if j>=1:
            td = tr.find_all('td')
            row = [i.text for i in td]
            completeRow = ''
            for index, cell in enumerate(row, start=0): 
                if index <= 5 and index >=1 :
                    completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
            data = data + completeRow + '\n'
        j = j+1
    return head + data
