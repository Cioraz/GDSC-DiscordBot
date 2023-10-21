// Initialize Mongoose
const mongoose = require('mongoose');

// Create a schema for events
const eventSchema = new mongoose.Schema({
    event_name: String,
    event_description: String,
    event_date: Date,
    event_venue: String,
    event_time: String,
    event_T: Boolean

})

// Export the model
module.exports = mongoose.model('events', eventSchema);