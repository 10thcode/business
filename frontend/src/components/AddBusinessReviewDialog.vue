<script setup>
  import { ref, onMounted } from 'vue';
  import { useAuth0 } from '@auth0/auth0-vue';
  import Loading from "../components/Loading.vue";


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const props = defineProps(['business']);
  const emit = defineEmits(['close']);
  const title = ref('');
  const content = ref('');
  const user_id = ref('');


  async function addBusinessReview() {
    loading.value = true;
    const formData = new FormData();

    formData.append("business", props.business.id);
    formData.append("user_id", user_id.value);
    formData.append("title", title.value);
    formData.append("content", content.value);

    const response = await fetch(`${API_URL}/api/v1/businesses/${props.business.id}/reviews/`, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    sendNotification(props.business.name);
    emit('close');
    loading.value = false;
  }

  function sendNotification(business) {
    const title = "Business Review";
    const content = `
Someone just reviewed your business, ${business}.

Check it out!

This is Business!`

    const formData = new FormData();

    formData.append('user_id', props.business.user_id);
    formData.append('title', title);
    formData.append('content', content);

    const response = fetch(`${API_URL}/api/v1/users/${props.business.user_id}/notifications/`, {
      method: 'POST',
      body: formData
    });
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
    <div class="dialog-title">Add review</div>
    <form @submit.prevent="addBusinessReview">
      <div class="field">
        <label for="title" >Title *</label>
        <input
          required
          id="title"
          v-model="title"
          maxlength="60"
          placeholder="eg. Excellent Service and ..."
        >
      </div>
      <div class="field">
        <label for="content">Content *</label>
        <textarea
          required
          v-model="content"
          id="content"
          rows="3"
          placeholder="eg. I recently visited this business and was thoroughly impressed by their exceptional service ..."
          maxlength="120">
        </textarea>
      </div>
      <div class="dialog-action-buttons">
        <button type="button" @click="$emit('close')">Cancel</button>
        <button type="submit">Add</button>
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
