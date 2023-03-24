import React from "react";
import { Link } from "react-router-dom";
import vitlogo from "../image/vitlogo.png";

export const Navbar = () => {
  return (
    <>
      <nav className="my-5 flex justify-center items-center lg:justify-between">
        <Link to="/">
          <span className="text-4xl font-extrabold sm:font-bold">KAVACH</span>
        </Link>

        <div className="w-36 hidden lg:block">
          <img src={vitlogo} alt="" />
        </div>
      </nav>
      <div className="mx-auto lg:mx-0 w-1/2 border border-blue-300 mb-10"></div>
    </>
  );
};
