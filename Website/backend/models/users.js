const mongoose = require('mongoose');

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

module.exports = mongoose.model('users', userSchema);