import React from 'react'
import Leftside from '../pages/leftSide'
const success = () => {
    return (

        <div className="grid grid-cols-1 sm:grid-cols-2">
            <Leftside />
            <div className="bg-[#1490e4] h-screen flex flex-col justify-center">
                <div className='block text-center border border-green-600 rounded mx-auto p-5 bg-lime-400'>Successfully performed the action!<br></br>
                    You may now close this page
                </div>
            </div>
        </div>


    )
}

export default success