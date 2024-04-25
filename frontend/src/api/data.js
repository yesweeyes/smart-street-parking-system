import axios from "axios"

const api = axios.create({
    baseURL: process.env.MODE == "PROD"? 
    process.env.VITE_API_URL_PROD:
    process.env.VITE_API_URL_LOCAL
});

export default api;