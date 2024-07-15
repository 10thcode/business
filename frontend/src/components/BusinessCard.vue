<script setup>
  defineProps([
    'name',
    'description',
    'country_code',
    'phone',
    'address',
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
      <span class="material-symbols-outlined">business</span>
      <div class="content">
        <div class="title">{{ name }}</div>
        <div>{{ description }}</div>
        <div v-if="address"><strong>Located at: </strong>{{ address }}</div>
        <div v-if="phone"><strong>Phone: </strong>+{{ country_code }}{{ phone }}</div>
        <div class="reactions">
          <div>
            <span class="material-symbols-outlined">favorite</span>
            <div>{{ favorites }}</div>
          </div>
          <div>
            <span class="material-symbols-outlined">chat</span>
            <div>{{ reviews }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
