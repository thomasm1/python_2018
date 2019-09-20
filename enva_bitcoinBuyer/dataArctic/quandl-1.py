from arctic import Arctic
import quandl

# Connect to Local MONGODB
store = Arctic('localhost')

# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')

# Access the library
library = store['NASDAQ']

# Load some data - maybe from Quandl
aapl = quandl.get("WIKI/AAPL", authtoken="EeF1-zUnuqQ3kU-xxxxx")

# Store the data in the library
library.write('AAPL', aapl, metadata={'source': 'Quandl'})

# Reading the data
item = library.read('AAPL')
aapl = item.data
metadata = item.metadata
