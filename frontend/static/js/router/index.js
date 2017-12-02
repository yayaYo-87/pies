import Vue from 'vue'
import Router from 'vue-router'

import index from '../views/Index.vue'

Vue.use(Router);

//При переходе скролит до верха
const scrollBehavior = (to, from, savedPosition) => {
  if (to.hash) {
    console.log(to.hash)
    return {
      selector: to.hash,
    }
  } else {
    return {x: 0, y: 0}
  }
};

export default new Router({
  mode: 'history',
  scrollBehavior,
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
  ]
})
