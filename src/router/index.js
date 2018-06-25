import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Article from '../views/Article.vue'
import About from '../views/About.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/article/:id',
      name: 'Article',
      component: Article
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
  ]
})
