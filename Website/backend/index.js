const express = require('express');
const app = express();
app.use(express.json())
const cors = require('cors');
app.use(cors());
require('./database/connection');

const events = require('./models/event')
const users = require('./models/users')
const sigs = require('./models/sig')

app.post('/api/addEvent', async (req, res) => {
    let event = new events(req.body);
    let result = await event.save();
});

app.post('/api/addUser', async (req, res) => {
    let user = new users(req.body);
    let result = await user.save();
    res.send(result)
});

app.post('/api/addSig', async (req, res) => {
    let user = new sigs(req.body);
    let result = await user.save();
    res.send(result)
});

app.listen(3000, () => {
    console.log('Example app listening on port 3000!');
});