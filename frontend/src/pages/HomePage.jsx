import React, { useState, useEffect } from "react";
import { Grid } from "@mui/material";
import ParkingSlot from "../components/ParkingSlot";
import { ParkingSlots as ParkingSlotEndpoint } from "../api/endpoints";
import api from "../api/api";

function HomePage() {
  const [parkingSlots, setParkingSlots] = useState([]);

  useEffect(() => {
    api
      .get("slot/all/")
      .then((response) => setParkingSlots(response.data))
      .catch((error) => console.log(error));
  }, []);

  return (
    <>
    <Grid container spacing={2}>
      {parkingSlots.map((slot) => (
        <Grid item key={slot.slot_id} xs={1.2} sm={1.2} md={1.2} lg={1.2}>
          <ParkingSlot parkingSlot={slot} />
        </Grid>
      ))}
    </Grid>
    </>
  );
}

export default HomePage;
