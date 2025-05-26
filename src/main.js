import { createApp } from 'vue'
import App from './App.vue'
import { io } from 'socket.io-client';

const socket = io('http://192.168.1.194:8000');

const app = createApp(App);

app.config.globalProperties.$socket = socket;

app.mount('#app');
