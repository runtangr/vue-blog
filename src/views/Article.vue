<template lang="html">
<div class="article">
  <nav-header></nav-header>
  <div class="headpic">
	<div class="container headtitle">
	<div class="title">
	  <h1>{{this.article.title}}</h1>
	</div>
	</div>
  </div>
  <div class="content">
     <h1 class="title text-center">{{article.title}}</h1>
     <div class="article-inline">
      <li class="fa fa-calendar">{{this.article.create_at | toDate}}</li>
      <li class="fa fa-tag">{{this.article.tag}}</li>
      <!-- <li class="fa fa-commenting">10</li> -->
    </div>
    <div class="content-md" v-html="mdHtml"></div>
  </div> 

  <div class="content pager">
                    
        <li v-if="this.articleIndex!=(this.articles.length-1) && articles[nextPage]" class="previous">
            <router-link :to="{ name:'Article', params: {id: articles[nextPage].article_id,  index: this.articleIndex + 1}}">
            	<i class="fa fa-angle-double-left" aria-hidden="true"><span>{{articles[nextPage].title}}</span></i>
            </router-link>
        </li>
        
        <li v-if="this.articleIndex!=0 && articles[prePage]" class="next">
            <router-link :to="{ name:'Article', params: {id: articles[prePage].article_id,  index: this.articleIndex - 1}}">
            	<span>{{articles[prePage].title}}<i class="fa fa-angle-double-right" aria-hidden="true"></i></span>
            </router-link>
        </li>                
  </div>

  <article-comment :sourceId="article.article_id"></article-comment>

  <footer class="footer">
		Copyright © Runtangr Blog 2018
  </footer>
</div>
</template>

<script>
import axios from 'axios'
import marked from 'marked'
import NavHeader from '@/views/Header.vue'
import ArticleComment from '@/views/Comment.vue'
import {requestArticle} from '../api/api'
import {mapState} from 'vuex'


const renderer = new marked.Renderer()
renderer.heading = function (text, level) {
    return '<a href="#' + text + '" class="hashTitle" data-scroll><h' + level +
            ' id="' + text + '">' + text + '</h' + level + '></a>'
}

export default {
  name: 'Article',
  components: {
    NavHeader,
    ArticleComment,
  },
  data() {
    return {
      article: '',
      prePage: 0,
      nextPage: 0,
      articleIndex: 0,
    }
  },
  computed: {
  	...mapState(['articles']),
    mdHtml () {
            return marked(this.article.content || '', { renderer: renderer })
        }
  },
  watch: {
	'$route' (to, from) {
		this.init()
		scrollTo(0,0);
	}
  },
  methods: {
    init() {
      let articleId = this.$route.params.id
      this.articleIndex = this.$route.params.index

      requestArticle(articleId).then((res) => {
      	if (res.status == 200) {
      		
      		this.article = res.data
      		// console.log('article:',this.article)
      	}
      })

      // 这里上下一页的显示和隐藏已经判断，这里不再判断
      // 这里上下页有个bug，就是上下页只能显示当前list的文章，如果当前list 文章还有下一页，取当前list文章的最后一篇文章，文章里面的 上下篇文章有问题
      this.nextPage = this.articleIndex + 1
      this.prePage = this.articleIndex - 1
    },
  },
  mounted() {
	this.init()
  } 
}	
</script>

<style>
	
</style>