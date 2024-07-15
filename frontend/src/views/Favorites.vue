<script setup>
  import PageTitle from '../components/PageTitle.vue';
  import BusinessFavoriteList from '../components/BusinessFavoriteList.vue';
  import ProductFavoriteList from '../components/ProductFavoriteList.vue';
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useAuth0 } from '@auth0/auth0-vue';


  const { user, isAuthenticated } = useAuth0()
  const router = useRouter();
  const option = ref('fb');


  async function selectTab(event) {
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
    option.value = event.target.id;
  }


  onMounted(async () => {
    if (await isAuthenticated.value) {
    } else {
      router.push('/account/login');
    }
  });
</script>

<template>
  <PageTitle>Favorites</PageTitle>
  <div class="tabbar">
    <div @click="selectTab" id="fb" class="tab selected full-width">
      Businesses
    </div>
    <div @click="selectTab" id="fp" class="tab full-width">
      Products
    </div>
  </div>
    <div v-show="option === 'fb'">
      <BusinessFavoriteList/>
    </div>
    <div v-show="option === 'fp'">
      <ProductFavoriteList/>
    </div>
</template>

<style scoped>
.full-width {
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: center;
  width: 100%;
}
</style>
