<script setup>
  import { ref, onMounted } from 'vue';
  import { useAuth0 } from '@auth0/auth0-vue';
  import Loading from "../components/Loading.vue";


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const props = defineProps(['businessId', 'review']);
  const emit = defineEmits(['close']);
  const title = ref(props.review.title);
  const content = ref(props.review.content);
  const user_id = ref('');


  async function editBusinessReview() {
    loading.value = true;
    const formData = new FormData();

    formData.append("business", props.businessId);
    formData.append("user_id", user_id.value);
    formData.append("title", title.value);
    formData.append("content", content.value);

    const response = await fetch(`${API_URL}/api/v1/businesses/${props.businessId}/reviews/${props.review.id}/`, {
      method: 'PUT',
      body: formData
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    emit('close');
    loading.value = false;
  }


  async function removeBusinessReview() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${props.businessId}/reviews/${props.review.id}/`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    emit('close');
    loading.value = false;
  }


  onMounted(async () => {
    if (await isAuthenticated.value) {
      user_id.value = user.value.sub;
    }
  })
</script>

<template>
  <Loading v-if="loading"/>
  <div class="dialog-container">
    <div class="dialog-title">Edit review</div>
    <form @submit.prevent="editBusinessReview">
      <div class="field">
        <label for="title" >Title *</label>
        <input
          required
          id="title"
          v-model="title"
          maxlength="60"
          placeholder="eg. Fantastic Product!"
        >
      </div>
      <div class="field">
        <label for="content">Content *</label>
        <textarea
          required
          v-model="content"
          id="content"
          rows="3"
          placeholder="eg. I recently purchased this product and it has exceeded my expectations..."
          maxlength="120">
        </textarea>
      </div>
      <div class="dialog-action-buttons">
        <button type="button" @click="$emit('close')">Cancel</button>
        <button type="button" @click="removeBusinessReview">Remove</button>
        <button type="submit">Save</button>
      </div>
    </form>
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
</style>
