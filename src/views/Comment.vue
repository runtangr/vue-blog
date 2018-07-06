<template>
    <div class="comment-box">
      <div id="disqus_thread"></div>
    </div>
</template>

<script>
export default {
    mounted() {
        var disqus_shortname = 'runtangr';
        (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
    },
};
</script>
