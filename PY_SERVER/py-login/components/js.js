http = require('http');
fs = require('fs');

  console.log('Popular Login');
  
  const hostname = '127.0.0.1';
  const port = 3001;

 fs.readFile('index.html', (err, html) => {
  if(err){
 		throw err;
 		}
  const server = http.createServer((req, res) => {
  	res.statusCode = 200;
  	res.setHeader('Content-type', 'text/plain');
  	res.write(html);
  	res.end('Carbon Creek');
  });
  server.listen(port, hostname, () => {
  	console.log('Server starto on port '+ port);
 });
});