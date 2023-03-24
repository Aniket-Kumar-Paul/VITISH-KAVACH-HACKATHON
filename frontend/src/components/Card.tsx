import React from "react";
import { Link } from "react-router-dom";

type person = {
  "id": number,
  "name": string,
  "image": string,
  "ownerof": string[]
}

export const Card: React.FC<person> = ({ id, name, image, ownerof }) => {
  return (
    <div className="my-10 flex justify-center hover:" key={id}>
      <div className="rounded-lg overflow-hidden shadow-lg max-w-sm w-3/4 sm:w-full lg:w-4/5">
        <Link to={`/peopledetails/${id}`} className="overflow-hidden">
          <img src={image} alt="Person" 
          className="transition-all hover:scale-105"
          />
        </Link>

        <div className="bg-blue-500">
          <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2">{name}</div>
            <span className="text-gray-300">Owner Of:</span>
          </div>
          <div className="grid grid-flow-col gap-5 pb-2 px-6">
            {/* Display only 2 cars */}
            {ownerof.slice(0, 2).map((car, index) => (
              <span
                className="mb-3 text-sm text-center bg-gray-200 rounded-full px-3 py-1 font-bold text-black"
                key={index}
              >
                {car}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
