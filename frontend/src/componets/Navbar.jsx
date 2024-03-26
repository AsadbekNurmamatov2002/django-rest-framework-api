


function Navbar(){
    return(
        <>
          <nav className=" flex flex-row justify-between items-center w-full h-20 bg-zinc-950 shadow-2xl shadow-black">
            <div className=" text-white  ml-5 text-2xl">
                Logo
            </div>
            <div>
                <input className=" rounded-xl bg-slate-100 text-zinc-950 outline-none py-[4px] mx-4 px-2 pl-4" type="text" placeholder="search..." />
                <button className="">?</button>
            </div>
                <ul className=" flex mr-6">
                    <li className="text-slate-100 text-center px-2 py-[2px] mx-4 rounded-lg hover:bg-white hover:text-zinc-950">Home</li>
                    <li className="text-slate-100 text-center px-2 py-[2px] mx-4 rounded-lg hover:bg-white hover:text-zinc-950">About</li>
                    <li className="text-slate-100 text-center px-2 py-[2px] mx-4 rounded-lg hover:bg-white hover:text-zinc-950">Contact</li>
                    <li><button className=" bg-blue-700 text-blue-50 rounded-xl px-5 py-[6px] mx-4 shadow-3xl shadow-blue-700 hover:bg-blue-500">Login</button></li>
                </ul>
          </nav>
        </>
    )
}

export default Navbar;