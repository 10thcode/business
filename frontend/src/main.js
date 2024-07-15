import './assets/css/main.css'

import { createApp } from 'vue'
import { createAuth0 } from '@auth0/auth0-vue'
import App from './App.vue'
import router from './router'


const app = createApp(App)
const AUTH0_DOMAIN = import.meta.env.VITE_AUTH0_DOMAIN;
const AUTH0_CLIENT_ID = import.meta.env.VITE_AUTH0_CLIENT_ID;


app.config.errorHandler = (err, vm, info) => {
  router.push('/error')
}

window.addEventListener('unhandledrejection', (event) => {
  router.push('/error')
})

app.use(router)
app.use(
  createAuth0({
    domain: AUTH0_DOMAIN,
    clientId: AUTH0_CLIENT_ID,
    authorizationParams: {
      redirect_uri: window.location.origin
    },
      cacheLocation: 'localstorage',
  })
);

app.mount('#app')
