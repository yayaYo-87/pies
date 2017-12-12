<template>
    <div class="index__order">
        <div class="index__order_wrapper">
            <div class="index__order_title">
                <span class="index__order_title-text"></span>
            </div>
            <div class="index__order_slider">
                <swiper :options="swiperOption">
                    <swiper-slide
                            :key="index"
                            v-for="(item, index) in result">
                        <div class="order__slider">
                            <div class="order__slider_left">
                                <div class="order__slider_title">{{ item.goods.name }}</div>
                                <div class="order__slider_text">{{ item.goods.shot_description }}</div>
                                <div class="order__slider_desc">Sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea</div>
                                <div class="order__slider_button">
                                    <button class="order__slider_button-left" @click="postProductFair(item.goods.id)">Заказать</button>
                                    <router-link
                                            tag="button"
                                            :to="{ name: 'item', params: {id: 'all', item: item.goods.id } }"
                                            class="order__slider_button-right">Узнать подробнее</router-link>
                                </div>
                            </div>
                            <div class="order__slider_right">
                                <img :src="item.goods.cover" alt="cover">
                            </div>
                        </div>
                    </swiper-slide>
                    <div class="swiper-button-prev" slot="button-prev"></div>
                    <div class="swiper-button-next" slot="button-next"></div>
                </swiper>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    props: ['result'],
    data(){
      return{
        swiperOption: {
          slidesPerView: 1,
          spaceBetween: 30,
          nextButton: '.swiper-button-next',
          prevButton: '.swiper-button-prev',
        }

      }
    },
    methods:{
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

    }

  }
</script>