<script setup>
  import Loading from "../components/Loading.vue";
  import { onMounted} from 'vue';
  import { useAuth0 } from '@auth0/auth0-vue';
  import { useRouter } from "vue-router";


  const router = useRouter();
  const { loginWithRedirect, isAuthenticated } = useAuth0();


  onMounted(async () => {
    if (!(await isAuthenticated.value)) {
      loginWithRedirect();
    } else {
      router.push('/account');
    }
  });
</script>

<template>
  <Loading />
</template>
