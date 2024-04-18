import React, { useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, Paper, Typography } from '@mui/material';

function ParkingSlot({ parkingSlot }) {
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

  return (
    <div className="parking-grid">
        <Button onClick={handleSlotClick} size="small">
          <Paper elevation={3} sx={{ padding: 2, height: '150px', width: '100px', overflow: 'hidden', backgroundColor: parkingSlotStatusColors[parkingSlot.status] }}>
            <Typography variant="subtitle1">Slot ID: {parkingSlot.slot_id}</Typography>
            <Typography variant="body2">Status: {parkingSlot.status}</Typography>
          </Paper>
        </Button>
      <Dialog open={openModal} onClose={handleCloseModal}>
        <DialogTitle>Slot Details</DialogTitle>
        <DialogContent dividers>
          <Typography variant="body1">Slot ID: {parkingSlot.slot_id}</Typography>
          <Typography variant="body1">Status: {parkingSlot.status}</Typography>
          <Typography variant="body1">Location: {parkingSlot.location}</Typography>
          <Typography variant="body1">Expiration: {parkingSlot.expiration?  
          new Date(parkingSlot.expiration).toLocaleString("en-US", { dateStyle: "medium", timeStyle: "short" })
          : "None"}
          </Typography>
          <Typography variant="body1">Battery Level: {parkingSlot.parkingmeter.battery_level}</Typography>
          <Typography variant="body1">Meter Status: {parkingSlot.parkingmeter.status}</Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseModal} color="primary" size="small">Close</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export default ParkingSlot;
