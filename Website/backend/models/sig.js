// Initialize mongoose
const mongoose = require('mongoose');

// Create a schema for events
const sigSchema = new mongoose.Schema({
    sig_name: String,
    sig_head: String,
    sig_desc: String,
})

//  Export the model
module.exports = mongoose.model('sig', sigSchema);