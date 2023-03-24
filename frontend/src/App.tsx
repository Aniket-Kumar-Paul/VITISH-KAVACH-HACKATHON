import React from "react";
import "./App.css";
import { Routes, BrowserRouter, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { SearchPeople } from "./pages/SearchPeople";
import { Vehicle } from "./pages/Vehicle";
import { Locate } from "./pages/Locate";
import { Navbar } from "./components/Navbar";
import { PeopleDetails } from "./pages/PeopleDetails";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/searchpeople" element={<SearchPeople />} />
        <Route path="/peopledetails/:id" element={<PeopleDetails />} />
        <Route path="/searchvehicle" element={<Vehicle />} />
        <Route path="/locate" element={<Locate />} />
      </Routes>
      
    </BrowserRouter>
  );
}

export default App;
