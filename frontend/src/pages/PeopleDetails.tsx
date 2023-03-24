import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import { dummyPeopleData } from "../dummy/PeopleData";

export const PeopleDetails = () => {
  // const { id } = useParams<{ id: string }>();
  const person = dummyPeopleData[0];
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center gap-5">
      <div className="p-5 border-2 border-blue-light rounded-2xl w-3/4 lg:w-2/3 xl:w-1/2 flex flex-col">
        <span className="text-2xl font-bold underline text-gray-300 mb-2">
          Person Details
        </span>

        <div className="flex">
          <div className="w-2/3 flex flex-col gap-3">
            <span>ID: {person.id}</span>
            <span>Name: {person.name}</span>
            <span>D.O.B: {person.dob}</span>
            <span>
              Owner Of:{" "}
              {person.ownerof.map((car, index) => (
                <span
                  className="mx-2 text-sm text-center bg-gray-200 rounded-full px-3 py-1 font-bold text-black"
                  key={index}
                >
                  {car}
                </span>
              ))}{" "}
            </span>
          </div>

          <div className="w-1/3">
            <img src={person.image} alt="" className="rounded-xl" />
          </div>
        </div>
      </div>

      <button
        onClick={() => navigate(`/locate/${person.id}`)}
        className="bg-blue-light px-5 py-3 text-2xl rounded-full w-3/4 lg:w-1/3 transition ease-in-out delay-150 hover:bg-blue-dark"
      >
        LOCATE
      </button>
    </div>
  );
};
