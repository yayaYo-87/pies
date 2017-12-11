<template>
    <div class="basket__wrapper" v-if="nextValid === 3">
        <div class="basket__end">
            <h1>Заказ оформлен!</h1>
            <p>Спасибо за покупку.</p>
        </div>
    </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    computed: {
      basket() {
        return this.$store.state.basket
      },
      nextValid() {
        return this.$store.state.basket.validation
      },
    }

  }
</script>