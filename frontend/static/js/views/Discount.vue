<template>
    <div class="discount">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Скидки</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item header__mini_item-active">Скидки</div>
                </div>
            </div>
        </div>
        <div class="discount__wrapper">
            <div class="discount_title">Уважаемые клиенты!</div>
            <p>Благодарим Вас за выбор Пекарни  <span class="discount_red">“Все о пирогах”</span>!</p>
            <p>Заказывать с сайта – выгодно! <span class="discount_red" > Скидка 5%</span></p>
            <p>на всё меню при <span class="discount_border">онлайн-заказе!</span></p>
            <p><span class="discount_border">Обращаем Ваше внимание:</span> скидка не отображается в корзине, а учитывается оператором в процессе оформления заказа.</p>
            <p>Желаем Вам хорошего настроения и ждем Вас снова на сайте нашей Пекарни!</p>

            <router-link :to="{ name:'menu', params: {id: 'all'} }" class="discount_button">Перейти в меню</router-link>
        </div>
    </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    mounted(){
      this.$store.dispatch('loader', { value: false })
    }

  }
</script>