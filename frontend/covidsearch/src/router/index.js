import { createWebHistory, createRouter } from 'vue-router'
import DetailPage from '../components/DetailPage.vue';
import homePage from '../components/homePage.vue';


const routes =  [
    { path: '/', component: homePage },
    { path: '/detail/:id',
        name: DetailPage,
        component: DetailPage,
        porps: true
    }
  ]

const router = createRouter({
  history: createWebHistory(),
    routes
});

export default router