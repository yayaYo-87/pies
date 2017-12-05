<template>
  <div class="footer">
    <div class="footer__wrapper">
      <div class="footer__list">
        <router-link tag="div" :to="{ name: 'index' }" class="footer__list-item">Главная</router-link>
        <router-link tag="div" :to="{ name: 'menu', params:{id: 'all'} }" class="footer__list-item">Меню</router-link>
        <router-link tag="div" :to="{ name: 'about' }" class="footer__list-item">О нас</router-link>
        <router-link tag="div" :to="{ name: 'discount' }" class="footer__list-item">Скидки</router-link>
        <router-link tag="div" :to="{ name: 'shipping' }" class="footer__list-item">Доставка</router-link>
        <router-link tag="div" :to="{ name: 'contacts' }" class="footer__list-item">Контакты</router-link>
      </div>
      <div class="footer__contacts">
        <div class="footer__contacts-item">Наши контакты</div>
        <a href="tel:+7 (495) 369-37-45" class="footer__contacts-tel">+7 (495) 369-37-45</a>
        <div class="footer__contacts_date">пн-сб: с 9:00 до 21:00</br>вс: с 10:00 до 21:00</div>
      </div>

      <div class="footer__soc">
        <div class="footer__soc-item">Присоединяйся к нам</div>
        <div class="footer__soc_image">
          <a class="footer__soc-cover" href="#"><img src="/static/img/vk.svg" alt="cover"></a>
          <a class="footer__soc-cover" href="#"><img src="/static/img/ins.svg" alt="cover"></a>
          <a class="footer__soc-cover" href="#"><img src="/static/img/fs.svg" alt="cover"></a>
          <a class="footer__soc-cover" href="#"><img src="/static/img/sk.svg" alt="cover"></a>
          <a class="footer__soc-cover" href="#"><img src="/static/img/tw.svg" alt="cover"></a>
        </div>
      </div>
      <div class="footer__order">
        <div class="footer__order-item">Сделать заказ теперь еще удобнее</div>
        <div class="footer__order_cover">
          <img src="/static/img/footer11.png" alt="cover">
          <img src="/static/img/footer22.png" alt="cover">
        </div>
      </div>
    </div>
    <div class="footer__cop">
    </div>
  </div>
</template>

<script>
  export default {
    name: 'footer',
    data() {
      return {
      }
    },
    computed: {


    }
  }
</script>
