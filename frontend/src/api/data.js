import axios from "axios"

const api = axios.create({
    baseURL: import.meta.env.MODE == "LOCAL"? 
    import.meta.env.VITE_API_URL_LOCAL:
    import.meta.env.VITE_API_URL_PROD
});

export default api;