import Vue from 'vue';
import Router from 'vue-router';
import Meetings from '../components/Meetings.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Meetings',
      component: Meetings,
    },
  ],
});
