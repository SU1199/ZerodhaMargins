# Zerodha Margins Reporting Script

Python script to get latest margins on equities, commodities and currencies. Works from terminal and can be added to any project as a module. 

## Installation

Use gitclone to clone this repository to your local machine.

```bash
git clone https://github.com/SU1199/ZerodhaMargins
```
Install required packages (bs4,requests) 

```bash
sudo pip3 install -r requirements.txt
```

## Usage

### From Terminal -

``` 
Enter 'python3 marginBoi.py <TICKER> <x>' where x can be : 
'com' : Commodity
'eq' : Equities
'eqfut' : Equity Futures
'fxfut' : Currency Futures
```
Example : 

```bash
python3 marginBoi.py BHEL eqfut
python3 marginBoi.py RELIANCE eq
python3 marginBoi.py USDINR fxfut
python3 marginBoi.py GOLD com

```
[Video Example](https://youtu.be/eEXN8oTGDi8)

### As an add-on to an existing project 
- Copy marginBoi.py file from forImport folder to your project folder.
- Import the file.
- Get the data using -

```python
#Import the file
import marginBoi

#for commodity
marginBoi.commodity("TICKER")

#for equities
marginBoi.equity("TICKER")

#for equity futures
marginBoi.equityFutures("TICKER")

#for currency futures
marginBoi.currencyFutures("TICKER")
```
#### To get data for every ticker available use bulkBoi.py -
```python
#Import the file
import bulkBoi

#for commodity
bulkBoi.commodity()

#for equities
bulkBoi.equity()

#for equity futures
bulkBoi.equityFutures()

#for currency futures
bulkBoi.currencyFutures()
```


## License
[MIT](https://choosealicense.com/licenses/mit/)