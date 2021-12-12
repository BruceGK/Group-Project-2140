import { createApp } from 'vue'
import App from './App.vue'
import naive from 'naive-ui'
import router from './router'


const app = createApp(App)
app.use(router)

app.use(naive)

//router.isReady().then(() =>
app.mount('#app')



