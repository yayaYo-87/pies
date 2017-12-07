<template>
    <div class="">
        <div class="index__title">Выбери
            <transition name="router" mode="out-in" >
            <span
                    v-if="index === itemIndex"
                    v-for="(item, index) in result"
            >{{ item.name }}</span>
            </transition>
        </div>
        <div class="index__slider">
            <div class="index__slider_wrapper">
                <swiper :options="swiperOption" ref="mySwiper">
                    <swiper-slide
                            :key="index"
                            v-for="(item, index) in result">
                        <div class="slider">
                            <div class="slider__left">
                                <div class="slider__title">{{ item.discount_goods[0].goods.name }}</div>
                                <div class="slider__desc">{{ item.discount_goods[0].goods.shot_description }}</div>
                                <div class="slider__img">
                                    <img :src="item.discount_goods[0].goods.cover" alt="cover">
                                </div>
                            </div>
                            <div class="slider__right">
                                <div class="slider__desc">{{ item.discount_goods[1].goods.shot_description }}</div>
                                <router-link tag="div"
                                             :to="{ name: 'menu', params: { item: 'all' , id: item.discount_goods[0].goods.id } }" class="slider__title">{{ item.discount_goods[1].goods.name }}</router-link>
                                <div class="slider__img">
                                    <img :src="item.discount_goods[1].goods.cover" alt="cover">
                                </div>
                            </div>
                            <div class="slider__discount">
                                <div class="slider__discount-title">со скидкой</div>
                                <div class="slider__discount-count">{{ item.discount }}%</div>
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
                            <img class="slider__pagination-img" :src="item.icon" alt="cover">
                            <img class="slider__pagination-img_active" :src="item.icon_active" alt="cover">
                        </div>
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
    props: ['result'],
    data() {
      return {
        disabled: false,
        itemIndex: 0,
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
