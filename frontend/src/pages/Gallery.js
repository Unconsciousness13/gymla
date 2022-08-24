import React from "react";
import logo from "../assets/images/navbar-logo.png";

export default function Gallery() {
  return (
    <div>
      Gallery <img className="logo-nav md:flex" src={logo} alt="logo" />
    </div>
  );
}
