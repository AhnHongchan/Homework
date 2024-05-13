// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import MainPage from '../components/MainPage.vue';
import SomeView from '../views/SomeView.vue';
import OtherView from '../views/OtherView.vue';
import StudentView from '../views/StudentView.vue';
import StudentDetailView from '../views/StudentDetailView.vue';


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
  {
    path: '/students',
    name: 'students',
    component: StudentView,
  },
  {
    path: '/students/:name',
    name: 'StudentDetailView',
    component: StudentDetailView
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;