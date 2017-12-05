<template>
  <div class="app" id="app">
    <header-block></header-block>
    <transition name="router" mode="out-in" >
      <router-view/>
    </transition>
    <footer-block></footer-block>
  </div>
</template>

<script>
  import headerBlock from '../components/Header.vue'
  import footerBlock from '../components/Footer.vue'

  export default {
    name: 'app',
    components: {
      headerBlock,
      footerBlock
    },
    computed: {
      order(){
        return this.$route.name === 'order'
      }
    }
  }
</script>
