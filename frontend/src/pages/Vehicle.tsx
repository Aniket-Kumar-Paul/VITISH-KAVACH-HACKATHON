import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Searchbox } from "../components/Searchbox";
import { dummyVehicleData } from "../dummy/VehicleData";

type Car = {
  id: number;
  company: string;
  model: string;
  image: string;
  owner: string;
  regdate: string;
  number: string;
};

export const Vehicle: React.FC = () => {
  // const { id } = useParams<{ id: string }>();
  // const car = dummyVehicleData[0];
  const navigate = useNavigate();

  const [carData, setCarData] = useState<Car>();

  const callApi = async (input: string) => {
    try {
      // const response = await fetch(`API_ENDPOINT_URL?q=${input}`);
      // const data = await response.json();
      setCarData(dummyVehicleData[0]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <div className="mb-10">
        <Searchbox
          name="searchvehicle"
          placeholder="Search Vehicle"
          callApiFunction={callApi}
        />
      </div>
      {carData && (
        <div className="flex flex-col items-center gap-5">
          <div className="p-5 border-2 border-blue-light rounded-2xl w-3/4 lg:w-2/3 xl:w-1/2 flex flex-col">
            <span className="text-2xl font-bold underline text-gray-300 mb-2">
              Car Details
            </span>

            <div className="flex">
              <div className="w-2/3 flex flex-col gap-3">
                <span>ID: {carData.id}</span>
                <span>Company: {carData.company}</span>
                <span>Model: {carData.model}</span>
                <span>Owner: {carData.owner}</span>
                <span>Registration Date: {carData.regdate}</span>
                <span>Vehicle Number: {carData.number} </span>
              </div>

              <div className="w-1/3">
                <img src={carData.image} alt="" className="rounded-xl" />
              </div>
            </div>
          </div>

          <button
            onClick={() => navigate(`/locate/${carData.id}`)}
            className="bg-blue-light px-5 py-3 text-2xl rounded-full w-3/4 lg:w-1/3 transition ease-in-out delay-150 hover:bg-blue-dark"
          >
            LOCATE
          </button>
        </div>
      )}
    </div>
  );
};
