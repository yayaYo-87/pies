// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './views/App.vue'
import router from './router/index'
import store from './store'
import Vue2Filters from 'vue2-filters'
import '../style/global.styl'


Vue.config.productionTip = false
//Плагины
import VueAwesomeSwiper from 'vue-awesome-swiper'
import { swiper, swiperSlide } from 'vue-awesome-swiper'

require('swiper/dist/css/swiper.css')
Vue.use(VueAwesomeSwiper);

Vue.use(Vue2Filters);

Vue.directive('click-outside', {
  bind: function(el, binding, vNode) {
    // Provided expression must evaluate to a function.
    if (typeof binding.value !== 'function') {
      const compName = vNode.context.name
      let warn = `[Vue-click-outside:] provided expression '${binding.expression}' is not a function, but has to be`
      if (compName) { warn += `Found in component '${compName}'` }

      console.warn(warn)
    }
    // Define Handler and cache it on the element
    const bubble = binding.modifiers.bubble
    const handler = (e) => {
      if (bubble || (!el.contains(e.target) && el !== e.target)) {
        binding.value(e)
      }
    };
    el.__vueClickOutside__ = handler

    // add Event Listeners
    document.addEventListener('click', handler)
  },

  unbind: function(el, binding) {
    // Remove Event Listeners
    document.removeEventListener('click', el.__vueClickOutside__)
    el.__vueClickOutside__ = null

  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  swiper,
  swiperSlide,
  store,
  template: '<App/>',
  components: { App }
})

