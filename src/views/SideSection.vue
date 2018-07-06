<template lang="html">
  <section class="secondary section">
    <div class="section">
      <div slot="sidecontent">
        <div class="side-tag">
          <hr class="hidden-sm"></hr>
          <h3>
            <a href="/tags">TAGS</a>
            <div class="tag-list tags-all">
              <a v-for="tag_one in tags" v-bind:href="'/tags#' + tag_one">{{tag_one}}</a>
            </div>
          </h3>  
        </div>
        <div class="side-about">
      	  <hr class="hidden-sm"></hr>
          <h3>
            <a href="/about">ABOUT ME</a>
          </h3>   
          <div class="short-about">
          	<img src="../assets/img/me.jpeg" alt="我的头像">
          	<p>改变就是好事。</p>
          	<ul class="list-inline">       
                <li>
                    <a target="_blank" href="https://www.zhihu.com/people/runtangr">
                        <span class="fa-stack fa-lg">
                            <i class="fa fa-circle fa-stack-2x"></i>
                            <i class="fa  fa-stack-1x fa-inverse">知</i>
                        </span>
                    </a>
                </li>
 
                <li>
                    <a target="_blank" href="https://weibo.com/runtangr">
                        <span class="fa-stack fa-lg">
                            <i class="fa fa-circle fa-stack-2x"></i>
                            <i class="fa fa-weibo fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                </li>
   
                <li>
                    <a target="_blank" href="https://www.facebook.com/runtangr1">
                        <span class="fa-stack fa-lg">
                            <i class="fa fa-circle fa-stack-2x"></i>
                            <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                </li>
          
                <li>
                    <a target="_blank" href="https://github.com/runtangr">
                        <span class="fa-stack fa-lg">
                            <i class="fa fa-circle fa-stack-2x"></i>
                            <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                </li>
                
            </ul>
        </div>  
        </div>    
       </div>     
    </div>
  </section>
</template>

<script>
import {requestTags} from '../api/api'

export default {
  name: 'SideSection',
  data() {
    return {
      tags:[],
    }
  },
  methods: {
    init() {
      requestTags().then((res) => {
        if (res.status == 200) {
          
          this.tags = res.data.tags
        }
      })
    }
  },
  mounted() {
  this.init()
  } 
}
</script>

<style>



</style>
