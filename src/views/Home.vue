<template>
	<div>
  		<nav-header></nav-header>
  		<div class="headpic">
	      <div class="container headtitle">
	        <div class="title">
	          <h1>Runtangr Blog</h1>
	        </div>
	      </div>
	    </div>

	    <div class="container list">
	        <div class="articles">
	          <article-list></article-list>
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
import ArticleList from '@/views/ArticleList.vue'
import SideSection from '@/views/SideSection.vue'


import axios from 'axios'
export default {
  name: 'home',
  components: {
	NavHeader,
	ArticleList,
	SideSection
  },
  data() {
    return {
      tag: '',
    }
  },
  mouted() {
    this.getMessages()
  },
  methods: {
  	shareTags(msg) {
      this.tags = msg
    },
    shareTag(msg) {
      this.tag = msg
    },
    getOne(msg) {
      this.tag = msg
    },
    getMessages() {
      
    },
  }
}
</script>

<style>

</style>
