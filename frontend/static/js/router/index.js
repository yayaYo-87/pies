import Vue from 'vue'
import Router from 'vue-router'


const index = () => import('../views/Index.vue');
const menu = () => import('../views/Menu.vue');
const item = () => import('../views/Item.vue');
const discount = () => import('../views/Discount.vue');
const shipping = () => import('../views/Shipping.vue');
const contacts = () => import('../views/Contacts.vue');
const about = () => import('../views/About.vue');
const comment = () => import('../views/Comments.vue');
const basket = () => import('../views/Basket.vue');

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
      path: '/menu/:id',
      name: 'menu',
      component: menu
    },{
      path: '/menu',
      redirect: '/menu/all',
    },{
      path: '/basket',
      name: 'basket',
      component: basket
    },{
      path: '/menu/:id/:item',
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
