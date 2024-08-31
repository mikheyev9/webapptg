import { createRouter, createWebHistory } from 'vue-router';
import type { RouteRecordRaw } from 'vue-router'; // Используем import type
import BirthDateForm from '../components/BirthDateForm.vue';
import UserProfile from '../components/UserProfile.vue';

const routes: Array<RouteRecordRaw> = [
  { path: '/', component: BirthDateForm },
  { path: '/profile', component: UserProfile },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;