const express = require('express');
const router = express.Router();
const mongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// Mongo connection URL
var mongoUrl = 'mongodb://read:read@ds135800.mlab.com:35800/ubcfeedme';
var postsCollection = 'dc';

var mockTable = {
  "entries": [
    {"key1": "val1", "key2": "val2", "key3": "val3"},
    {"key1": "val3", "key2": "val4", "key3": "val5"}
  ]
};



/* GET api listing. */
router.get('/', (req, res) => {
  res.send('api works')
})

// Get all posts
router.get('/posts', (req, res) => {
  // Connect to mongo server
    mongoClient.connect(mongoUrl, function(err, db) {
    assert.equal(null, err);
    console.log("Connected successfully to mlab server");
    findDocuments(db, function(docs) {
      console.log(docs);
      res.send(docs);
      db.close();
    })
  });
})

// Mongo methods
var findDocuments = function(db, callback) {
  // Get the documents collection
  var collection = db.collection(postsCollection);
  // Find some documents
  collection.find({}).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    // console.log(docs);
    callback(docs);
  });
}

module.exports = router;

