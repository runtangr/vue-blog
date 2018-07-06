<template lang="html">
<div>
  <nav-header></nav-header>
  <div class="headpic">
	  <div class="container headtitle">
	    <div class="title">
	      <h1>Tags</h1>
	    </div>
	  </div>
  </div>

  <div class="tags">
  		<div class="tags-all">
  			<a v-for="tag_one in tags" v-bind:href="'#' + tag_one">{{tag_one}}</a>
		</div>
	  	<div class="tags-list"  v-for="article_tag in articles">
	  		<span class="fa fa-tag listing-seperator" v-bind:id="article_tag[0][0]">{{article_tag[0][0]}}</span>
	  		<div class="post-preview" v-for="article in article_tag">
	  			<router-link :to="{ name:'Article', params: {id: article[2]}}">
	  				<h2>{{article[1]}}</h2>
	  				<h3>{{article[4]}}</h3>
	  			</router-link>
	  			<hr>
	  		</div>
	 	</div>
  </div>
  <footer class="footer">
		Copyright © Runtangr Blog 2018
  </footer>
</div>
</template>

<script>
import Article from '@/views/Article.vue'
import NavHeader from '@/views/Header.vue'

import {requestTags, requestArticleList} from '../api/api'



export default {
  name: 'About',
  components: {
    NavHeader,
  },
  data() {
    return {
      articles:[],
      tags:[],
      tag:'',
    }
  },

  mounted() {
	this.init()
  },
  updated() {
  		this.location()
  },
  methods: {
    init() {
      requestTags().then((res) => {
      	if (res.status == 200) {
      		
      		this.tags = res.data.tags
      	}
      })

      requestArticleList().then((res) => {
      	if (res.status == 200) {
      		
      		this.articles = res.data.articles
      	}
      })
    },
    location () {        
        var location_id=this.$route.hash
        // console.log(location_id)
        // console.log(document.getElementById(location_id.slice(1)))

        if (document.getElementById(location_id.slice(1)) != null) {
            document.getElementById(location_id.slice(1)).scrollIntoView({block: "start", behavior: "smooth"})
            return
        }
    },

  }
 }

</script>