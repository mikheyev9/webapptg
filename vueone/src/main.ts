import { createApp } from 'vue';
import App from './App.vue';
import { createPinia } from 'pinia';
import router from './router';
import VueScrollPicker from 'vue-scroll-picker';
import 'vue-scroll-picker/lib/style.css';

import './index.css';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(VueScrollPicker);

app.mount('#app');
