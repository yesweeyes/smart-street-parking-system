import axios from "axios"

const api = axios.create({
    baseURL: "https://smart-parking-system-backend.azurewebsites.net/api/v1/"
});

export default api;