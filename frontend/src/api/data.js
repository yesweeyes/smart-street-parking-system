import axios from "axios"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL? 
    import.meta.env.VITE_API_URL:
    "/choreo-apis/smart-parking-system/smartparkingsystembackend/rest-api-be2/v1.0"
});

export default api;