var axios = require('axios');//promise-based http requests component

/*Github requires a client id after a certain number of queries -- might need this to make it work and bypass rate limiting.
var id = 'CLIENT_ID';
var sec = 'CLIENT_SECRET';
var params = '?client_id=' + id + '&client_secret=' + sec;*/


module.exports = {
	fetchPopularRepos: function(dataset){
		//var encodedURI = window.encodeURI('https://react.quantigy.com/scripts/portfolio_test.php?dataset=' + dataset);
		var encodedURI = window.encodeURI('../../data/' + dataset); //Currently passed a file name for testing. Will change to scripts url with param(s)

		return axios.get(encodedURI)
		.then(function (response){
			return response.data.items;//items is the wrapper in the JSON file
		});
	}
}