import requests
from bs4 import BeautifulSoup
import sys

def equityFutures(ticker):
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
            if ticker.lower() == row[1].lower().replace('\n', '').replace('\t', ''):
                for index, cell in enumerate(row, start=0): 
                    if index <= 7 and index >=1 :
                        completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
                data = data + completeRow + '\n'
        j = j+1
    return head + data
        
def currencyFutures(ticker):
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
            if ticker.lower() == row[1].lower().replace('\n', '').replace('\t', ''):
                for index, cell in enumerate(row, start=0): 
                    if index <= 5 and index >=1 :
                        completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
                data = data + completeRow + '\n'
        j = j+1
    return head + data

def equity(ticker):
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
            if ticker.lower() == row[1].lower().replace('\n', '').replace('\t', ''):
                for index, cell in enumerate(row, start=0): 
                    if index <= 3 and index >=1 :
                        completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
                data = data + completeRow + '\n'
        j = j+1
    return head + data

def commodity(ticker):
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
            if ticker.lower() == row[1].lower().replace('\n', '').replace('\t', ''):
                for index, cell in enumerate(row, start=0): 
                    if index <= 5 and index >=1 :
                        completeRow = completeRow + cell.replace('\n', '').replace('\t', '') + '\t\t'
                data = data + completeRow + '\n'
        j = j+1
    return head + data

def help_me():
    print("\n\n\nEnter 'python3 marginBoi.py <TICKER> <x>' where x can be : \n'com' : Commodity\n'eq' : Equities\n'eqfut' : Equity Futures\n'fxfut' : Currency Futures\nExample : 'python3 marginBoi.py BHEL eqfut'\n\n\n")


arguments = sys.argv[1:]
if len(arguments) < 2 or arguments[0] == '--help':
    help_me()
elif len(arguments) == 2:   
    ticker_input = arguments[0]
    command = arguments[1]
    if command == "com":
        print(commodity(ticker_input))
    elif command == "eq":
        print(equity(ticker_input))
    elif command == "eqfut":
        print(equityFutures(ticker_input))
    elif command == "fxfut":
        print(currencyFutures(ticker_input))

# print(ticker_input)
# print(command)