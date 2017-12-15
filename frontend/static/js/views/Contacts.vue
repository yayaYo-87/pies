<template>
    <div class="contacts">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Контакты</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item header__mini_item-active">Контакты</div>
                </div>
            </div>
        </div>
        <div class="contacts__wrapper">
            <div class="contacts__left">
                <div class="contacts__title">Информация</div>
                <div class="contacts__item">
                    <div class="contacts__item_title">
                        <span class="contacts__item-icon"><img src="/static/img/contact1.png" alt="cover"></span>
                        Телефоны
                    </div>
                    <div class="contacts__item_desc">
                        <a href="tel:8 (499) 713-66-00">8 (499) 713-66-00</a>
                        <a href="tel:8 (495) 589-36-93">8 (495) 589-36-93</a>
                        <a href="tel:8 (495) 589-36-93">8 (909) 944-46-22</a>
                    </div>
                </div>
                <div class="contacts__item">
                    <div class="contacts__item_title">
                        <span class="contacts__item-icon"><img src="/static/img/contac2.png" alt="cover"></span>
                        График работы
                    </div>
                    <div class="contacts__item_desc">
                        <p class="contacts__item-bot">
                            <span class="contacts__item-bold">понедельник – суббота:</span><br>
                            с 09.00 до 21.00
                        </p>
                        <p>
                            <span class="contacts__item-bold">воскресенье:</span><br>
                            с 10.00 до 21.00
                        </p>
                    </div>
                </div>
                <div class="contacts__item">
                    <div class="contacts__item_title">
                        <span class="contacts__item-icon"><img src="/static/img/contact3.png" alt="cover"></span>
                        E-mail
                    </div>
                    <div class="contacts__item_desc">
                        <a target="_blank" href="mailto:pirogi-m@mail.ru">pirogi-m@mail.ru</a>
                    </div>
                </div>
                <div class="contacts__item">
                    <div class="contacts__item_title">
                        <span class="contacts__item-icon"><img src="/static/img/contact4.png" alt="cover"></span>
                        Сведения о юридическом лице
                    </div>
                    <div class="contacts__item_desc">
                        <p class="contacts__item-bot">
                            ИП Алов Роман Михайлович.
                        </p>
                        <p class="contacts__item-bot">
                            ОГРНИП 310774625600292
                        </p>
                        <p>
                            <span class="contacts__item-bold">Адрес для корреспонденции:</span><br>
                            г.Москва,  ул.Елецкая 9-2-358
                        </p>
                    </div>
                </div><div class="contacts__item">
                <div class="contacts__item_title">
                    <span class="contacts__item-icon"><img src="/static/img/contact4.png" alt="cover"></span>
                    Всё о пирогах в социальных сетях
                </div>
                <div class="contacts__item_social">
                    <a href="#" class="contacts__item-soc">
                        <img src="/static/img/con1.png" alt="cover">
                    </a>
                    <a href="#" class="contacts__item-soc">
                        <img src="/static/img/con2.png" alt="cover">
                    </a>
                    <a href="#" class="contacts__item-soc">
                        <img src="/static/img/con3.png" alt="cover">
                    </a>
                    <a href="#" class="contacts__item-soc">
                        <img src="/static/img/con4.png" alt="cover">
                    </a>
                    <a href="#" class="contacts__item-soc">
                        <img src="/static/img/con5.png" alt="cover">
                    </a>
                </div>
            </div>
            </div>
            <div class="contacts__right">
                <div class="contacts__title">Отправить сообщение</div>

                <div class="contacts__form">
                    <div class="contacts__form_input">
                        <input type="text" class="form_input" placeholder="Введите имя...">
                        <input type="text" class="form_input" placeholder="Введите E-mail...">
                    </div>
                    <div class="contacts__form_textarea">
                        <textarea rows="10" cols="135" name="text"placeholder="Введите сообщение..."></textarea>
                    </div>
                    <button class="contacts__form_button">Отправить</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    metaInfo () {
      return {
        title: 'Контакты',
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
    data(){
      return{

      }
    },
    mounted(){
      this.$store.dispatch('loader', { value: false })
    }

  }
</script>