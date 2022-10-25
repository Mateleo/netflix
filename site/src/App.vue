<script setup lang="ts">
import Header from "./components/Header.vue";
import Hero from "./components/Hero.vue";
import Metrics from "./components/Metrics.vue";
import CommonWords from "./components/CommonWords.vue";
import type { Suspense } from "vue";
import CommonWords2 from "./components/CommonWords2.vue";
import CommonWords3 from "./components/CommonWords3.vue";
import Tweet from "./components/Tweet.vue";
import Tweet2 from "./components/Tweet2.vue";
import Quote from "./components/Quote.vue";
import Tweet3 from "./components/Tweet3.vue";
import Pie from "./components/Pie.vue";
import WordCloud from "./components/WordCloud.vue";
</script>

<template>
  <Header></Header>
  <div class="w-[95%] md:w-[80%] lg:w-[70%] xl:w-[60%] mx-auto">
    <Hero></Hero>
    <Metrics></Metrics>
    <Suspense>
      <CommonWords></CommonWords>
    </Suspense>
    <Suspense>
      <CommonWords2></CommonWords2>
    </Suspense>
    <Suspense>
      <CommonWords3></CommonWords3>
    </Suspense>
    <Suspense>
      <Tweet></Tweet>
    </Suspense>
    <Suspense>
      <Tweet2></Tweet2>
    </Suspense>
    <Suspense>
      <Tweet3></Tweet3>
    </Suspense>
    <Pie></Pie>
    <Quote></Quote>
    <WordCloud></WordCloud>
    <div class="h-[300px]"></div>
  </div>
</template>
<style>
html {
  background-color: #292929;
  scroll-behavior: smooth;
}
#app {
  color: white;
  font-family: "Inter var";
}
</style>
