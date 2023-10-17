const mongoose = require('mongoose');

const sigSchema = new mongoose.Schema({
    sig_name: String,
    sig_head: String,
    sig_desc: String,
})

module.exports = mongoose.model('sig', sigSchema);