<template>
    <div class="header__basket">
        <router-link :to="{ name: 'basket' }" tag="div" class="header__basket__img">
            <div class="header__basket__img-count">2</div>
        </router-link>
        <div class="header__basket-price">1212 <span class="rubl" > &#8399;</span></div>
    </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    methods: {

    }
  }
</script>