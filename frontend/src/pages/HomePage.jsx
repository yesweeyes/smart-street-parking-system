import React, { useState, useEffect } from "react";
import { Grid,  Button, Typography } from "@mui/material";
import ParkingSlot from "../components/ParkingSlot";
import api from "../api/data";
import { PARKING_METER, PARKING_SLOT } from "../api/endpoints";

function HomePage() {
  const [parkingSlots, setParkingSlots] = useState([]);
  const [parkingSlotsCount, setParkingSlotsCount] = useState([]);

  const fetchSlots = async () => {
    try {
      const response = await api
      .get(PARKING_SLOT.PARKING_SLOT_BASE_URL());
      setParkingSlots(response.data);
    } catch (error) {
      console.error("Error fetching parking slots:", error);
    }
  };

  const fetchSlotsCount = async () => {
    try {
      const response = await api
      .get(PARKING_METER.PARKING_METER_ALL_URL());
      setParkingSlotsCount(response.data.count);
    } catch (error) {
      console.error("Error fetching parking slots count:", error);
    }
  };

  const handleDeleteAll = async () => {
    try {
      const response = await api
      .delete(PARKING_SLOT.PARKING_SLOT_BASE_URL());
    } catch (error) {
      console.error("Error while deleteing slots:", error);
    }
  }

  useEffect(() => {
    fetchSlots();
    fetchSlotsCount();
  }, []);

  return (
    <>
    <Button onClick={handleDeleteAll} color="primary" size="small">Delete All</Button>
    <Typography>Count:{parkingSlotsCount}</Typography>
      <Grid container spacing={2}>
        {parkingSlots.map((slot) => (
          <Grid item key={slot.id} xs={1.2} sm={1.2} md={1.2} lg={1.2}>
            <ParkingSlot parkingSlot={slot} fetchSlots={fetchSlots} />
          </Grid>
        ))}
      </Grid>
    </>
  );
}

export default HomePage;
