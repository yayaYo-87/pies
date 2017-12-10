<template>
    <div class="menu">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Меню</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item"
                         :class="{ 'header__mini_item-active': $route.params.id === 'all'  }"
                    >Меню</div>
                    <div v-if="$route.params.id !== 'all'"
                         class="header__mini_item header__mini_item-active">> {{ resultPage.name }}</div>
                </div>
            </div>
        </div>

        <div class="menu__wrapper">
            <div class="menu__left">
                <div class="menu__list">
                    <div class="menu__list_item" v-for="item in resultProduct">
                        <div class="menu__list_cover">
                            <img :src="item.cover" alt="cover">
                            <div class="menu__list_hover">
                                <router-link :to="{ name:'item', params: { id: $route.params.id, item: item.id } }"
                                             class="menu__list_hover-top">Быстрый просмотр</router-link>
                                <div class="menu__list_hover-bottom">Быстрый заказ</div>
                            </div>
                        </div>
                        <div class="menu__list_desc">
                            <div class="menu__list_title">{{ item.name }}</div>
                        </div>
                        <div class="menu__list_price">{{ item.price }} руб.</div>
                        <router-link
                                tag="button"
                                :to="{ name:'item', params: { id: $route.params.id, item: item.id } }"
                                class="menu__list_button">Заказать</router-link>
                    </div>
                </div>
            </div>
            <menu-bar></menu-bar>
        </div>

    </div>
</template>

<script>
  import menuBar from '../components/MenuBar.vue'
  import axios from 'axios'

  export default {
    name: 'menu',
    data(){
      return{
        resultProduct: [],
        resultPage: [],
        countProduct: 0
      }
    },
    components:{
      menuBar
    },
    watch: {
      '$route.params.id' : 'get'
    },
    methods:{
      get(){
        const self = this;
        const router = this.$route.params.id;
        if( router === 'all' ){
          axios.get('/api/goods/')
            .then(function (response) {
              self.resultProduct = response.data;
              self.countProduct =  response.data.length
            })
        } else {
          axios.get('/api/category/' + router + '/')
            .then(function (response) {
              self.resultProduct = response.data.goods;
              self.resultPage = response.data;
              self.countProduct =  response.data.goods.length
            })
        }
      }
    },
    created(){
      this.get()
    }
  }
</script>