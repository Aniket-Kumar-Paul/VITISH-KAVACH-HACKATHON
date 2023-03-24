import React from 'react'
import { useNavigate, useParams } from "react-router-dom";
import { dummyVehicleData } from '../dummy/VehicleData';

export const Vehicle: React.FC = () => {
  // const { id } = useParams<{ id: string }>();
  const car = dummyVehicleData[0];
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center gap-5">
      <div className="p-5 border-2 border-blue-light rounded-2xl w-3/4 lg:w-2/3 flex flex-col">
        <span className="text-2xl font-bold underline text-gray-300 mb-2">
          Car Details
        </span>

        <div className="flex">
          <div className="w-2/3 flex flex-col gap-3">
            <span>ID: {car.id}</span>
            <span>Company: {car.company}</span>
            <span>Model: {car.model}</span>
            <span>Owner: {car.owner}</span>
            <span>Registration Date: {car.regdate}</span>
          </div>

          <div className="w-1/3">
            <img src={car.image} alt="" className="rounded-xl" />
          </div>
        </div>
      </div>

      <button
        onClick={() => navigate(`/locate/${car.id}`)}
        className="bg-blue-light px-5 py-3 text-2xl rounded-full w-3/4 lg:w-1/3 transition ease-in-out delay-150 hover:bg-blue-dark"
      >
        LOCATE
      </button>
    </div>
  )
}
