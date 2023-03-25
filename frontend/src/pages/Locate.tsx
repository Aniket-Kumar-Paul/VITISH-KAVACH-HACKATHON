import React from "react";
import { useParams } from "react-router-dom";
import { Maps } from "../components/Maps";

export const Locate: React.FC = () => {
  const coordinates: [number, number] = [12.972391,79.157675];
  const { id } = useParams<{ id: string }>();
  
  return (
    <div className="max-w-screen-sm">
      <Maps coordinates={coordinates} id={id}/>
    </div>
  );
};
