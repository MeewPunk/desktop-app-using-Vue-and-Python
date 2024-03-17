import { createApp } from 'vue';
import App from './App.vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@vuepic/vue-datepicker/dist/main.css';
import VueSelect from 'vue-select';
import PrimeVue from 'primevue/config';
import Button from 'primevue/button';
import 'primevue/resources/themes/lara-light-teal/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import 'ant-design-vue/dist/reset.css';
const app = createApp(App);
app.use(PrimeVue);
app.component('Button', Button);
app.component('VueSelect', VueSelect);
app.mount('#app');

