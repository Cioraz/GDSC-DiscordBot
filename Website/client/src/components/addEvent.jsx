// This file contains the form to add a new event to the database
import React from 'react'
import Leftside from '../pages/leftSide'
import { useState } from 'react'
import axios from 'axios'

// This function contains the form to add a new event to the database
const addEvent = () => {
    const initialValues = {
        event_date: '',
        event_venue: '',
        event_T: false,
        event_time: '',
        event_name: '',
        event_description: '',
    }
    // This function handles the changes in the form
    const [formValues, setFormValues] = useState(initialValues)
    const [formError, setFormErrors] = useState({})
    const handleChange = (e) => {
        console.log(e.target)
        const { name, value } = e.target
        setFormValues({
            ...formValues,
            [name]: value
        })

    }

    // This function handles the submission of the form
    const handleSubmit = async (e) => {
        e.preventDefault();
        const errors = validate(formValues);
        setFormErrors(errors);

        if (Object.keys(errors).length === 0) {
            // No errors, so you can submit the form
            formValues.event_name = formValues.event_name.toUpperCase();

            try {
                await axios.post("http://localhost:3000/api/addEvent", {
                    event_date: formValues.event_date,
                    event_time: formValues.event_time,
                    event_description: formValues.event_description,
                    event_venue: formValues.event_venue,
                    event_T: formValues.event_T,
                    event_name: formValues.event_name,
                });

                // Optionally, you can reset the formValues here
                setFormValues(initialValues);
            } catch (error) {
                // Handle the Axios error here, if needed
            }
        }
    };

    const validate = (values) => {
        const errors = {}
        if (!values.event_name) {
            errors.event_name = "Event Name is required!";
        }
        if (!values.event_description) {
            errors.event_description = "Event Description is required!";
        }
        if (!values.event_venue) {
            errors.event_venue = "Event Venue is required!";
        }

        // This is to check if the date and time are valid
        if (!values.event_date || values.event_date < new Date().toISOString().split('T')[0]) {
            errors.event_date = "Event Date is required or incorrect!";
        }
        if (!values.event_time || values.event_time < new Date().toISOString().split('T')[1]) {
            errors.event_time = "Event Time is required or incorrect!";
        }
        return errors
    }


    return (

        <div className="grid grid-cols-1 sm:grid-cols-2">
            <Leftside />
            <div className="bg-[#1490e4] h-screen flex flex-col justify-center">
                <form onSubmit={handleSubmit}

                    className="max-w-[400px] w-full mx-auto backdrop-blur-xl bg-[#1a212a] p-4 text-white rounded shadow-2xl"
                >
                    <h2 className="text-4xl font-bold text-center uppercase py-6">
                        New Event
                    </h2>
                    <div className="flex flex-col py-2">
                        <label htmlFor="event_name">Event Name</label>
                        <input
                            type="text"
                            className="border p-2 text-black"
                            name="event_name" value={formValues.event_name} onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.event_name}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="">Event Description</label>
                        <textarea
                            className="border p-2 text-black"
                            name="event_description"
                            defaultValue={""} value={formValues.event_description}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.event_description}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="">Venue</label>
                        <input
                            type="text"
                            className="border p-2 text-black"
                            name="event_venue" value={formValues.event_venue}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.event_venue}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="start">Date</label>
                        <input
                            type="date"
                            id="start"
                            className="text-black"
                            name="event_date"
                            value={formValues.event_date}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.event_date}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="time">Time</label>
                        <input
                            type="time"
                            id="time"
                            className="text-black "
                            name="event_time"
                            value={formValues.event_time}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.event_time}</p>
                    <div className="flex justify-between py-2">
                        <label htmlFor="">Technical Event</label>
                        <input
                            className="flex"
                            type="checkbox"
                            onChange={
                                () => {
                                    formValues.event_T = !formValues.event_T;
                                    handleChange
                                }
                            }
                        />
                    </div>
                    <button className="border w-full my-5 p-4 bg-black text-white hover:bg-gray-800 rounded">
                        Add Event!
                    </button>
                </form>
            </div>
        </div>


    )
}

export default addEvent