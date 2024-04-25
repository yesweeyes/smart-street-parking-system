import axios from "axios"

const api = axios.create({
    baseURL: false? 
    process.env.VITE_API_URL_LOCAL:
    process.env.VITE_API_URL_PROD
});

export default api;