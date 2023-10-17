import React from 'react'
import Leftside from '../pages/leftSide'
import { useState } from 'react'
import axios from 'axios'

const success = () => {


    return (

        <div className="grid grid-cols-1 sm:grid-cols-2">
            <Leftside />
            <div className="bg-[#1490e4] h-screen flex flex-col justify-center">
                <div>Successfully performed the action!
                    You may now close this page
                </div>
            </div>
        </div>


    )
}

export default success