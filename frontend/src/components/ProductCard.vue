<script setup>
  defineProps([
    'name',
    'description',
    'currency',
    'amount',
    'availability',
    'favorites',
    'reviews',
    'image'
  ])
</script>

<template>
  <div class="container">
    <div class="image" :style="`background: url('${image}')`">
      <img :src="image" alt="Business image">
    </div>
    <div class="details">
      <span class="material-symbols-outlined">local_mall</span>
      <div class="content">
        <div class="title">{{ name }}</div>
        <div>{{ description }}</div>
        <strong>{{ availability ? "In stock" : "Out of stock"}}</strong>
        <div class="title">{{ currency }} {{ amount }}</div>
        <div class="reactions">
          <div>
            <span class="material-symbols-outlined">favorite</span>
            <div>{{ favorites || 0 }}</div>
          </div>
          <div>
            <span class="material-symbols-outlined">chat</span>
            <div>{{ reviews || 0}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
