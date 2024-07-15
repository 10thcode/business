<script setup>
  import { RouterView } from 'vue-router';
  import TopBar from './components/TopBar.vue'
  import Footer from './components/Footer.vue';
</script>

<template>
  <TopBar/>
  <RouterView />
  <Footer/>
</template>
