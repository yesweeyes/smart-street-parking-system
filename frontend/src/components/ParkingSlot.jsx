import React, { useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, Paper, Typography } from '@mui/material';
import api from '../api/api';
import {PARKING_SLOT} from "../api/endpoints";


function ParkingSlot({ parkingSlot, fetchSlots }) {
  const [openModal, setOpenModal] = useState(false);

  const handleSlotClick = () => {
    setOpenModal(true);
  };

  const handleCloseModal = () => {
    setOpenModal(false);
  };

  const parkingSlotStatusColors = {
    OCCUPIED: '#F44336',
    VACANT: '#4CAF50',
  };

  const handleDelete = () => {
    api
    .delete(PARKING_SLOT.PARKING_SLOT_DETAIL_URL(parkingSlot.id))
    .then((response) => console.log(response))
    .catch((error) => console.log(error));

    fetchSlots();
    handleCloseModal();
    
  }

  return (
    <div className="parking-slot-grid-item">
        <Button onClick={handleSlotClick} size="small">
          <Paper elevation={3} sx={{ padding: 2, height: '150px', width: '100px', overflow: 'hidden', backgroundColor: parkingSlotStatusColors[parkingSlot.status] }}>
            <Typography variant="subtitle1">Slot ID: {parkingSlot.id}</Typography>
            <Typography variant="body2">Status: {parkingSlot.status}</Typography>
          </Paper>
        </Button>
      <Dialog open={openModal} onClose={handleCloseModal}>
        <DialogTitle>Slot Details</DialogTitle>
        <DialogContent dividers>
          <Typography variant="body1">Slot ID: {parkingSlot.id}</Typography>
          <Typography variant="body1">Status: {parkingSlot.status}</Typography>
          <Typography variant="body1">Location: {parkingSlot.location}</Typography>
          <Typography variant="body1">Expiration: {parkingSlot.expiration?  
          new Date(parkingSlot.expiration).toLocaleString("en-US", { dateStyle: "medium", timeStyle: "short" })
          : "None"}
          </Typography>
          {parkingSlot?.parkingmeter && (
            <>
              <Typography variant="body1">Battery Level: {parkingSlot.parkingmeter.battery_level}</Typography>
              <Typography variant="body1">Meter Status: {parkingSlot.parkingmeter.status}</Typography>
            </>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseModal} color="primary" size="small">Close</Button>
          <Button onClick={handleDelete} color="primary" size="small">Delete</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export default ParkingSlot;
