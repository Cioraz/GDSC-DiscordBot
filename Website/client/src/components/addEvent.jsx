import React from 'react'
import Leftside from '../pages/leftSide'
import { useState, useEffect } from 'react'
import axios from 'axios'

const addEvent = () => {
    const initialValues = {
        event_name: '',
        event_description: '',
        event_venue: '',
        event_date: '',
        event_time: '',
        event_t_or_nt: false
    }
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
    const handleSubmit = async (e) => {
        e.preventDefault()
        setFormErrors(validate(formValues))

        axios.post("http://localhost:3000/api/addEvent", {
            event_name: formValues.event_name,
            event_description: formValues.event_description,
            event_venue: formValues.event_venue,
            event_date: formValues.event_date,
            event_time: formValues.event_time,
            event_t_or_nt: formValues.event_t_or_nt,

        })
            .then(res => console.log(res))
            .catch(err => console.log(err))

        //localStorage.setItem("event", JSON.stringify(result))
    }

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
        // handle edge cases when date is before current date and time is before current time on current date
        if (!values.event_date) {
            errors.event_date = "Event Date is required!";
        }
        if (!values.event_time) {
            errors.event_time = "Event Time is required!";
        }
        return errors
    }


    return (

        <div className="grid grid-cols-1 sm:grid-cols-2">
            <Leftside />
            <div className="bg-[#1490e4] h-screen flex flex-col justify-center">
                <form onSubmit={handleSubmit}

                    className="max-w-[400px] w-full mx-auto backdrop-blur-xl bg-white p-4 text-black rounded shadow-2xl"
                >
                    <h2 className="text-4xl font-bold text-center uppercase py-6">
                        New Event
                    </h2>
                    <div className="flex flex-col py-2">
                        <label htmlFor="event_name">Event Name</label>
                        <input
                            type="text"
                            className="border p-2 bg-gray-200"
                            name="event_name" value={formValues.event_name} onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.event_name}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="">Event Description</label>
                        <textarea
                            className="border p-2 bg-gray-200"
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
                            className="border p-2 text-black bg-gray-200"
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
                            className="text-black bg-gray-200"
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
                            className="text-black bg-gray-200"
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
                            name="event_t_or_nt"
                            value={formValues.event_t_or_nt}
                            onChange={handleChange}
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