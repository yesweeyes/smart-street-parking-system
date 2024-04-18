import React, { useState, useEffect } from "react";
import { Grid } from "@mui/material";
import ParkingSlot from "../components/ParkingSlot";
import api from "../api/api";
import { PARKING_SLOT_ALL } from "../api/endpoints";

function HomePage() {
  const [parkingSlots, setParkingSlots] = useState([]);

  const fetchSlots = () => {
    api
    .get(PARKING_SLOT_ALL())
    .then((response) => setParkingSlots(response.data))
    .catch((error) => console.log(error));
  }

  useEffect(() => {
    fetchSlots
  }, []);

  return (
    <>
    <Grid container spacing={2}>
      {parkingSlots.map((slot) => (
        <Grid item key={slot.slot_id} xs={1.2} sm={1.2} md={1.2} lg={1.2}>
          <ParkingSlot parkingSlot={slot} fetchSlots={fetchSlots}/>
        </Grid>
      ))}
    </Grid>
    </>
  );
}

export default HomePage;
