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
                            <item-order
                                :item="item.goods"
                                :key="index"
                            ></item-order>
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
  import itemOrder from '../components/IndexOrderItem.vue'
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
    components:{
      itemOrder
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