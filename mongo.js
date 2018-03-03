/**
 * Created by karthik on 7/14/17.
 */
var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var bodyParser = require("body-parser");
var express = require('express');
var cors = require('cors');
var app = express();

var url='mongodb://Shalin:12345@ds161049.mlab.com:61049/asetutorial10';//1.Modify this url with the credentials of your db name and password.
var ObjectID = require('mongodb').ObjectID;

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.post('/create', function (req, res) {
    MongoClient.connect(url, function(err, db) {
        if(err)
        {
            res.write("Failed, Error while connecting to Database");
            res.end();
        }
        insertDocument(db, req.body, function() {
            res.write("Successfully inserted");
            res.end();
        });
    });
});

app.get('/get', function (req, res) {
    MongoClient.connect(url, function(err, db) {
        if(err)
        {
            res.write("Failed, Error while connecting to Database");
            res.end();
        }

        db.collection('books').find().toArray(function(err, result){
            if(err)
            {
                res.write("get Failed");
                res.end();
            }else
            {

                res.send(JSON.stringify(result));
            }
            console.log("Got All Documents");

        });
    });

});

app.get('/delete/:toBeDeleted_id', function (req, res) {
    MongoClient.connect(url, function(err, db) {
        if (err) {
            res.write("Failed, Error while connecting to Database");
            res.end();
        }
        console.log(req.url.split('/')[2]);
        db.collection('books').deleteOne({'ISBN': req.url.split('/')[2]});
    });
});


app.get('/update/:toBeUpdated_id', function (req, res) {
    MongoClient.connect(url, function(err, db) {
        if (err) {
            res.write("Failed, Error while connecting to Database");
            res.end();
        }
        console.log(req);
        db.collection('books').update({'ISBN':req.query.ISBN},{$set:{'authorName':req.query.authorName,'bookName':req.query.bookName,'ISBN':req.query.ISBN}}, function (err, result) {
            if(err)
            {
                res.write("failed to update");
                res.end();
            }
            if(result!=null)
            {
                z=req.body.email;
                res.send("successfully updated");
                res.end();
            }
            console.log(result);
        })
    });
});


var insertDocument = function(db, data, callback) {
    db.collection('books').insertOne( data, function(err, result) {
        if(err)
        {
            res.write("Registration Failed, Error While Registering");
            res.end();
        }
        console.log("Inserted a document into the books collection.");
        callback();
    });
};

var server = app.listen(8081, function () {
    var host = server.address().address;
    var port = server.address().port;

    console.log("Example app listening at http://%s:%s", host, port)
});