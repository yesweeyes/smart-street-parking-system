import axios from "axios"

const api = axios.create({
    baseURL: import.meta.env.MODE == "PROD"? 
    import.meta.env.VITE_API_URL_PROD:
    import.meta.env.VITE_API_URL_LOCAL
});

export default api;