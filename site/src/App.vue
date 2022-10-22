<script setup lang="ts">
import Header from "./components/Header.vue";
import Hero from "./components/Hero.vue";
import Metrics from "./components/Metrics.vue";
</script>

<template>
  <Header></Header>
  <div class="w-[70%] mx-auto">
    <Hero></Hero>
    <Metrics></Metrics>
    <div class="h-[1000px]"></div>
  </div>
</template>
<style>
html {
  background-color: #353535;
}
#app {
  color: white;
  font-family: "Inter var";
}
</style>
