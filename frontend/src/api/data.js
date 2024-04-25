import axios from "axios"

const api = axios.create({
    baseURL: false? 
    import.meta.env.VITE_API_URL_LOCAL:
    import.meta.env.VITE_API_URL_PROD
});

export default api;