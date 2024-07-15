<script setup>
  import Loading from '../components/Loading.vue';
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useAuth0 } from '@auth0/auth0-vue';


  const router = useRouter()
  const { logout, isAuthenticated } = useAuth0();


  onMounted(async () => {
    if (await isAuthenticated.value) {
      localStorage.setItem("invoices", "[]");
      logout({ logoutParams: { returnTo: window.location.origin } });
    } else {
      router.push('/');
    }
  })
</script>

<template>
  <Loading />
</template>
