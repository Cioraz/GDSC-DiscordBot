import React from 'react'
import Leftside from '../pages/leftSide'
import { useState } from 'react'
import axios from 'axios'

const addSig = () => {
    const initialValues = {
        sig_name: '',
        head_name: '',
        sig_desc: '',
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

        await axios.post("http://localhost:3000/api/addSig", {
            sig_name: formValues.sig_name,
            sig_head: formValues.sig_head,
            sig_desc: formValues.sig_desc

        })

    }

    const validate = (values) => {
        const errors = {}
        if (!values.sig_name) {
            errors.sig_name = "SIG Name is required!";
        }
        if (!values.sig_head) {
            errors.sig_head = "SIG Head is required!";
        }
        if (!values.sig_desc) {
            errors.sig_desc = "SIG Description is required!";
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
                        New SIG
                    </h2>
                    <div className="flex flex-col py-2">
                        <label htmlFor="sig_name">SIG Name</label>
                        <input
                            type="text"
                            className="border p-2 bg-gray-200 text-black"
                            name="sig_name" value={formValues.sig_name} onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.sig_name}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="sig_desc">SIG Description</label>
                        <textarea
                            className="border p-2 bg-gray-200 text-black"
                            value={formValues.sig_desc} name="sig_desc"
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.sig_desc}</p>
                    <div className="flex flex-col py-2">
                        <label htmlFor="sig_head">SIG Head Name</label>
                        <input
                            type="text"
                            className="border p-2 text-black bg-gray-200"
                            name="sig_head" value={formValues.sig_head}
                            onChange={handleChange}
                        />
                    </div>
                    <p className=' text-red-500'>{formError.sig_head}</p>

                    <button className="border w-full my-5 p-4 bg-black text-white hover:bg-gray-800 rounded">
                        Add SIG!
                    </button>
                </form>
            </div>
        </div>


    )
}

export default addSig