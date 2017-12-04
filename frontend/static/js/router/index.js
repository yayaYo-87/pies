import Vue from 'vue'
import Router from 'vue-router'

import index from '../views/Index.vue'
import menu from '../views/Menu.vue'
import item from '../views/Item.vue'
import discount from '../views/Discount.vue'
import shipping from '../views/Shipping.vue'
import contacts from '../views/Contacts.vue'
import about from '../views/About.vue'
import comment from '../views/Comments.vue'

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
    },{
      path: '/discount',
      name: 'discount',
      component: discount
    },{
      path: '/shipping',
      name: 'shipping',
      component: shipping
    },{
      path: '/menu',
      name: 'menu',
      component: menu
    },{
      path: '/item',
      name: 'item',
      component: item
    },{
      path: '/contacts',
      name: 'contacts',
      component: contacts
    },{
      path: '/about',
      name: 'about',
      component: about
    },,{
      path: '/comment',
      name: 'comment',
      component: comment
    },
  ]
})
