<script setup>
  import PageTitle from '../components/PageTitle.vue';
  import Loading from "../components/Loading.vue";
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0()
  const loading = ref(true);
  const router = useRouter();
  const notifications = ref([]);
  

  async function getNotifications() {
    if (await isAuthenticated.value) {
      const response = await fetch(`${API_URL}/api/v1/users/${user.value.sub}/notifications`)

      if (!response.ok) {
        throw new Error("Server error");
      }

      notifications.value = await response.json();
    }
    loading.value = false;
  }


  async function deleteNotification(notification_id) {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/users/${user.value.sub}/notifications/${notification_id}/`, {
      method: 'DELETE'
    })

    if (!response.ok) {
      throw new Error("Server error");
    }

    await getNotifications();
  }


  onMounted(async () => {
    if (await isAuthenticated.value) {
      await getNotifications();
    } else {
      router.push('/account/login');
    }
  });
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Notifications</PageTitle>
  <section>
    <div v-if="notifications.length" class="card-container">
      <div v-for="notification in notifications" :key="notification.id" class="small container">
        <div class="details">
          <span class="material-symbols-outlined">notifications</span>
          <div class="content">
            <div class="title">{{ notification.title }}</div>
            <div class="notification-massage">{{ notification.content }}</div>
            <div class="date">{{ (new Date(notification.created_at)).toLocaleString() }}</div>
          </div>
          <div>
            <div @click="deleteNotification(notification.id)">
              <span class="material-symbols-outlined">delete</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="info-message">
      <span class="material-symbols-outlined">lightbulb</span>
      You have no notification.
      <br>
      You will recieve one soon.
    </div>
  </section>
</template>

<style scoped>
  .notification-massage {
    white-space: pre-wrap;
  }

  .date {
    font-size: 12px;
    color: var(--faded-text);
  }
</style>
