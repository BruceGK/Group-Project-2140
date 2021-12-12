import axios from "axios"

const service = axios.create({
  baseURL: process.env.NODE_ENV === "development" ? "/" : "/api",
})
service.interceptors.response.use((resp) => resp.data)

export default service
