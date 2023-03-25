import React, { useRef, useEffect } from "react";
import mapboxgl, { Map, Marker, Popup } from "mapbox-gl";

interface MapProps {
  coordinates: [number, number];
  id: string | undefined;
}

export const Maps: React.FC<MapProps> = ({ coordinates, id }) => {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapInitRef = useRef<Map | null>(null);

  useEffect(() => {
    // Check if map has already been initialized
    if (!mapInitRef.current) {
      // Initialize map
      mapboxgl.accessToken =
        "pk.eyJ1IjoiaHVtZXNhMTIiLCJhIjoiY2xmbjAyYmdnMDJwMTNyb2RzcmxpY2dyMiJ9.2ews2dSsZ7msy3dAJdfPkg";
      mapInitRef.current = new mapboxgl.Map({
        container: mapContainerRef.current!,
        style: "mapbox://styles/mapbox/streets-v11",
        center: [coordinates[1], coordinates[0]],
        zoom: 6,
      });

      // Add markers for each coordinate and Popups
      const popUp = new Popup({ closeButton: false, anchor: "left" }).setHTML(
        `<div class="text-black">
        <div>
          <strong>ID:</strong>
          ${id}
        </div>
        <div>
          <strong>Latitude:</strong>
          ${coordinates[0]}
        </div>
        <div>
          <strong>Longitude:</strong>
          ${coordinates[1]}
        </div>
        <div>
          <strong>Timestamp:</strong>
          ${new Date(Date.now()).toLocaleString()}
        </div>
        </div>
        `
        // `<div class="text-black">You click here: <br/>[${coordinates[0]},  ${coordinates[1]}]</div>`
      );
      new Marker({ color: "#370b98", scale: 2 })
        .setLngLat([coordinates[1], coordinates[0]])
        .setPopup(popUp)
        .addTo(mapInitRef.current!);
    }

    // Clean up
    // return () => {
    //   mapInitRef.current.remove();
    // };
  }, []);

  return (
    <div>
      <div
        className="absolute"
        ref={mapContainerRef}
        style={{ height: "calc(100vh - 13rem)", width: "calc(100vw - 4rem)" }}
      />
    </div>
  );
};
