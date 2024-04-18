import React, { useState, useEffect } from "react";
import { Grid } from "@mui/material";
import ParkingSlot from "../components/ParkingSlot";
import CreateParkingSlot from "../components/CreateParkingSlot";
import api from "../api/api";
import { PARKING_SLOT_ALL } from "../api/endpoints";

function HomePage() {
  const [parkingSlots, setParkingSlots] = useState([]);
  const allSlotsUrl = PARKING_SLOT_ALL();

  const fetchSlots = async () => {
    try {
      const response = await api.get("slot/all/");
      setParkingSlots(response.data);
    } catch (error) {
      console.error("Error fetching parking slots:", error);
    }
  };

  useEffect(() => {
    fetchSlots();
  }, []);

  return (
    <>
      <Grid container spacing={2}>
        {parkingSlots.map((slot) => (
          <Grid item key={slot.slot_id} xs={1.2} sm={1.2} md={1.2} lg={1.2}>
            <ParkingSlot parkingSlot={slot} fetchSlots={fetchSlots} />
          </Grid>
        ))}
        <Grid item xs={1.2} sm={1.2} md={1.2} lg={1.2}>
          <CreateParkingSlot />
        </Grid>
      </Grid>
    </>
  );
}

export default HomePage;
