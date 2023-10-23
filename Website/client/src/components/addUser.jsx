// This page is used to add a new user to the database
import React from 'react'
import Leftside from '../pages/leftSide'
import { useState } from 'react'
import axios from 'axios'

// This function contains the form to add a new user to the database
const addUser = () => {

    const initialValues = {
        role: '',
        username: '',
        email: '',
        github: '',
        sig: '',
        year: '',
        branch: '',
        phone: '',
        discord_username: '',
        head: false
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
    const handleSubmit = async (e) => {
        e.preventDefault();
        const errors = validate(formValues);
        setFormErrors(errors);

        if (Object.keys(errors).length === 0) {
            // No errors, so you can submit the form
            formValues.username = formValues.username.toUpperCase();

            try {
                await axios.post("http://localhost:3000/api/addUser", {
                    username: formValues.username,
                    email: formValues.email,
                    github: formValues.github,
                    phone: formValues.phone,
                    discord_username: formValues.discord_username,
                    role: formValues.role,
                    sig: formValues.sig,
                    year: formValues.year,
                    branch: formValues.branch,
                    head: formValues.head,
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
        if (!values.username) {
            errors.username = "Name is required!";
        }
        if (!values.email) {
            errors.email = "Email is required!";
        }
        if (!values.github) {
            errors.github = "Github ID is required!";
        }
        if (!values.phone) {
            errors.phone = "Phone number is required!";
        }
        if (!values.discord_username) {
            errors.discord_username = "Discord Username is required!";
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
                        New Member
                    </h2>
                    <div className="flex flex-col py-1">
                        <label htmlFor="username">Name</label>
                        <input
                            type="text"
                            className="border p-2 bg-gray-200 text-black"
                            name="username" value={formValues.username} onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.username}</p>
                    <div className="flex flex-col py-1">
                        <label htmlFor="email">Email</label>
                        <input
                            type="email"
                            className="border p-2 bg-gray-200 text-black"
                            name="email" value={formValues.email} onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.email}</p>
                    <div className="flex flex-col py-1">
                        <label htmlFor="github">Github ID</label>
                        <input
                            type="text"
                            className="border p-2 text-black bg-gray-200"
                            name="github" value={formValues.github}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.github}</p>
                    <div className="flex flex-col py-1">
                        <label htmlFor="phone">Phone</label>
                        <input
                            className="flex border p-2 bg-gray-200 text-black"
                            type="text"
                            name="phone"
                            value={formValues.phone}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.phone}</p>
                    <div className="flex flex-col py-1">
                        <label htmlFor="discord_username">Discord Username</label>
                        <input
                            className="flex border p-2 bg-gray-200 text-black"
                            type="text"
                            name="discord_username"
                            value={formValues.discord_username}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.discord_username}</p>
                    <div className="flex justify-between py-2">
                        <label htmlFor="role">Role</label>
                        <select className='flex text-black' onChange={
                            (e) => {
                                formValues.role = e.target.value;
                                handleChange
                            }
                        }>
                            <option value="-">-</option>
                            <option value="M">Member</option>
                            <option value="EM">Executive Member</option>
                        </select>
                    </div>
                    <div className="flex justify-between py-2">
                        <label htmlFor="start">SIG</label>
                        <select className="flex text-black"
                            onChange={
                                (e) => {
                                    formValues.sig = e.target.value;
                                    handleChange
                                }
                            }>
                            <option value="-">-</option>
                            <option value="INTELLIGENCE">Intelligence</option>
                            <option value="DEV">Development</option>
                            <option value="ALGO">Algorithms</option>
                            <option value="SYSTEMS">Systems</option>
                        </select>
                    </div>
                    <div className="flex justify-between py-2">
                        <label htmlFor="time ">Year</label>
                        <select className="flex text-black"
                            onChange={
                                (e) => {
                                    formValues.year = e.target.value;
                                    handleChange
                                }
                            }>
                            <option value="-">-</option>
                            <option value="2B">2nd Year </option>
                            <option value="3B">3rd Year</option>
                            <option value="1MCA">1st MCA</option>
                        </select>
                    </div>
                    <div className="flex justify-between py-1">
                        <label htmlFor="">Branch</label>
                        <select className="flex text-black"
                            onChange={
                                (e) => {
                                    formValues.branch = e.target.value;
                                    handleChange
                                }
                            }>
                            <option value="-">-</option>
                            <option value="CSE">CSE</option>
                            <option value="CHEM">CHEM</option>
                            <option value="MECH">MECH</option>
                            <option value="CIVIL">CIVIL</option>
                            <option value="IT">IT</option>
                            <option value="EEE">EEE</option>
                            <option value="ECE">ECE</option>
                        </select>
                    </div>

                    <div className="flex justify-between py-1 text-white">
                        <label htmlFor="">Head</label>
                        <input
                            className="flex"
                            type="checkbox"
                            onChange={
                                () => {
                                    formValues.head = !formValues.head;
                                    handleChange
                                }
                            }
                        />
                    </div>
                    <button className="border w-full my-5 p-4 bg-black text-white hover:bg-gray-800 rounded">
                        Add User!
                    </button>
                </form>
            </div>
        </div>


    )
}

export default addUser