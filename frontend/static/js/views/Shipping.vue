<template>
    <div class="shipping">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Доставка</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item header__mini_item-active">Доставка</div>
                </div>
            </div>
        </div>
        <div class="shipping__wrapper">
            <div class="shipping__list">
                <div class="shipping__item">
                    <div class="shipping__cover">
                        <img src="/static/img/dil1.png" alt="cover">
                        <div class="shipping_title">Только из печи</div>
                    </div>
                    <div class="shipping__text">
                        <div class="shipping__text-wrapper">
                            <p>
                                Выпечка осуществляется
                                <span class="shipping_red">только после</span> <span class="shipping_bold">Вашего
                        телефонного звонка</span>
                                или <span class="shipping_bold">онлайн заказа</span>
                                и <span class="shipping_red">только из</span> <span class="shipping_bold">свежих
                        натуральных продуктов.</span>
                            </p>
                            <p>
                                Благодаря <span class="shipping_bold">специальным
                            термосумкам</span> заказанные блюда доставляются
                                <span class="shipping_red">в горячем виде</span>
                                <span class="shipping_border">в любой конец Москвы</span>.
                            </p>
                            <p>
                                К Вашему столу прямо
                                из печи, сохраняя свое
                                тепло, восхитительный
                                аромат и неповторимый
                                вкус.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="shipping__item">
                    <div class="shipping__cover">
                        <img src="/static/img/dil2.png" alt="cover">
                        <div class="shipping_title">Заказ по телефону</div>
                    </div>
                    <div class="shipping__text">
                        <div class="shipping__text-wrapper">

                            <p>
                                Вы можете <span class="shipping_bold">сделать заказ</span>
                                на доставку <span class="shipping_red">вкусных</span> осетинских пирогов и других блюд
                                <span class="shipping_red">по телефону:</span>
                            </p>
                            <p>
                                <a href="tel:+7 (495) 589-36-93" class="shipping_bold">+7 (495) 589-36-93</a>
                            </p>
                            <p>
                                <a href="tel:+7 (903) 724-03-10" class="shipping_bold">+7 (903) 724-03-10</a>

                            </p>
                            <p>
                                <a href="tel:+7 (495) 724-03-10" class="shipping_bold">+7 (495) 724-03-10</a>

                            </p>
                        </div>
                    </div>
                </div>
                <div class="shipping__item">
                    <div class="shipping__cover">
                        <img src="/static/img/dil3.png" alt="cover">
                        <div class="shipping_title">Время работы</div>
                    </div>
                    <div class="shipping__text">
                        <div class="shipping__text-wrapper">


                            <p>
                                <span class="shipping_bold">Прием заказов:</span><br>
                                с понедельника по субботу<br>
                                <span class="shipping_red">с 09.00 до 21.00,</span><br>
                                в воскресенье<br>
                                <span class="shipping_red">с 10.00 до 21.00.</span>
                            </p>
                            <p>
                                <span class="shipping_bold">Служба доставки:</span><br>
                                с понедельника по субботу<br>
                                <span class="shipping_red"> с 10.00 до 22.00,</span><br>
                                в воскресенье<br>
                                <span class="shipping_red">с 11.00 до 22.00.</span><br>
                                <span class="shipping_border">Средняя длительность<br>
                                    доставки</span> – <span class="shipping_red">1 час.</span>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="shipping__item">
                    <div class="shipping__cover">
                        <img src="/static/img/dil4.png" alt="cover">
                        <div class="shipping_title">Условия доставки</div>
                    </div>
                    <div class="shipping__text">
                        <div class="shipping__text-wrapper">
                            <p>
                                <span class="shipping_bold">Минимальный заказ</span><br>
                                в пределах Москвы – <span class="shipping_red">1000 руб.</span><br>
                            </p>
                            <p></p>
                            <p>
                                <span class="shipping_bold">При онлайн заказе</span><br>
                                предоставляется <span class="shipping_bold">скидка </span> 5%<br>
                                на осетинские пироги.<br>
                                Доставка <span class="shipping_red">БЕСПЛАТНА</span><br>
                                для заказов в пределах МКАД!<br>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="shipping__bot">Стоимость доставки за пределами Москвы, пожалуйста, уточняйте у оператора.</div>
            <div class="shipping__tr">Желаем Вам осетинского здоровья и долголетия, приятного аппетита и хорошего настроения!</div>
        </div>
    </div>
</template>

<script>
  export default {
    data(){
      return{

      }
    },
    mounted(){
      this.$store.dispatch('loader', { value: false })
    }
  }
</script>