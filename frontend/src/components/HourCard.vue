<script setup>
  defineProps(['day', 'opens_at', 'closes_at']);
</script>

<template>
  <div class="small container">
    <div class="details">
      <span class="material-symbols-outlined">date_range</span>
      <div class="content">
        <div class="title">{{ day }}</div>
        <div><strong>Opens at: </strong>{{ opens_at }}</div>
        <div><strong>Closes at: </strong>{{ closes_at }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .inactive {
    background: white;
  }
</style>
