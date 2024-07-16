<script setup>
  import IconButton from '../components/IconButton.vue';
  import Compressor from 'compressorjs';
  import PageTitle from '../components/PageTitle.vue';
  import Loading from "../components/Loading.vue";
  import { useRoute } from 'vue-router';
  import { ref, onMounted } from 'vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const route = useRoute();
  const loading = ref(true);
  const openDialog = ref(false);
  const businessId = route.params.businessId;
  const productId = route.params.productId;
  const selectedImages = ref([]);
  const images = ref([]);


  function handleImages (event) {
    const files = event.target.files;

    if (files) {
      for (const img of files) {
        new Compressor(img, {
          quality: 0.4,
          success: (result) => {
            selectedImages.value.push(new File([result], result.name));
          },
          error: (err) => {
            throw new Error('Image compression error');
          }
        });
      }
    }
  }


  async function addImage() {
    loading.value = true;
    selectedImages.value.forEach(async (selectedImage) => {
      const formData = new FormData();

      formData.append('product', productId);
      formData.append('image', selectedImage);

      const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/images/`, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error("Server error");
      }

      openDialog.value = false;
      await getImages();
    });
  }


  async function deleteImage(imageId) {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/images/${imageId}/`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    await getImages();
  }


  async function getImages() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/images`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    images.value = await response.json();
    loading.value = false;
  }


  onMounted(async () => {
    await getImages();
  });
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Product Images</PageTitle>
  <section class="additional-images-section">
    <div v-if="images.length" class="images-container">
      <div v-for="image in images" class="image-container">
        <div class="image" :style="`background: url('${API_URL+image.image}')`">
          <img :src="API_URL+image.image" alt="Business image">
        </div>
        <div @click="deleteImage(image.id)" class="delete-button">
          <span class="material-symbols-outlined">delete</span>
        </div>
      </div>
    </div>
    <div v-else class="info-message">
      <span class="material-symbols-outlined">lightbulb</span>
        No image added.
      <br>
      Click on the "Add images" button below to add images.
    </div>
    <div class="action-buttons center">
      <IconButton
        @click="openDialog = true"
        icon="add"
        color="solid-accent">Add images &nbsp</IconButton>
    </div>
  </section>
  <div v-show="openDialog" class="dialog">
    <div class="dialog-container">
      <div class="dialog-title">Add image</div>
      <form @submit.prevent="addImage">
        <div class="field">
          <label for="images">Images *</label>
          <input
            required
            type="file"
            id="images"
            accept="image/*"
            multiple
            @change="handleImages"
          >
        </div>
        <div class="dialog-action-buttons">
          <button type="button" @click="openDialog = false">Cancel</button>
          <button type="submit">Add</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
  button {
    padding: 16px;
    background: none;
    color: var(--accent);
    font-weight: 700;
    font-size: 14px;
  }

  .image {
    width: 100px;
    height: 100px;
  }

  .images-container {
    display: flex;
    gap: 64px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .image-container {
    display: flex;
    gap: 16px;
  }
</style>
