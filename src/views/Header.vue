<template lang="html">
<div class="header navbar animated">
  <div class="container">

    <div class="site-navigation navbar-brand">
      <a @click="setInit()"><router-link to="/">Blog</router-link></a>
    </div>

    <nav id="primary-navigation" class="site-navigation primary-navigation">
      <div class="menum">
        <ul class="nav-menu">
          <li class="menu-item" @click="setInit()"><router-link to="/"><i class="fa fa-home"></i>首页</router-link></li>
          <li id="collapse" class="menu-item">
            <a target="_blank"><i class="fa fa-bars"></i>分类</a>
            <ul class="collapse-menum">
              <li class="menu-item" v-for="item in articleTags">
                <a @click="getTag(item)"><router-link to="/">{{item}}</router-link></a>
              </li>
            </ul>
          </li>
          <li class="menu-item"><router-link :to="{ name:'About'}"><i class="fa fa-user"></i>关于</router-link></li>
        </ul>
      </div>
    </nav>
  </div>
</div>
</template>

<script>
// 实现导航条的自动显示
import Headroom from 'headroom.js'
import {requestArticleList, requestTags} from '../api/api'
import {mapMutations, mapState} from 'vuex'
import axios from 'axios'
export default {
  data () {
    return {
      articleTags: []
    }
  },
  methods: {
    ...mapMutations(['set_tag',]),
    getTags () {
      requestTags().then((result) => {
        let res = result.data
        
        this.articleTags = res       
      })
    },
    getTag (tag) {
      this.set_tag(tag)
    },
    setInit () {
      this.$router.go(0)
    }
  },
  mounted () {
    var myElement = document.querySelector(".header");
    // construct an instance of Headroom, passing the element
    var headroom  = new Headroom(myElement, {
      "tolerance": 1,
      "offset": 10,
      "classes": {
        "initial": "animated",
        "pinned": "slideDown",
        "unpinned": "slideUp"
      }
    });
    headroom.init();
    this.getTags()
  }
}
</script>
