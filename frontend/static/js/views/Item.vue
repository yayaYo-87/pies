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
                        <div class="item__price">{{ price }} руб.</div>
                        <div class="item__list" v-if="result.goods_consist.length !== 0">
                            <ol class="item__list-ol">
                                <li class="item__list-li" v-for="item in result.goods_consist">{{ item.text_item }}</li>
                            </ol>
                        </div>
                        <div class="menu__list_bottom">
                            <div class="menu__list_bottom-left">
                                <div class="menu_input" v-click-outside="popupClose">
                                    <div class="menu_input-active"
                                         :class="{ 'menu_input-active-true': popup === true }"
                                         @click="popupActive">{{ weightActive }}г.</div>
                                    <div class="menu_input-popup"
                                         v-show="popup">
                                        <div class="menu_input-popup_item"
                                             :class="{ 'menu_input-popup_item-active' : index === weightActive}"
                                             v-for="(weight, index) in result.goods_weight"
                                             @click="pushPrice(weight)"
                                        >{{ weight.weight }}г.</div>
                                    </div>
                                </div>
                                <div class="menu_count">
                                    <button class="menu_count-minus"
                                            :disabled="count <= 1"
                                            @click="countMinus"
                                    >-</button>
                                    <div class="menu_count-count">{{ count }}</div>
                                    <button class="menu_count-plus" @click="countPlus">+</button>
                                </div>
                            </div>
                            <div class="menu__list_bottom-right">
                                <button @click="postProduct(result.id)" class="menu__list_button">Заказать</button>
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
    metaInfo () {
      return {
        title: this.result.meta_title,
        titleTemplate: '%s | Осетинские пироги',
        meta: [
          {
            name: 'description' ,
            content: this.result.meta_description
          },
          {
            name: 'keywords',
            content: this.result.meta_keywords
          },
        ]
      }
    },
    data() {
      return{
        dis: false,
        popup: false,
        count: 1,
        weightActive: 0,
        weightId: 0,
        price: 0,
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
            self.result =  response.data;
            self.$store.dispatch('loader', { value: false });

            if(self.result.goods_weight[0].discount_price === 0) {
              self.price = self.result.goods_weight[0].price;
              self.weightActive = self.result.goods_weight[0].weight;
              self.weightId = self.result.goods_weight[0].id
            } else {
              self.price = self.result.goods_weight[0].discount_price;
              self.weightActive = self.result.goods_weight[0].weight;
              self.weightId = self.result.goods_weight[0].id
            }

          })
      },
      pushPrice(item){
        this.popup = false;
        if(item.discount_price === 0) {
          this.price = item.price
          this.weightActive = item.weight
          this.weightId = item.id
        } else {
          this.price = item.discount_price
          this.weightActive = item.weight
          this.weightId = item.id
        }
      },
      countPlus(){
        this.count++
      },
      countMinus(){
        this.count--
      },
      popupActive(){
        this.popup = !this.popup
      },
      popupClose(){
        this.popup = false
      },
      postProductFair(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": self.count,
          "weight": self.weightId,
        }).then(
          function (response) {
            self.$store.dispatch('results');
            self.animatePopup();
            self.$router.push({name: 'basket' })
          },
          function (error) {
          }
        )
      },
      postProduct(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": self.count,
          "weight": self.weightId,
        }).then(
          function (response) {
            self.$store.dispatch('results');
            self.animatePopup();
          },
          function (error) {
          }
        )
      },
      animatePopup(){
        const newDiv = document.createElement('div');
        newDiv.classList.add('popup')
        newDiv.innerHTML = 'Товар добавлен в корзину';

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      }
    },
    created(){
      this.get()
    }
  }
</script>