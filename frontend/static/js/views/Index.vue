<template>
    <div class="index">
        <div class="index__wrapper">
            <div class="index__title">Выбери <span>пирог</span></div>

            <index-slider></index-slider>
            <index-menu></index-menu>
            <index-popular></index-popular>
            <index-about></index-about>
        </div>
    </div>
</template>

<script>
  import indexSlider from '../components/IndexSlider.vue'
  import indexMenu   from '../components/IndexMenu.vue'
  import indexPopular from '../components/IndexPopular.vue'
  import indexAbout from '../components/IndexAbout.vue'

  export default {
    data() {
      return {
      }
    },
    components: {
      indexMenu,
      indexPopular,
      indexAbout,
      indexSlider
    },


  }
</script>