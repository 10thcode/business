<script setup>
  import { useRouter, useRoute } from 'vue-router';
  import { ref, onMounted } from 'vue';
  import PageTitle from '../components/PageTitle.vue';
  import Carousel from '../components/Carousel.vue';
  import IconButton from '../components/IconButton.vue';
  import LoginRequiredDialog from '../components/LoginRequiredDialog.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const route = useRoute();
  const router = useRouter();
  const openDialog = ref(false);
  const icon = ref('favorite');
  const openLoginRequiredDialog = ref(false);
  const businessId = route.params.businessId;
  const productId = route.params.productId;
  const product = ref({});
  const images = ref([]);
  const loaded = ref(false);


  async function getProduct() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    product.value = await response.json();
    loading.value = false;
  }


  async function getImages() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/images`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    images.value = [...images.value, ... await response.json()];
    loading.value = false;
  }


  async function toggleFavorite() {
    loading.value = true;
    if (await isAuthenticated.value) {
      let response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites?user=${user.value.sub}`);

      if (!response.ok) {
        throw new Error("Server error");
      }

      const data = await response.json();

      if (data.length) {
        response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites/${data[0].id}`, {
          method: 'DELETE'
        });

        if (!response.ok) {
          throw new Error("Server error");
        }

        icon.value = 'favorite'
      } else {
        const formData = new FormData();

        formData.append('user_id', user.value.sub);
        formData.append('product', productId);

        response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites/`, {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          throw new Error("Server error");
        }

        icon.value = 'heart_check';
      }

      await getProduct();
    } else {
      openLoginRequiredDialog.value = true;
    }
    loading.value = false;
  }


  function copyLink() {
    navigator.clipboard.writeText(window.location.origin + route.fullPath);
  }


  onMounted(async () => {
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    product.value = await response.json();

    if (await isAuthenticated.value) {
      const favRes = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites?user=${user.value.sub}`);
      const data = await favRes.json();

      if (data.length) {
        icon.value = 'heart_check';
      }
    }

    images.value.push(product.value);
    await getImages();
    loaded.value = true;
    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <div class="my-business">
    <PageTitle>Product</PageTitle>
    <div class="flexbox">
      <div class="flex-item">
        <Carousel v-if="loaded" :images="images"/>
      </div>
      <div class="flex-item">
        <section class="details">
          <span class="material-symbols-outlined">local_mall</span>
          <div class="content">
            <div class="title">{{ product.name }}</div>
            <div>{{ product.short_description }}</div>
            <div v-if="product.long_description" class="long-description">
              {{ product.long_description }}
            </div>
            <div>
              <strong>
                {{ product.availability ? "In stock" : "Out of stock" }}
              </strong>
            </div>
            <div class="title">{{ product.currency }} {{ product.amount }}</div>
            <div class="reactions">
              <div @click="toggleFavorite">
                <span class="material-symbols-outlined">{{ icon }}</span>
                <div>{{ product.favorites_count }}</div>
              </div>
              <div @click="$router.push(`/explore/businesses/${businessId}/products/${productId}/reviews`)">
                <span class="material-symbols-outlined">chat</span>
                <div>{{ product.reviews_count }}</div>
              </div>
            </div>
            <div class="action-buttons">
              <IconButton
                @click="openDialog = true"
                icon="share"
                color="accent"
              >Share</IconButton>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div v-show="openDialog" class="share">
      <div class="container share-container">
        <div class="share-image image" :style="`background: url('${API_URL+product.image}')`">
          <img :src="API_URL+product.image" alt="Card image">
        </div>
        <div class="content">
          <div class="title">{{ product.name }}</div>
          <div>{{ product.short_description }}</div>
          <strong>
            {{ product.availability ? "In stock" : "Out of stock"}}
          </strong>
          <div class="title">{{ product.currency }} {{ product.amount }}</div>
          <div class="reactions">
            <div>
              <span class="material-symbols-outlined">favorite</span>
              <div>{{ product.favorites_count }}</div>
            </div>
            <div>
              <span class="material-symbols-outlined">chat</span>
              <div>{{ product.reviews_count }}</div>
            </div>
          </div>
          <div class="brand">
            <span class="material-symbols-outlined">business</span>
            <div>Business</div>
          </div>
        </div>
      </div>
      <div class="action-buttons center">
        <IconButton @click="copyLink" icon="link" color="solid">Copy link</IconButton>
        <IconButton
          @click="openDialog = false"
          icon="close"
          color="solid"
        />
      </div>
    </div>
    <div v-if="openLoginRequiredDialog" class="dialog">
      <LoginRequiredDialog @close="openLoginRequiredDialog = false"/>
    </div>
  </div>
</template>
