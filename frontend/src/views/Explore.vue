<script setup>
  import { ref, onMounted, watch } from 'vue';
  import PageTitle from '../components/PageTitle.vue';
  import BusinessCard from '../components/BusinessCard.vue';
  import Loading from "../components/Loading.vue";


  const API_URL = import.meta.env.VITE_API_URL;
  const loading = ref(true);
  const businesses = ref([]);
  const search = ref('');
  const category = ref('');
  const message = ref('');
  const extraMessage = ref('');


  async function selectTab(event) {
    loading.value = true;
    const tabs = document.querySelectorAll(".tab");

    tabs.forEach((tab) => {
      tab.style.backgroundColor = "#F9F9FF";
      tab.style.color = "#001A41";
      tab.style.border = "1px solid #C4C6D0";
      tab.style.fontWeight = "400";
    });

    event.target.style.backgroundColor = "#445E91";
    event.target.style.color = "white";
    event.target.style.border = "none";
    event.target.style.fontWeight = "700";
    category.value = event.target.textContent;
    search.value = '';

    let response;

    if (category.value === 'All') {
      response = await fetch(`${API_URL}/api/v1/businesses`);
    } else {
      response = await fetch(`${API_URL}/api/v1/businesses?category=${category.value}`);
    }

    if (!response.ok) {
      throw new Error("Server error");
    }

    businesses.value = await response.json();
    loading.value = false;
  }


  watch([search], async ([newSearch]) => {
    loading.value = true;
    let response;

    if (category.value === 'All') {
      response = await fetch(`${API_URL}/api/v1/businesses?name=${newSearch}`);
    } else {
      response = await fetch(`${API_URL}/api/v1/businesses?category=${category.value}&name=${newSearch}`);
    }

    if (!response.ok) {
      throw new Error("Server error");
    }

    businesses.value = await response.json();
    if (!businesses.length) {
      message.value = "Could not find the business you are looking for."
      extraMessage.value = "Try something different."
    }

    if (newSearch === '') {
      message.value = ""
      extraMessage.value = ""
    }

    loading.value = false;
  });


  onMounted(async () => {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    businesses.value = await response.json();
    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Explore</PageTitle>
  <div class="tabbar">
    <div @click="selectTab" class="tab selected">All</div>
    <div @click="selectTab" class="tab">Art</div>
    <div @click="selectTab" class="tab">Automotive</div>
    <div @click="selectTab" class="tab">Beauty</div>
    <div @click="selectTab" class="tab">Education</div>
    <div @click="selectTab" class="tab">Entertainment</div>
    <div @click="selectTab" class="tab">Fashion</div>
    <div @click="selectTab" class="tab">Finance</div>
    <div @click="selectTab" class="tab">Food</div>
    <div @click="selectTab" class="tab">Grocery</div>
    <div @click="selectTab" class="tab">Health</div>
    <div @click="selectTab" class="tab">Real Estate</div>
    <div @click="selectTab" class="tab">Sport</div>
    <div @click="selectTab" class="tab">Other</div>
  </div>
  <section class="my-businesses-section">
    <input
      class="search-bar"
      type="search"
      placeholder="Search by business name"
      v-model.lazy="search"
    >
    <div v-if="businesses.length" class="card-container">
      <BusinessCard 
        @click="$router.push(`/explore/businesses/${business.id}`)"
        v-for="business in businesses"
        :key="business.id"
        :name="business.name"
        :description="business.short_description"
        :country_code="business.country_code"
        :phone="business.phone"
        :address="business.address"
        :favorites="business.favorites_count"
        :reviews="business.reviews_count"
        :image="API_URL+business.image"
      />
    </div>
    <div v-else class="info-message">
      <span class="material-symbols-outlined">lightbulb</span>
      {{ message || 'No business in this category.' }}
      <br>
      {{ extraMessage || 'Be the first person to add a business to this category.' }}
    </div>
  </section>
</template>
