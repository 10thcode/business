<script setup>
  import {ref, onMounted} from 'vue';
  import BusinessCard from '../components/BusinessCard.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const businesses = ref([]);
  const loading = ref(true);


  onMounted(async () => {
    loading.value = true;
    if (await isAuthenticated.value) {
      const response = await fetch(`${API_URL}/api/v1/users/${user.value.sub}/favorites/businesses`);

      if (!response.ok) {
        throw new Error("Server error");
      }

      businesses.value = await response.json();
    }
    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <section class="my-businesses-section">
    <div v-if="businesses.length" class="card-container">
      <BusinessCard 
        @click="$router.push(`/explore/businesses/${business.id}`)"
        v-for="business in businesses"
        :name="business.name"
        :description="business.short_description"
        :phone="business.phone"
        :address="business.address"
        :favorites="business.favorites_count"
        :reviews="business.reviews_count"
        :image="API_URL+business.image"
      />
    </div>
    <div v-else class="info-message">
      <span class="material-symbols-outlined">lightbulb</span>
      No business added to favorite list. 
      <br>
      Click on the ♡ icon of a business to add it to your favorite list.
    </div>
  </section>
</template>
