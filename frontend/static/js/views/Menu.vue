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
                    <menu-item-block
                            v-for="(item, index) in resultProduct"
                            :key="index"
                            :itemProduct="item"
                    ></menu-item-block>
                </div>
            </div>
            <menu-bar></menu-bar>
        </div>

    </div>
</template>

<script>
  import menuBar from '../components/MenuBar.vue'
  import axios from 'axios'
  import menuItemBlock from '../components/MenuItem.vue'

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
      menuBar,
      menuItemBlock
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
    },
    created(){
      this.get()
    }
  }
</script>