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
            <p>ЗАРЕГИСТРИРУЙТЕСЬ И ПОЛУЧИТЕ <span class="discount_red" > СКИДКУ 5%</span></p>
            <p>на всё меню при <span class="discount_border">онлайн-заказе!</span></p>
            <p> ЗАКАЗЫВАЙТЕ БОЛЬШЕ И ВАША СКИДКА БУДЕТ РАСТИ!</p>

            <router-link :to="{ name:'menu', params: {id: 'all'} }" class="discount_button">Перейти в меню</router-link>
        </div>
    </div>
</template>

<script>
  export default {
    metaInfo () {
      return {
        title: 'Скидки',
        titleTemplate: '%s | Осетинские пироги',
        meta: [
          {
            name: 'description' ,
            content: 'ЗАРЕГИСТРИРУЙТЕСЬ И ПОЛУЧИТЕ СКИДКУ 5% НА ВСЁ МЕНЮ ПРИ ОНЛАЙН-ЗАКАЗЕ! ЗАКАЗЫВАЙТЕ БОЛЬШЕ И ВАША СКИДКА БУДЕТ РАСТИ!.'
          },
          {
            name: 'keywords',
            content: 'Пекарня «Всё о пирогах»  выпекающая осетинские пироги по традиционной и оригинальной рецептуре'
          },
        ]
      }
    },
    data() {
      return {

      }
    },
    mounted(){
      this.$store.dispatch('loader', { value: false })
    }

  }
</script>