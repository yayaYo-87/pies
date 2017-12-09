<template>
    <div class="index__about">
        <div class="index__about_title">
            <span class="index__about_title-text">Что говорят о нас</span>
        </div>
        <div class="index__about_wrapper">
            <swiper :options="swiperOption">
                <swiper-slide
                        :key="index"
                        v-for="(item, index) in result">
                    <div class="index__about-slider">
                        <div class="index__about_img">
                            <img :src="item.image" alt="cover">
                        </div>
                        <div class="index__about-text">
                            {{ item.text_item }}
                        </div>
                    </div>
                </swiper-slide>
                <div class="swiper-button-prev" slot="button-prev"></div>
                <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
        </div>
    </div>
</template>

<script>
  import SwiperSlide from "../../../../node_modules/vue-awesome-swiper/src/slide.vue";

  export default {
    props: ['result'],
    components: {SwiperSlide},
    data(){
      return{
        swiperOption: {
          slidesPerView: 1,
          spaceBetween: 30,
          nextButton: '.swiper-button-next',
          prevButton: '.swiper-button-prev',
        }

      }
    }
  }
</script>