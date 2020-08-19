import Vue from 'vue';
import App from './App.vue';
import Vuex from 'vuex';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import store from './store'
import { Uploader } from 'vant'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(ElementUI)

Vue.config.productionTip = false;
Vue.use(Vuex);
Vue.use(VueAxios, axios)
Vue.use(Uploader)


new Vue({
    store,
    render: h => h(App)
}).$mount('#app');
