<script setup>
  import { ref } from 'vue';
  import Loading from "../components/Loading.vue";


  const API_URL = import.meta.env.VITE_API_URL;
  const loading = ref(true);
  const props = defineProps(['hour']);
  const emit = defineEmits(['close']);
  const business = ref(props.hour.business);
  const day = ref(props.hour.day);
  const opensAt = ref(props.hour.opens_at);
  const closesAt = ref(props.hour.closes_at);


  async function editBusinessHour() {
    loading.value = true;
    const formData = new FormData();

    formData.append("business", business.value);
    formData.append("day", day.value);
    formData.append("opens_at", opensAt.value);
    formData.append("closes_at", closesAt.value);

    const response = await fetch(`${API_URL}/api/v1/businesses/${business.value}/hours/${props.hour.id}/`, {
      method: 'PUT',
      body: formData
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    emit('close');
    loading.value = false;
  }


  async function removeBusinessHour() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${business.value}/hours/${props.hour.id}/`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    emit('close');
    loading.value = false;
  }
</script>

<template>
  <Loading v-if="loading"/>
  <div class="dialog-container">
    <div class="dialog-title">Edit business hour</div>
    <form @submit.prevent="editBusinessHour">
      <div class="field">
        <label for="day" >Day</label>
        <select id="day" required v-model="day">
          <option value="" selected disabled>Select day</option>
          <option value="Mondays">Mondays</option>
          <option value="Tuesdays">Tuesdays</option>
          <option value="Wednesdays">Wednesdays</option>
          <option value="Thursdays">Thursdays</option>
          <option value="Fridays">Fridays</option>
          <option value="Saturdays">Saturdays</option>
          <option value="Sundays">Sundays</option>
        </select>
      </div>
      <div class="field">
        <label for="opens_at">Opens at</label>
        <input
          required
          id="opens_at"
          type="time"
          v-model="opensAt"
        >
      </div>
      <div class="field">
        <label for="closes_at">Closes at</label>
        <input
          required
          id="closes_at"
          type="time"
          v-model="closesAt"
        >
      </div>
      <div class="dialog-action-buttons">
        <button type="button" @click="$emit('close')">Cancel</button>
        <button type="button" @click="removeBusinessHour">Remove</button>
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
