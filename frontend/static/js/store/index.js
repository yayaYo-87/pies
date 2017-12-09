import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import basket from './modules/basket'
import basketPopup from './modules/basketPopup'

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  actions,
  getters,
  modules: {
    basket,
    basketPopup
  },
  strict: debug,
})
