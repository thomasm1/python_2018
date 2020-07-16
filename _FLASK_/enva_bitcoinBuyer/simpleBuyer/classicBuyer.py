# source https://github.com/bjames647/StocksBuyer/blob/master/stocks.py


from bs4 import BeautifulSoup as BS
import urllib.request
import time
from pdb import set_trace as debug

def doRequest(request):
	result = urllib.request.urlopen(request).read()
	soup = BS(result, from_encoding='UTF-8')
	return soup

def getRequest():
	#request = input('Website: ')
	soup = 'http://www.allpennystocks.com/aps_us/hot_nasdaq_stocks.asp'
	return soup

def minePopulation(soup):
	data = []
	soup = soup.findAll("td", {"width":"10%"})

	for blarg in soup:
		data.append(str(blarg.contents))

	counter = 0
	for d in data:
		stringData = data[counter]
		stringData = stringData[2:-2]
		stringData = stringData.replace(',','')
		data[counter] = int(stringData)
		counter += 1
		#print(stringData)
	return data

def minePrice(soup):
	data = []
	tempData = []
	priceData = []
	soup = soup.findAll("td", {"width":"9%"})

	for blarg in soup:
		tempData.append(str(blarg.contents))
	
	i = 0
	for c in tempData:
		sliceTemp = tempData[i]
		tempData[i] = sliceTemp[2:-2]
		if len(tempData[i]) <= 7 and len(tempData[i]) > 0:
			data.append(float(tempData[i]))
		i += 1

	counter = 0
	for d in data:
		if counter < len(data):
			#print(counter)
			priceData.append(data[counter])
			counter += 4
		else:
			break	
	#print(priceData)
	return priceData
def mineHigh(soup):
	data = []
	tempData = []
	highData = []
	soup = soup.findAll("td", {"width":"9%"})

	for blarg in soup:
		tempData.append(str(blarg.contents))
	
	i = 0
	for c in tempData:
		sliceTemp = tempData[i]
		tempData[i] = sliceTemp[2:-2]
		if len(tempData[i]) <= 7 and len(tempData[i]) > 0:
			data.append(float(tempData[i]))
		i += 1

	counter = 1
	for d in data:
		if counter < len(data):
			highData.append(data[counter])
			counter += 4
		else:
			break	
	return highData

def mineLow(soup):
	data = []
	tempData = []
	lowData = []
	soup = soup.findAll("td", {"width":"9%"})

	for blarg in soup:
		tempData.append(str(blarg.contents))
	
	i = 0
	for c in tempData:
		sliceTemp = tempData[i]
		tempData[i] = sliceTemp[2:-2]
		if len(tempData[i]) <= 7 and len(tempData[i]) > 0:
			data.append(float(tempData[i]))
		i += 1

	counter = 2
	for d in data:
		if counter < len(data):
			lowData.append(data[counter])
			counter += 4
		else:
			break	
	return lowData

def mineOpen(soup):
	data = []
	tempData = []
	openData = []
	soup = soup.findAll("td", {"width":"9%"})

	for blarg in soup:
		tempData.append(str(blarg.contents))
	
	i = 0
	for c in tempData:
		sliceTemp = tempData[i]
		tempData[i] = sliceTemp[2:-2]
		if len(tempData[i]) <= 7 and len(tempData[i]) > 0:
			data.append(float(tempData[i]))
		i += 1

	counter = 3
	for d in data:
		if counter < len(data):
			openData.append(data[counter])
			counter += 4
		else:
			break	
	return openData

#def mineChange(soup):

def mineSymbol(soup):
	data = []
	tempData = []
	soup = soup.findAll("a")
	for blarg in soup:
		tempData.append(str(blarg.contents))
	i = 0
	for c in tempData:
		sliceTemp = tempData[i]
		tempData[i] = sliceTemp[2:-2]
		if len(tempData[i]) <= 4 and len(tempData[i]) > 0 and tempData[i].isupper():
			data.append(tempData[i])
		i += 1
	return data

def printAll(symbol, population, price, high, low, openM):
	i = 0
	for s in symbol:
		print(symbol[i] + '     ' + str(population[i]) + '     ' + str(price[i]) + '     ' + str(high[i])
			+ '     ' + str(low[i]) + '     ' + str(openM[i]))
		i += 1

def main():
	while True:
		request = getRequest()
		soup = doRequest(request)
		population = minePopulation(soup)
		symbol = mineSymbol(soup)
		price = minePrice(soup)
		high = mineHigh(soup)
		low = mineLow(soup)
		openM = mineOpen(soup)
		printAll(symbol, population, price, high, low, openM)
		inputVar = input('To run again enter Y. Selection: ')
		if inputVar != 'y' and inputVar != 'Y':
			break

main()