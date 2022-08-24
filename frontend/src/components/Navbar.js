import React, { useState } from "react";
import { AiOutlineMenu, AiOutlineClose } from "react-icons/ai";
import { Link } from "react-router-dom";
import logo from "../assets/images/navbar-logo.png"

const Navbar = () => {
  const [nav, setNav] = useState(false);
  const handleNav = () => {
    setNav(!nav);
  };
  return (
    <div className="w-full h-[90px] bg-black">
      <div className=" max-w-[1240px] mx-auto px-4 flex justify-between items-center h-full" >
      <img className="logo-nav md:flex" src={logo} alt="logo" />

        {/* <div className="logo-navbar">
          
          <h1 className="text-[#00d8ff]">Isabella</h1>
        </div> */}
        <div className="hidden md:flex">
          <ul className="flex text-white items-center ">
            <Link to="/gallery">
              <li className="navbar-links-li">Gallery</li>
            </Link>
            <Link className="navbar-links-li" to="/videos">
              <li>Videos</li>
            </Link>
          </ul>
        </div>

        {/* Hamburger menu */}

        <div onClick={handleNav} className="block md:hidden">
          {nav ? (
            <AiOutlineClose size={30} className="text-white" />
          ) : (
            <AiOutlineMenu size={30} className="text-white" />
          )}
        </div>

        {/* Mobile menu */}
        <div
          className={
            nav
              ? " w-full bg-black text-white absolute top-[90px] left-0 flex justify-center text-center"
              : "absolute left-[-100%]"
          }
        >
          <ul>
            <Link to="/gallery">
              <li>Gallery</li>
            </Link>
            <Link to="/videos">
              <li>Videos</li>
            </Link>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
