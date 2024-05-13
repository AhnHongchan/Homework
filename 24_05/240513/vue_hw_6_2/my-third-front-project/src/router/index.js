// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import MainPage from '../components/MainPage.vue';
import SomeView from '../views/SomeView.vue';
import OtherView from '../views/OtherView.vue';

const routes = [
  {
    path: '/',
    name: 'some',
    component: SomeView
  },
  {
    path: '/other',
    name: 'other',
    component: OtherView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
