import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
  return (
    <>
      <nav className="my-5 flex justify-center items-center lg:justify-start">
        <Link to="/">
          <span className="text-4xl font-extrabold sm:font-bold">KAVACH</span>
        </Link>
      </nav>
      <div className="mx-auto lg:mx-0 w-1/2 border border-blue-300 mb-10"></div>
    </>
  );
};
