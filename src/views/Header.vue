<template lang="html">
<div class="header navbar animated">
  <div class="container">

    <div class="site-navigation navbar-brand">
      <a href="/">Blog</a>
    </div>

    <nav id="primary-navigation" class="site-navigation primary-navigation">
      <div class="menum">
        <ul class="nav-menu">
          <a href="/"><i class="menu-item"></i>首页</a>
          <a href="/tags"><i class="menu-item"></i>分类</a>
          <a href="/about"><i class="menu-item"></i>关于</a>
        </ul>
      </div>
    </nav>
  </div>
</div>
</template>

<script>
// 实现导航条的自动显示
import Headroom from 'headroom.js'
import axios from 'axios'
export default {
  data () {
    return {
    }
  },
  methods: {
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
  }
}
</script>
