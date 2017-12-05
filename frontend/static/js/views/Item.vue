<template>
    <div class="item">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Меню</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <router-link
                            v-if="result.length !== 0"
                            :to="{ name: 'menu', params: {id: result.category[0].slug } }"
                            class="header__mini_item ">{{ result.category[0].name }} ></router-link>
                    <div class="header__mini_item header__mini_item-active">{{ result.name }}</div>
                </div>
            </div>
        </div>
        <div class="menu__wrapper" v-if="result.length !== 0">
            <div class="menu__left">
                <div class="item__wrapper">
                    <div class="item__cover">
                        <img :src="result.cover" alt="cover">
                    </div>
                    <div class="item__text">
                        <div class="item__title">{{ result.name }}</div>
                        <div class="item__price">{{ result.price }} руб.</div>
                        <div class="item__list">
                            <ol class="item__list-ol">
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                            </ol>
                        </div>
                        <div class="item__button">
                            <div class="item__button_left">
                                <button class="item__button-sum">-</button>
                                <div class="item__button-text">1</div>
                                <button class="item__button-sum">+</button>
                            </div>
                            <div class="item__button_right">
                                <button class="item-button">Заказать</button>
                            </div>
                        </div>
                        <div class="item__teg">
                            <div class="item__teg-text" v-if=""><span>Категория:</span> {{ result.category[0].name }}</div>
                            <div class="item__teg-text">
                                <span>Теги:</span>
                                <span v-for="item in result.tag"><a href="#">{{ item.name }}</a></span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="item__desc">
                    <div class="item__desc-title">ОПИСАНИЕ</div>
                    <div class="item__desc-text" v-html="result.description"></div>
                </div>
                <div class="item__rec">
                    <div class="item__rec-title">Популярные товары
                        <div class="item__rec-prev"></div>
                        <div class="item__rec-next"></div>
                    </div>
                    <div class="item__rec_list">
                        <div class="menu__list_item">
                            <div class="menu__list_cover">
                                <img src="/static/img/list123.png" alt="cover">
                                <div class="menu__list_hover">
                                    <router-link :to="{ name:'item' }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                                    <div class="menu__list_hover-bottom">Быстрый заказ</div>
                                </div>
                            </div>
                            <div class="menu__list_desc">
                                <div class="menu__list_title">LOREM IPSUM PIE</div>
                            </div>
                            <div class="menu__list_price">600 руб.</div>
                            <button class="menu__list_button">Заказать</button>
                        </div>
                        <div class="menu__list_item">
                            <div class="menu__list_cover">
                                <img src="/static/img/list123.png" alt="cover">
                                <div class="menu__list_hover">
                                    <router-link :to="{ name:'item' }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                                    <div class="menu__list_hover-bottom">Быстрый заказ</div>
                                </div>
                            </div>
                            <div class="menu__list_desc">
                                <div class="menu__list_title">LOREM IPSUM PIE</div>
                            </div>
                            <div class="menu__list_price">600 руб.</div>
                            <button class="menu__list_button">Заказать</button>
                        </div>
                        <div class="menu__list_item">
                            <div class="menu__list_cover">
                                <img src="/static/img/list123.png" alt="cover">
                                <div class="menu__list_hover">
                                    <router-link :to="{ name:'item' }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                                    <div class="menu__list_hover-bottom">Быстрый заказ</div>
                                </div>
                            </div>
                            <div class="menu__list_desc">
                                <div class="menu__list_title">LOREM IPSUM PIE</div>
                            </div>
                            <div class="menu__list_price">600 руб.</div>
                            <button class="menu__list_button">Заказать</button>
                        </div>
                    </div>
                </div>
            </div>
            <menu-bar></menu-bar>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  import menuBar from '../components/MenuBar.vue'

  export default {
    name:'item',
    data() {
      return{
        result: []
      }
    },
    components:{
      menuBar
    },
    watch: {
      '$route.params.item': 'get'
    },
    methods:{
      get(){
        const self = this;
        const router = this.$route.params.item;
        axios.get('/api/goods/' + router + '/')
          .then(function (response) {
            self.result =  response.data
          })
      }
    },
    created(){
      this.get()
    }
  }
</script>