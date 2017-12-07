<template>
    <div class="menu__list_item">
        <div class="menu__list_cover">
            <img :src="result.cover" alt="cover">
            <div class="menu__list_hover">
                <router-link :to="{ name:'item', params: { item: id } }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                <div class="menu__list_hover-bottom">Быстрый заказ</div>
            </div>
        </div>
        <div class="menu__list_desc">
            <div class="menu__list_title">{{ result.name }}</div>
        </div>
        <div class="menu__list_price">{{ result.price }} руб.</div>
        <button class="menu__list_button">Заказать</button>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['id'],
    data(){
      return{
        result: [],
      }
    },
    methods:{
      get(){
        const self = this;

        axios.get('/api/goods/' + self.id + '/')
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