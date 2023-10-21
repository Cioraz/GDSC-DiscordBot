// Initialize Mongoose
const mongoose = require('mongoose');

// Create a schema for events
const userSchema = new mongoose.Schema({
    role: String,
    username: String,
    email: String,
    github: String,
    sig: String,
    year: String,
    branch: String,
    phone: String,
    discord_username: String,
    head: Boolean

})

//  Export the model
module.exports = mongoose.model('users', userSchema);