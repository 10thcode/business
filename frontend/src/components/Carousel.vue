<script setup>
  import { ref } from 'vue';


  const props = defineProps(["images"]);
  const API_URL = import.meta.env.VITE_API_URL;
  const openImageDialog = ref(false);

  let changeImage = setInterval(() => {
    props.images.push(props.images.shift());
  }, 5000);

  function toggleImageDialog() {
    openImageDialog.value = !openImageDialog.value;

    if (openImageDialog.value) {
      clearInterval(changeImage);
    } else {
      changeImage = setInterval(() => {
        props.images.push(props.images.shift());
      }, 5000);
    }
  }
</script>

<template>
  <div class="carousel">
    <div
      @click="toggleImageDialog"
      class="active carousel-item"
      :style="`background: url('${API_URL+images[0].image}')`">
      <img :src="API_URL+images[0].image" alt="Carousel Image">
    </div>
    <div v-if="images[1]" class="inactive carousel-item">
      <img @click="images.push(images.shift())" :src="API_URL+images[1].image" alt="Carousel Image">
    </div>
  </div>
  <div
    @click="toggleImageDialog"
    v-show="openImageDialog"
    class="image-dialog"
  >
    <img :src="API_URL+images[0].image" alt="Image">
  </div>
</template>
