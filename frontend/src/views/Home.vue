<script setup>
  import { onMounted, ref } from 'vue';
  import { useRouter } from 'vue-router';
  import IconButton from '../components/IconButton.vue';
  import ActionButton from '../components/ActionButton.vue';
  import PageTitle from '../components/PageTitle.vue';
  import BusinessCard from '../components/BusinessCard.vue';
  import LoginRequiredDialog from '../components/LoginRequiredDialog.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue'

  
  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0()
  const loading = ref(true);
  const businesses = ref([]);
  const router = useRouter();
  const openLoginRequiredDialog = ref(false);


  async function createBusiness() {
    if (await isAuthenticated.value) {
      router.push('/businesses/add');
    } else {
      openLoginRequiredDialog.value = true;
    }
  }


  onMounted(async () => {
    if (await isAuthenticated.value) {
      const response = await fetch(`${API_URL}/api/v1/businesses?user=${user.value.sub}`);

      if (!response.ok) {
        throw new Error('Server error');
      }

      businesses.value = await response.json();
    }

    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <div class="home">
    <PageTitle>Home</PageTitle>
    <div class="hero">
      <div class="hero-text">Take Your Bizz Online</div>
      <div class="action-buttons">
        <IconButton
          @click="$router.push('/explore')"
          icon="explore"
          color="solid">Explore</IconButton>
        <IconButton
          @click="$router.push('/docs')"
          icon="menu_book"
          color="solid"/>
      </div>
      <ActionButton @click="createBusiness"/>
    </div>
    <section class="my-businesses-section">
      <div class="section-header">My businesses</div>
      <div v-if="businesses.length" class="card-container">
        <BusinessCard 
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
          @click="$router.push(`/businesses/${business.id}`)"
        />
      </div>
      <div v-else class="info-message">
        <span class="material-symbols-outlined">lightbulb</span>
        You have not created a business yet.
        <br>
        Click on the "Create business" button above to get started.
      </div>
    </section>
    <div v-if="openLoginRequiredDialog" class="dialog">
      <LoginRequiredDialog @close="openLoginRequiredDialog = false"/>
    </div>
  </div>
</template>

<style scoped>
  .hero {
    display: flex;
    flex-direction: column;
    gap: 64px;
    align-items: center;
    justify-content: flex-end;
    padding: 16px;
    min-height: 100vh;
    background: url("https://ik.imagekit.io/prezzgh/business/hero.jpg?updatedAt=1719020717994");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }

  .hero-text {
    font-family: 'Stara', sans-serif;
    font-size: 96px;
    color: white;
    line-height: 103px;
    letter-spacing: -5px;
    text-align: center;
  }

  @media (min-width: 640px) {
    .hero {
      justify-content: center;
      padding: 16px 32px;
    }

    .card-container {
      flex-direction: row;

    }
  }

  @media (min-width: 768px) {
    .hero {
      padding: 16px 64px;
      gap: 64px;
    }
  }

  @media (min-width: 1024px) {
    .hero {
      padding: 16px 128px;
    }
  }
</style>
