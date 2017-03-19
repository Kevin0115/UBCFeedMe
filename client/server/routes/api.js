const express = require('express');
const router = express.Router();

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
  res.send(mockTable)
})

module.exports = router;
