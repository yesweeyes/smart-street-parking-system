import React, { useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, Paper, Typography, TextField } from '@mui/material';
import { Select } from '@mui/base/Select';
import { Option } from '@mui/base/Option';
import api from '../api/api';

function CreateParkingSlot(props) {
  const [createModal, setCreateModal] = useState(false);
  const [newSlotLocation, setNewSlotLocation] = useState("");
  const [newSlotStatus, setNewSlotStatus] = useState("");
  const [isLoading, setIsLoading] = useState(false); // State for loading indicator

  const handleOpenCreateModal = () => {
    setCreateModal(true);
  };

  const handleCloseCreateModal = () => {
    setCreateModal(false);
    setNewSlotLocation(""); // Clear form fields on close
    setNewSlotStatus("");
  };

  const handleCreateSlot = async () => {
    setIsLoading(true); // Set loading indicator
    try {
      const response = await api.post('/slot', {
        location: newSlotLocation,
        status: newSlotStatus,
      });
      console.log('Slot created successfully:', response.data);
      handleCloseCreateModal(); // Close modal on success
      // Handle success further (e.g., show success message)
    } catch (error) {
      console.error('Error creating slot:', error);
      // Handle error (e.g., display error message to user)
    } finally {
      setIsLoading(false); // Clear loading indicator
    }
  };

  return (
    <div className="parking-create-grid-item">
      <Button onClick={handleOpenCreateModal} size="small">
        <Paper elevation={3} sx={{ padding: 2, height: '150px', width: '100px', overflow: 'hidden', backgroundColor: 'cyan' }}>
          Create
        </Paper>
      </Button>
    </div>
  );
}

export default CreateParkingSlot;
