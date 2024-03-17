import { createApp } from 'vue';
import App from './App.vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
import '@fortawesome/fontawesome-free/css/all.css';
import VueSelect from 'vue-select';
import 'ant-design-vue/dist/reset.css';
const app = createApp(App);
app.component('VueSelect', VueSelect);
app.mount('#app');