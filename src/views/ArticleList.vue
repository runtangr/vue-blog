<template lang="html">
<div class="article-list">
  <article class="block" v-for="(item, index) in list">
    <h2><router-link :to="{ name:'Article', params: {id: item.article_id, index: index}}">{{item.title}}</router-link></h2>

    <div class="article-inline">
      <li class="fa fa-calendar">{{item.create_at | toDate}}</li>
      <li class="fa fa-tag">{{item.tag}}</li>
      <!-- <li class="fa fa-commenting">10</li> -->
    </div>
    <div class="abstract">
      <p><router-link :to="{ name:'Article', params: {id: item.article_id,  index: index}}">{{item.content}}</router-link></p>
    </div>

  </article>
  <div class="pages">
    <a v-if="page!=1" href="javascript:;" @click="go(page-=1)" style="float: left;">← Previous page</a>
    <a v-if="list.length==this.pageSize" href="javascript:;" @click="go(page+=1)" style="float: right;">Next page →</a>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import marked from 'marked'
import {requestArticleList, getMatchSchedule} from '@/api/api'
import {mapMutations, mapState} from 'vuex'


export default {

  data () {
    return {
      list: [],
      page: 1,
      pageSize: 5, 
    }
  },
  computed: {
    ...mapState(['tag']),
    tag () {
      return this.$store.state.tag;
    }
  },
  watch: {  
    tag: function(oldTag, newTag) {  
        // console.log("修改前卫：" + oldTag);  
        // console.log("修改后为：" + newTag); 
        this.getArticleList()
    }
  },
  mounted () {
    this.getArticleList()
  },

  methods: {
    ...mapMutations(['set_articles',]),
    getArticleList () {
      var param = {
        page: this.page,
        pageSize: this.pageSize,
        tag: this.tag
      }
      requestArticleList(param).then(result=>{

          let res = result.data
          this.list = res.map(article => {
            let newArticle = {}
            for (let i in article) { newArticle[i] = article[i] }
            newArticle.content = marked(article.content || '').replace(/<[^>]*>/g, '').slice(0, 150) + '......'
            return newArticle
          })
          this.set_articles(this.list)
        })
    },
    go () {
      // console.log(this.page)
      this.getArticleList()

    },
  }
}
</script>

<style media="screen">
.article-list {
  padding: 20px;
  border-radius: 10px;
}
</style>
