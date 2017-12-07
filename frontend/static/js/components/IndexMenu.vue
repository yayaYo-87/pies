<template>
    <div class="index__menu">
        <div class="index__menu_title">
            <span class="index__menu_title-text">Меню</span>
        </div>
        <div class="index__menu_wrapper">
            <div class="index__menu_items">
                <router-link tag="div" :to="{ name: 'menu', params: { id: item.slug } }"
                             class="index__menu_item"
                             :key="index"
                             v-for="(item, index) in result">
                    <div class="index__menu_item-img">
                        <img :src="item.icon" alt="img">
                    </div>
                    <div class="index__menu_item-text">
                        {{ item.name }}
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'indexMenu',
    data() {
      return{
        result: []
      }
    },
    methods:{
      get(){
        const self = this;
        axios.get('/api/category/')
          .then(function (response) {
            self.result =  response.data
          })
      }
    },
    created() {
      this.get()
    }
  }
</script>