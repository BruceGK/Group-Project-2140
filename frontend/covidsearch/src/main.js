import { createApp } from 'vue'
import App from './App.vue'
import naive from 'naive-ui'

createApp(App).mount('#app')
const app = createApp(App)
app.use(naive)