<script setup>
  import IconButton from '../components/IconButton.vue';
  import Loading from "../components/Loading.vue";
  import PageTitle from '../components/PageTitle.vue';
  import { onMounted, ref } from 'vue';
  import { useAuth0 } from '@auth0/auth0-vue';


  const { user, isAuthenticated } = useAuth0()
  const loading = ref(true);


  onMounted(async () => {
    if (!(await isAuthenticated.value)) {
      router.push('/account/login')
    }
    loading.value = false;
  })
</script>

<template>
  <PageTitle>Account</PageTitle>
  <Loading v-if="loading"/>
  <div v-if="isAuthenticated" class="profile">
    <div class="profile-image">
      <img :src="user.picture" alt="Profile picture">
    </div>
    <div class="profile-info">
      <div class="profile-name">{{ user.name }}</div>
      <div class="profile-email">{{ user.email }}</div>
      <div class="profile-verified">
        <span class="material-symbols-outlined">verified</span>
        {{ user.email_verified ? "Verified" : "Not verified" }}
      </div>
    </div>
    <IconButton @click="$router.push('/account/logout')" icon="logout" color="solid-accent">Logout</IconButton>
  </div>
</template>

<style scoped>
  .profile {
    display: flex;
    flex-direction: column;
    gap: 32px;
    justify-content: center;
    align-items: center;
    padding: 32px;
  }

  .profile-image {
    display: flex;
    justify-content: center;
    border-radius: 100%;
    overflow: hidden;
  }

  img {
    width: 170px;
    height: auto;
  }

  .profile-info {
    display: flex;
    flex-direction: column;
    gap: 16px;
    text-align: center;
    font-size: 16px;
  }

  .profile-name {
    font-size: 32px;
  }

  .profile-verified {
    display: flex;
    justify-content: center;
    gap: 8px;
    color: green;
  }
</style>
