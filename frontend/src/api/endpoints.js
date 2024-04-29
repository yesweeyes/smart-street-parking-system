const PARKING_SLOT = {
    PARKING_SLOT_BASE_URL: () => "slot/",
    PARKING_SLOT_DETAIL_URL: (id) => `slot/${id}/`,
};

const PARKING_METER = {
    PARKING_METER_BASE_URL: () => "meter/",
    PARKING_METER_DETAIL_URL: (id) => `meter/${id}`,
    PARKING_METER_ALL_URL: () => `get-all/`,
};

export {PARKING_SLOT, PARKING_METER};
