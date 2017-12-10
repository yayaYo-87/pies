import axios from 'axios'

const state = {
  results: []

};


// actions
const actions = {
  results(state){

    axios.get('/api/cart/')
      .then(
        function (response) {

          state.commit('results', { type: 'results', items: response.data[0]});

        },
        function (error) {
        }
      );
  },
  validation(store, {value, typeValid}){
    store.commit('results', { type: typeValid, items: value})
  }

};
// getters
const getters = {

};
// mutations
const mutations = {
  results(state, {type, items}) {
    state[type] = items
  },
  pushItem(state, {type, items}) {
    state[type] = state[type].concat(items)
  },

};

export default {
  state,
  getters,
  actions,
  mutations
}