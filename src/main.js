// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

import '@/assets/css/container.css'
import '@/assets/css/header.css'
import '@/assets/css/blog.css'
import '@/assets/css/side.css'
import '@/assets/css/index.css'
import '@/assets/css/article.css'

Vue.config.productionTip = false

Vue.filter('toDate', (date) => {
    if (date) {
        const d = new Date(date)
        const minutes = d.getMinutes() < 10 ? '0' + d.getMinutes() : d.getMinutes()
        const hours = d.getHours() < 10 ? '0' + d.getHours() : d.getHours()
        return d.getFullYear() + '年' + (d.getMonth() + 1) + '月' +
            d.getDate() + '日 ' + hours + ' : ' + minutes
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

