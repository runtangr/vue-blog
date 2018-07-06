// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

import './assets/css/container.css'
import './assets/css/header.css'
import './assets/css/blog.css'
import './assets/css/side.css'
import './assets/css/index.css'
import './assets/css/article.css'
import './assets/css/about.css'
import './assets/css/tags.css'


Vue.config.productionTip = false

Vue.filter('toDate', (date) => {
    if (date) {
        return new Date(date).toISOString().slice(0,10).replace(/T/, " ");
    }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  render: h => h(App)
})

