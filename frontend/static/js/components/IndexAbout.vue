<template>
    <div class="index__about">
        <div class="index__about_title">
            <span class="index__about_title-text">ЗАКАЗАЖИ СОЧНУЮ ПИЦЦУ ПРЯМО СЕЙЧАС</span>
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