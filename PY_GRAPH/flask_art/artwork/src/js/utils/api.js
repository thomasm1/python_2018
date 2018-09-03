var axios = require('axios');//promise-based http requests component

/*Github requires a client id after a certain number of queries -- might need this to make it work and bypass rate limiting.
var id = 'CLIENT_ID';
var sec = 'CLIENT_SECRET';
var params = '?client_id=' + id + '&client_secret=' + sec;*/


module.exports = {
	fetchPortfolioList: function(dataset){
		//var encodedURI = window.encodeURI('https://react.quantigy.com/scripts/portfolio_test.php?dataset=' + dataset);
		var encodedURI = window.encodeURI('../../data/' + dataset); //Currently passed a file name for testing. Will change to scripts url with param(s)
		//console.log(dataset)
		return axios.get(encodedURI)
		.then(function (response){
			//console.log(response.data.items);
			return response.data.items;//items is the wrapper in the JSON file
		});
	},
	fetchCustodyDetails: function(dataset){
		//var encodedURI = window.encodeURI('https://react.quantigy.com/scripts/buyerchaincustody.json');
		var encodedURI = window.encodeURI('../../data/buyerchaincustody.json'); //Currently passed a file name for testing. Will change to scripts url with param(s)
		//console.log("dataset in api.js",dataset);
		return axios.get(encodedURI)
		.then(function (response){
			return response.data.items;//items is the wrapper in the JSON file
		});
	},
	fetchGasMakeup: function(dataset){
		//var encodedURI = window.encodeURI('https://react.quantigy.com/scripts/buyerchaincustody.json');
		var encodedURI = window.encodeURI('../../data/buyerchaincustody.json'); //Currently passed a file name for testing. Will change to scripts url with param(s)
		//console.log("dataset in api.js",dataset);
		return axios.get(encodedURI)
		.then(function (response){
			return response.data.gasmakeup;//items is the wrapper in the JSON file
		});
	},	
	sendTransactionData: function(selectedFeedstockUID,selectedTransactionType,selectedTransactionUnits){
		//var encodedURI = window.encodeURI('https://react.quantigy.com/scripts/buyerchaincustody.json');
		var paramString = "selectedFeedstockUID=" + selectedFeedstockUID + "&selectedTransactionType=" + selectedTransactionType + "&selectedTransactionUnits=" + selectedTransactionUnits;
		var encodedURI = window.encodeURI('../../data/buyerchaincustody.json'); //Currently passed a file name for testing. Will change to scripts url with param(s)
		console.log("dataset in api.js",paramString);
		return axios.get(encodedURI)
		.then(function (response){
			return response.data.gasmakeup;//items is the wrapper in the JSON file
		});
	}

}