<template>
    <div class="index__slider">

        <!--<div class="index__slider_saladE">-->
        <!--<img src="/static/img/salad3.png" alt="cover">     s-->
        <!--</div>-->
        <div class="index__slider_wrapper">
            <!--<div class="index__slider_saladQ">-->
            <!--<img src="/static/img/salad1.png" alt="cover">-->
            <!--</div>-->
            <!--<div class="index__slider_saladW">-->
            <!--<img src="/static/img/salad2.png" alt="cover">-->
            <!--</div>-->


            <!--<div class="index__slider_saladR">-->
            <!--<img src="/static/img/saladright.png" alt="cover">-->
            <!--</div>-->
            <!--<div class="index__slider_saladT">-->
            <!--<img src="/static/img/perez.png" alt="cover">-->
            <!--</div>-->
            <swiper :options="swiperOption" ref="mySwiper">
                <swiper-slide>
                    <div class="slider">
                        <div class="slider__left">
                            <div class="slider__title">Lorem ipsum Pizza</div>
                            <div class="slider__desc">dolor sit amet, consectetur adipiscing</div>
                            <div class="slider__img">
                                <img src="/static/img/pizza2.png" alt="cover">
                            </div>
                        </div>
                        <div class="slider__right">
                            <div class="slider__desc">dolor sit amet, consectetur adipiscing</div>
                            <div class="slider__title">Lorem ipsum Pizza</div>
                            <div class="slider__img">
                                <img src="/static/img/pizza1.png" alt="cover">
                            </div>
                        </div>
                        <div class="slider__discount">
                            <div class="slider__discount-title">со скидкой</div>
                            <div class="slider__discount-count">50%</div>
                        </div>
                    </div>
                </swiper-slide>
                <swiper-slide>
                    <div class="slider">
                        <div class="slider__left">
                            <div class="slider__title">Lorem ipsum Pizza</div>
                            <div class="slider__desc">dolor sit amet, consectetur adipiscing</div>
                            <div class="slider__img">
                                <img src="/static/img/pizza2.png" alt="cover">
                            </div>
                        </div>
                        <div class="slider__right">
                            <div class="slider__desc">dolor sit amet, consectetur adipiscing</div>
                            <div class="slider__title">Lorem ipsum Pizza</div>
                            <div class="slider__img">
                                <img src="/static/img/pizza1.png" alt="cover">
                            </div>
                        </div>
                        <div class="slider__discount">
                            <div class="slider__discount-title">со скидкой</div>
                            <div class="slider__discount-count">50%</div>
                        </div>
                    </div>
                </swiper-slide>
            </swiper>
            <div class="slider__pagination" v-if="disabled">
                <div class="slider__pagination_wrapper">
                    <div class="slider__pagination-bullet"
                         v-for="(item, index) in result"
                         :class="{'slider__pagination-active': itemIndex === index}"
                         @click="paginationUp(index)">
                        <img class="slider__pagination-img" :src="item.url" alt="cover">
                        <img class="slider__pagination-img_active" :src="item.coverActive" alt="cover">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import 'swiper/dist/css/swiper.css'
  import {swiper, swiperSlide} from 'vue-awesome-swiper'
  export default {
    data() {
      return {
        disabled: false,
        itemIndex: 0,
        result: [
          {
            url: '/static/img/icon1.png',
            coverActive: '/static/img/pizza222.png'
          }, {
            url: '/static/img/icon1.png',
            coverActive: '/static/img/pizza222.png'
          }
        ],
        swiperOption: {
          direction: 'vertical',
          slidesPerView: 1,
          spaceBetween: 30,
          onSlideChangeStart: (swiper) => {
            this.itemIndex = swiper.activeIndex
          }

        }
      }
    },
    components: {
      swiper,
      swiperSlide,
    },
    computed: {
      swiperOne() {
        return this.$refs.mySwiper.swiper
      }
    },
    methods: {
      paginationUp(index) {
        this.swiperOne.slideTo(index);
        console.log(this.swiperOne)
      }
    },
    mounted() {
      this.disabled = true
    }
  }
</script>
