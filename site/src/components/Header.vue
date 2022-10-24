<script setup lang="ts"></script>
<template>
  <div class="fixed top-0 left-0 right-0 z-101">
    <header
      class="px-2 py-1 w-full text-center flex justify-between border-b-[1px] border-white/20 backdrop-blur-[2px] text-white bg-[#292929]/70"
    >
      <div class="flex items-center px-2">
        <img src="../assets/development.png" class="h-[32px] w-[32px]" />
        <div class="font-black text-2xl p-1">EReputation</div>
      </div>
      <nav class="flex items-center text-white font-bold">
        <a
          href="#we"
          class="md:mr-8 mr-2 link-underline no-underline hover:text-[#15c584] transition-all ease-in-out delay-75"
          >Our Goal</a
        >
        <a
          href="#showcase"
          class="link-underline no-underline hover:text-[#15c584] transition-all ease-in-out delay-75"
          >Showcase</a
        >
      </nav>
    </header>
  </div>
  <div class="h-[70px]"></div>
</template>
<style>
.link-underline {
  border-bottom-width: 0;
  background-image: linear-gradient(transparent, transparent),
    linear-gradient(rgb(21, 197, 132), rgb(21, 197, 132));
  background-size: 0 2px;
  background-position: 0 100%;
  background-repeat: no-repeat;
}

.link-underline:hover {
  background-size: 100% 2px;
  background-position: 0 100%;
}
a:any-link {
  text-decoration: none !important;
}
</style>
