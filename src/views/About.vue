<template lang="html">
<div>
  <nav-header></nav-header>
  <div class="headpic">
	  <div class="container headtitle">
	    <div class="title">
	      <h1>About</h1>
	    </div>
	  </div>
  </div>
  <div class="container list">
    <div class="about">
      <blockquote>
        <p>改变就是好事。</p>
      </blockquote>
      
      <div class="about-md" v-html="mdHtml"></div>
    </div>
    <div class="side">
      <side-section></side-section>
    </div>  
  </div>    
  <footer class="footer">
    Copyright © Runtangr Blog 2018
  </footer>
</div>
</template>


<script>
import NavHeader from '@/views/Header.vue'
import SideSection from '@/views/SideSection.vue'
import marked from 'marked'

const about = `
我是一名 Pythoneer，在今后的学习中希望成为一名 Pythonista。
`

export default {
  name: 'About',
  components: {
    NavHeader,
    SideSection,
  },
  data() {
    return {
    }
  },
  computed: {
    mdHtml() {
      return marked(about)
    }
  },
}
</script>