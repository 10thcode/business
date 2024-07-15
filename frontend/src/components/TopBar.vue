<script setup>
  import LoginRequiredDialog from '../components/LoginRequiredDialog.vue';
  import { RouterLink, useRouter } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { useAuth0 } from '@auth0/auth0-vue'

  const { isAuthenticated } = useAuth0()
  const router = useRouter();
  const openLoginRequiredDialog = ref(false);

  async function getNotifications() {
    if (await isAuthenticated.value) {
      router.push('/notifications');
    } else {
      openLoginRequiredDialog.value = true;
    }
  }

  async function getFavorites() {
    if (await isAuthenticated.value) {
      router.push('/favorites');
    } else {
      openLoginRequiredDialog.value = true;
    }
  }
</script>

<template>
  <div v-if="openLoginRequiredDialog" class="dialog">
    <LoginRequiredDialog @close="openLoginRequiredDialog = false"/>
  </div>
  <header>
    <div class="topbar">
      <div class="home icon" @click="$router.push('/')">
        <span class="material-symbols-outlined">home</span>
      </div>
      <div class="appname">
        <h1>Business</h1>
      </div>
      <div class="notification" @click="getNotifications">
        <span class="material-symbols-outlined">notifications</span>
      </div>
      <div class="favorites" @click="getFavorites">
        <span class="material-symbols-outlined">favorite</span>
      </div>
      <div
        @click="isAuthenticated ? $router.push('/account') : $router.push('/account/login')"
        class="account icon">
        <span class="material-symbols-outlined">{{ isAuthenticated ? "account_circle" : "login" }}</span>
      </div>
    </div>
  </header>
</template>

<style scoped>
  .home, .account, .notification, .favorites{
    cursor: pointer;
  }

  .topbar {
    padding: 16px;
    display: flex;
    gap: 16px;
  }

  .appname {
    font-size: 20px;
    font-weight: 900;
    width: 100%;
  }

  @media (min-width: 640px) {
    .topbar {
      padding: 16px 32px;
    }
  }

  @media (min-width: 768px) {
    .topbar {
      padding: 16px 64px;
    }
  }

  @media (min-width: 1024px) {
    .topbar {
      padding: 16px 128px;
    }
  }
</style>
