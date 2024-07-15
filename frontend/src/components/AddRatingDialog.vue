<script setup>
  import { ref, onMounted } from 'vue';
  import Loading from "../components/Loading.vue";


  const API_URL = import.meta.env.VITE_API_URL;
  const emit = defineEmits(['close']);
  const name = ref('');
  const loading = ref(true);
  const content = ref('');
  const rating = ref(1);


  async function addRating() {
    loading.value = true;
    const formData = new FormData();

    formData.append("name", name.value || 'Anonymous');
    formData.append("content", content.value);
    formData.append("rating", rating.value);

    const response = await fetch(`${API_URL}/api/v1/ratings/`, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    emit('close');
  }
  loading.value = false;
</script>


<template>
  <Loading v-if="loading"/>
  <div class="dialog-container">
    <div class="dialog-title">Rate this project</div>
    <form @submit.prevent="addRating">
      <div class="field">
        <label for="name" >Name</label>
        <input
          id="name"
          v-model="name"
          maxlength="60"
          placeholder="eg: Anonymous"
        >
      </div>
      <div class="field">
        <label for="content">Rating *</label>
        <div class="stars">
          <span v-for="n in rating * 1" class="material-symbols-outlined">star</span>
        </div>
        <input
          v-model="rating"
          type="range"
          step="1" min="1" max="5">
      </div>
      <div class="field">
        <label for="content">Review *</label>
        <textarea
          required
          v-model="content"
          id="content"
          rows="3"
          placeholder="eg. Excellent project! Highly recommended ..."
          maxlength="360">
        </textarea>
      </div>
      <div class="dialog-action-buttons">
        <button type="button" @click="$emit('close')">Cancel</button>
        <button type="submit">Rate</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
  .stars {
    display: flex;
    justify-content: center;
  }

  button {
    padding: 16px;
    background: none;
    color: var(--accent);
    font-weight: 700;
    font-size: 14px;
  }
</style>
