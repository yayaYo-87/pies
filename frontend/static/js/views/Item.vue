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
                        <div class="item__list" v-if="result.goods_consist.length !== 0">
                            <ol class="item__list-ol">
                                <li class="item__list-li" v-for="item in result.goods_consist">{{ item.text_item }}</li>
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
                <div class="item__desc" >
                    <div class="item__desc-title">ОПИСАНИЕ</div>
                    <div class="item__desc-text" v-html="result.description"></div>
                </div>
                <div class="item__rec" v-if="result.related_goods.length !== 0">
                    <div class="item__rec-title">Популярные товары
                        <div class="item__rec-prev" slot="button-prev"></div>
                        <div class="item__rec-next" slot="button-next"></div>
                    </div>
                    <div class="item__rec_list">
                        <swiper :options="swiperOption">
                            <swiper-slide
                                    :key="index"
                                    v-for="(id, index) in result.related_goods">
                                <item-recommended
                                        :id="id"
                                        :key="index"
                                ></item-recommended>
                            </swiper-slide>
                        </swiper>

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
  import itemRecommended from '../components/ItemRecommended.vue'

  export default {
    name:'item',
    data() {
      return{
        result: [],
        swiperOption: {
          slidesPerView: 3,
          spaceBetween: 30,
          slidesPerGroup: 3,
          nextButton: '.item__rec-next',
          prevButton: '.item__rec-prev',
        }

      }
    },
    components:{
      menuBar,
      itemRecommended
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