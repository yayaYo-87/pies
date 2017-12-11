<template>
  <div class="app" id="app">
    <header-block></header-block>
    <transition name="router">
      <div class="loader-wrapper" v-if="loaderw" >
        <div class="loader-wrapper_gif">
          <div class="cssload-thecube">
            <div class="cssload-cube cssload-c1"></div>
            <div class="cssload-cube cssload-c2"></div>
            <div class="cssload-cube cssload-c4"></div>
            <div class="cssload-cube cssload-c3"></div>
          </div>
        </div>
      </div>
    </transition>
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
    data(){
      return{
        loader: true
      }
    },
    components: {
      headerBlock,
      footerBlock
    },
    computed: {
      order(){
        return this.$route.name === 'order'
      },
      loaderw() {
        return this.$store.state.loader.loader

      }
    },
    methods:{
      loaderOk(){
        const loader = document.getElementById('loader')

        this.$store.dispatch('loader', { value: false })
        window.addEventListener('load', function() {
          loader.style.opacity = 0;
          setTimeout(function () {
            document.body.removeChild(loader)
          }, 1000)
        });

      },
      loaderTrue() {
        this.$store.dispatch('loader', { value: true })
      }

    },
    watch: {
      '$route.path': 'loaderTrue',
    },

    mounted(){
//      this.loaderOk()
    }
  }
</script>
