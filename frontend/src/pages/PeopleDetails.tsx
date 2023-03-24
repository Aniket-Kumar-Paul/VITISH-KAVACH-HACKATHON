import React from "react";
import { useParams } from "react-router-dom";
import { dummyPeopleData } from "../dummy/PeopleData";

export const PeopleDetails = () => {
  // const { id } = useParams<{ id: string }>();
  const person = dummyPeopleData[0];

  return (
    <div className="p-5 border-2 border-blue-light rounded-2xl w-3/4 flex flex-col mx-auto shadow-lg shadow-">
      <span className="text-2xl font-bold underline text-gray-300 mb-2">
        Person Details
      </span>

      <div className="flex">
        <div className="w-2/3 flex flex-col gap-3">
          <span>ID: {person.id}</span>
          <span>Name: {person.name}</span>
          <span>Owner Of: {person.ownerof.map((car, index) => (
            <span
                className="mx-2 text-sm text-center bg-gray-200 rounded-full px-3 py-1 font-bold text-black"
                key={index}
              >
                {car}
              </span>
          ))} </span>
        </div>

        <div className="w-1/3">
          <img src={person.image} alt="" />
        </div>
      </div>
    </div>
  );
};
