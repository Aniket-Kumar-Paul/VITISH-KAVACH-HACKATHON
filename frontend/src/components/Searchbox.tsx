import React, { useRef } from "react";
import { BiSearchAlt } from "react-icons/bi";

type Props = {
  placeholder: string;
  name: string;
  callApiFunction: (input: string) => void;
};

export const Searchbox: React.FC<Props> = ({ placeholder, name, callApiFunction }) => {
  const inputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const input = (inputRef.current?.value || "").trim();
    if (input) {
      // call API endpoint with the input
      inputRef.current!.value = "";
      console.log(input);
      callApiFunction(input);
    }
  };

  return (
    <div>
      <form
        action=""
        onSubmit={handleSubmit}
        className="md:flex justify-center"
      >
        <div className="relative flex items-center text-gray-400 focus-within:text-gray-600 md:w-2/3">
          <BiSearchAlt className="w-5 h-5 absolute ml-3 pointer-events-none" />
          <input
            ref={inputRef}
            name={name}
            type="text"
            placeholder={placeholder}
            className="w-full pr-3 pl-10 py-2 font-semibold placeholder-gray-500 text-black rounded-full border-none ring-2 ring-gray-300 focus:ring-gray-500 focus:ring-2"
          />
        </div>
      </form>
    </div>
  );
};
