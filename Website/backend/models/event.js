const mongoose = require('mongoose');

const eventSchema = new mongoose.Schema({
    event_name: String,
    event_description: String,
    event_date: Date,
    event_venue: String,
    event_time: String,
    event_T: Boolean

})

module.exports = mongoose.model('events', eventSchema);