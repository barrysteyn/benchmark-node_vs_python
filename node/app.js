var fs = require('fs')
  , express = require('express')
  , http = require('http');

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(app.router);
});

app.get('/', function(req, res, next) {
    fs.readFile('lorem_ipsum_input.txt', 'utf8', function(err, data) {
        fs.writeFile('lorem_ipsum_output.txt', data, function(err) {
            res.render('index');
        });
    });
});

http.createServer(app).listen(app.get('port'));
