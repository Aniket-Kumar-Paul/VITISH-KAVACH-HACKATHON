import React from "react";
import { useNavigate } from "react-router-dom";
import number_plate from "../image/number_plate.jpg";

export const Home: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col lg:flex-row justify-between">
      <div className="lg:w-1/3 flex flex-col m-5 lg:justify-between">
        <div className="flex flex-col">
        <span className="text-blue-dark text-3xl font-bold mb-3">KAVACH</span>

        <span className="text-2xl">
        Introducing our dynamic surveillance system that integrates multiple image streams to capture and process data with minimal data loss, enabling surveillance and traceability of entities.
        </span>
        </div>

        <div className="flex flex-col my-8 justify-between md:flex-row lg:flex-col">
          <button
            onClick={() => navigate("/searchpeople")}
            className="bg-blue-light px-5 py-3 text-xl rounded-2xl md:w-1/3 mb-5 md:mb-0 lg:w-full lg:mb-5 transition ease-in-out delay-150 hover:bg-blue-dark"
          >
            Search by People
          </button>
          <button
            onClick={() => navigate("/searchvehicle")}
            className="bg-blue-light px-5 py-3 text-xl rounded-2xl md:w-1/3 lg:w-full transition ease-in-out delay-150 hover:bg-blue-dark"
          >
            Search by Vehicle
          </button>
        </div>
      </div>

      <div className="lg:w-2/3 m-5">
        <img 
        className="rounded-2xl"
        src={number_plate} 
        alt="Number Plate Detection" />
      </div>
    </div>
  );
};
