<template>
    <div class="index__about">
        <div class="index__about_title">
            <span class="index__about_title-text">Что говорят о нас</span>
        </div>
        <div class="index__about_wrapper">
            <swiper :options="swiperOption">
                <swiper-slide>
                    <div class="index__about-slider">
                        <div class="index__about_img">
                            <img src="/static/img/about111.png" alt="cover">
                        </div>
                        <div class="index__about-text">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                        </div>
                    </div>
                </swiper-slide> <swiper-slide>
                    <div class="index__about-slider">
                        <div class="index__about_img">
                            <img src="/static/img/about111.png" alt="cover">
                        </div>
                        <div class="index__about-text">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                        </div>
                    </div>
                </swiper-slide> <swiper-slide>
                    <div class="index__about-slider">
                        <div class="index__about_img">
                            <img src="/static/img/about111.png" alt="cover">
                        </div>
                        <div class="index__about-text">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                        </div>
                    </div>
                </swiper-slide> <swiper-slide>
                    <div class="index__about-slider">
                        <div class="index__about_img">
                            <img src="/static/img/about111.png" alt="cover">
                        </div>
                        <div class="index__about-text">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
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