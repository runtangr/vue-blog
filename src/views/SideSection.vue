<template lang="html">
  <section class="secondary section">
    <div class="section">
      <div slot="sidecontent">
      	<hr class="hidden-sm"></hr>
          <h3>
            <a href="">ABOUT ME</a>
          </h3>   
          <div class="short-about">
          	<img src="../../static/me.jpeg" alt="我的头像">
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
  </section>
</template>

<script>

export default {
  data () {
    return {
      list: [],
      page: 1,
      pageSize: 10,
      count: 0
    }
  }
}
</script>

<style>



</style>
