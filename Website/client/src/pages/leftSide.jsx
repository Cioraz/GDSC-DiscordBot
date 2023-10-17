import React from 'react'

const leftSide = () => {
    return (
        <div>
            <div className="hidden sm:block bg-[#000000] relative ">
                <div className="absolute top-0 left-0 p-2">
                    <img
                        src="https://webclub.nitk.ac.in/static/media/webclub-logo-blue.f4acd85e.png"
                        alt="logo"
                        className="w-20 h-20 mx-auto"
                    />
                    <h1 className="inline-block text-[#1490e4] font-extrabold p-2 text-2xl">
                        Webclub
                    </h1>
                </div>
                <div className="h-screen flex items-center flex-col justify-center text-white">
                    <h2 className="sm:text-1xl md:text-2xl lg:text-4xl text-[#b3d3f6] my-4">
                        We Are
                    </h2>

                    <h1 className="block text-[#1490e4] font-extrabold p-2  sm:text-3xl md:text-4xl lg:text-6xl text-center">
                        Web
                        <br />
                        Enthusiasts
                        <br />
                        Club
                    </h1>
                    <h1 className="block lg:text-4xl my-4">NITK</h1>
                </div>
            </div>
        </div>
    )
}

export default leftSide