<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import PageTitle from '../components/PageTitle.vue';
  import Carousel from '../components/Carousel.vue';
  import IconButton from '../components/IconButton.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const route = useRoute();
  const router = useRouter();
  const openDialog = ref(false);
  const confirmDeleteProduct = ref(false);
  const businessId = route.params.businessId;
  const productId = route.params.productId;
  const product = ref({});
  const images = ref([]);
  const loaded = ref(false);
  const icon = ref('favorite');


  async function getProduct() {
    loading.value = true;
    if (await isAuthenticated.value) {
      const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}?user=${user.value.sub}`);

      if (!response.ok) {
        throw new Error('Server error');
      }

      product.value = await response.json();
    }
    loading.value = false;
  }


  async function getImages() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/images`);

    if (!response.ok) {
      throw new Error('Server error');
    }

    images.value = [...images.value, ... await response.json()];
    loading.value = false;
  }


  async function deleteProduct() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/?user=${user.value.sub}`, {
      method: 'DELETE'
    });

    if (!response.ok) {
      throw new Error('Server error');
    }

    loading.value = false;
    router.push(`/businesses/${businessId}`);
  }


  async function toggleFavorite() {
    loading.value = true;
    let response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites?user=${user.value.sub}`);

    if (!response.ok) {
      throw new Error('Server error');
    }

    const data = await response.json();

    if (data.length) {
      response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites/${data[0].id}`, {
        method: 'DELETE'
      });

      if (!response.ok) {
        throw new Error('Server error');
      }

      icon.value = 'favorite';
    } else {
      const formData = new FormData();

      formData.append('user_id', user.value.sub);
      formData.append('product', productId);

      response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites/`, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Server error');
      }

      icon.value = 'heart_check';
    }

    await getProduct();
    loading.value = false;
  }


  function copyLink() {
    navigator.clipboard.writeText(window.location.origin + route.fullPath);
  }


  onMounted(async () => {
    await getProduct();

    loading.value = true;
    const favRes = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/${productId}/favorites?user=${user.value.sub}`);

    if (!favRes.ok) {
      throw new Error('Server error');
    }

    const data = await favRes.json();

    if (data.length) {
      icon.value = 'heart_check'
    }

    images.value.push(product.value);
    await getImages();
    loaded.value = true;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <div>
    <PageTitle>My Product</PageTitle>
    <div class="flexbox">
      <div class="flex-item">
        <Carousel v-if="loaded" :images="images"/>
        <div class="action-buttons center">
          <IconButton
            @click="$router.push(`/businesses/${businessId}/products/${productId}/images`)"
            icon="gallery_thumbnail"
            color="solid">Manage images</IconButton>
        </div>
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
              <IconButton
                @click="$router.push(`/businesses/${businessId}/products/${productId}/edit`)"
                type='button'
                icon="edit"
                color="accent"
              />
              <IconButton @click="confirmDeleteProduct = true" type='button' icon="delete" color="accent"/>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div v-if="confirmDeleteProduct" class="dialog">
      <div class="dialog-container">
        <div class="dialog-title">Confirm</div>
        <div>
          Are you sure you want to delete this product?
          <br> <br>
          This operation cannot be undone.
        </div>
        <div class="dialog-action-buttons">
          <button type="button" @click="confirmDeleteProduct = false">Cancel</button>
          <button type="button" @click="deleteProduct">Delete forever</button>
        </div>
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
  </div>
</template>

<style scoped>
  button {
    padding: 16px;
    background: none;
    color: var(--accent);
    font-weight: 700;
    font-size: 14px;
  }
</style>
