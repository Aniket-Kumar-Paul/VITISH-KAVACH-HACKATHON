import React, { useState } from "react";
import { Card } from "../components/Card";
import { Searchbox } from "../components/Searchbox";
// Using dummy data
import { dummyPeopleData } from "../dummy/PeopleData";

type Person = {
  id: number;
  name: string;
  image: string;
  ownerof: string[];
};

export const SearchPeople: React.FC = () => {
  const [peopleData, setPeopleData] = useState<Person[]>([]);
  
  const callApi = async (input: string) => {
    try { 
      const response = await fetch(`API_ENDPOINT_URL?q=${input}`);
      const data = await response.json();
      setPeopleData(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <Searchbox name="searchpeople" placeholder="Search People" callApiFunction={callApi}/>

      {/* CARDS */}
      <div className="grid sm:gap-5 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-5 xl:gap-0 justify-items-center">
        {dummyPeopleData &&
          dummyPeopleData.map((person) => {
            return (
              // CARD
              <Card
                id={person.id}
                name={person.name}
                image={person.image}
                ownerof={person.ownerof}
              />
            );
          })}
      </div>
    </div>
  );
};
