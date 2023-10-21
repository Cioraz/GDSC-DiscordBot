// Importing the required packages and files
const express = require('express');
const app = express();
app.use(express.json())
const cors = require('cors');
app.use(cors());
require('./database/connection');

// Importing the required models
const events = require('./models/event')
const users = require('./models/users')
const sigs = require('./models/sig');
const sendMail = require('./sendMail');


// API Endpoints
app.post('/api/addEvent', async (req, res) => {
    let event = new events(req.body);
    await event.save();
});

app.post('/api/addUser', async (req, res) => {
    let user = new users(req.body);
    email = req.body.email;
    //await sendMail(email);

    await user.save();
});

app.post('/api/addSig', async (req, res) => {
    let user = new sigs(req.body);
    await user.save();
});

app.listen(3000, () => {
    console.log('Listening on port 3000');
});