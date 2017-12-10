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
                                <div @click="postProductFair(item.id)" class="menu__list_hover-bottom">Быстрый заказ</div>
                            </div>
                        </div>
                        <div class="menu__list_desc">
                            <div class="menu__list_title">{{ item.name }}</div>
                        </div>
                        <div class="menu__list_price">{{ item.price }} руб.</div>
                        <button @click="postProduct(item.id)" class="menu__list_button">Заказать</button>
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
              self.$store.dispatch('loader', { value: false })
            })
        } else {
          axios.get('/api/category/' + router + '/')
            .then(function (response) {
              self.resultProduct = response.data.goods;
              self.resultPage = response.data;
              self.$store.dispatch('loader', { value: false })
              self.countProduct =  response.data.goods.length
            })
        }
      },
      animatePopup(){
        const newDiv = document.createElement('div');
        newDiv.classList.add('popup')
        newDiv.innerHTML = 'Товар добавлен в корзину';

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      },
      postProduct(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": 1,
        }).then(
          function (response) {
            self.$store.dispatch('results');
            self.animatePopup();
          },
          function (error) {
          }
        )
      },
      postProductFair(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": 1,
        }).then(
          function (response) {
            self.$store.dispatch('results');
            self.animatePopup();
            self.$router.push({name: 'basket' })
          },
          function (error) {
          }
        )
      }
    },
    created(){
      this.get()
    }
  }
</script>