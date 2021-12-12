import { createWebHistory, createRouter } from 'vue-router'
import DetailPage from '../components/DetailPage.vue';
import homePage from '../components/homePage.vue';


const routes =  [
    { path: '/', component: homePage },
    { path: '/detail', component: DetailPage }
  ]

const router = createRouter({
  history: createWebHistory(),
    routes
});

export default router