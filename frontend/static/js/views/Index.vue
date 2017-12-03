<template>
    <div class="index">
        <div class="index__wrapper">
            <div class="index__title">Выбери <span>пирог</span></div>
            <index-slider></index-slider>
            <index-menu></index-menu>
            <index-popular></index-popular>
            <index-about></index-about>
            <index-order></index-order>
            <index-image></index-image>
            <index-end></index-end>
        </div>
    </div>
</template>

<script>
  import indexSlider from '../components/IndexSlider.vue'
  import indexMenu   from '../components/IndexMenu.vue'
  import indexPopular from '../components/IndexPopular.vue'
  import indexAbout from '../components/IndexAbout.vue'
  import indexOrder from '../components/IndexOrdering.vue'
  import indexImage from '../components/IndexImage.vue'
  import indexEnd from '../components/IndexEnd.vue'

  export default {
    name: 'index',
    data() {
      return {
      }
    },
    components: {
      indexMenu,
      indexPopular,
      indexAbout,
      indexSlider,
      indexOrder,
      indexImage,
      indexEnd
    },


  }
</script>