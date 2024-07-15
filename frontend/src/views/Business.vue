<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import PageTitle from '../components/PageTitle.vue';
  import Carousel from '../components/Carousel.vue';
  import IconButton from '../components/IconButton.vue';
  import Collapsible from '../components/Collapsible.vue';
  import HourCard from '../components/HourCard.vue';
  import ProductCard from '../components/ProductCard.vue';
  import ActionButton from '../components/ActionButton.vue';
  import LoginRequiredDialog from '../components/LoginRequiredDialog.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue'


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0()
  const loading = ref(true);
  const openDialog = ref(false);
  const icon = ref('favorite');
  const openLoginRequiredDialog = ref(false);
  const business = ref({});
  const hours = ref([]);
  const products = ref([]);
  const route = useRoute();
  const router = useRouter();
  const businessId = route.params.businessId;
  const images = ref([]);
  const loaded = ref(false);


  async function getBusiness() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    business.value = await response.json();
    loading.value = false;
  }


  async function getImages() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/images`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    images.value = [...images.value, ... await response.json()];
    loading.value = false;
  }


  async function getProducts() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    products.value = await response.json();
    loading.value = false;
  }


  async function getBusinessHours() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/hours`);
    
    if (!response.ok) {
      throw new Error("Server error");
    }

    hours.value = await response.json();
    loading.value = false;
  }


  async function toggleFavorite() {
    loading.value = true;
    if (await isAuthenticated.value) {
      let response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/favorites?user=${user.value.sub}`);

      if (!response.ok) {
        throw new Error("Server error");
      }

      const data = await response.json();

      if (data.length) {
        response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/favorites/${data[0].id}`, {
          method: 'DELETE'
        });

        if (!response.ok) {
          throw new Error("Server error");
        }

        icon.value = 'favorite';
      } else {
        const formData = new FormData();

        formData.append('user_id', user.value.sub);
        formData.append('business', businessId);

        response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/favorites/`, {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          throw new Error("Server error");
        }

        icon.value = 'heart_check';
      }

      await getBusiness();
    } else {
      openLoginRequiredDialog.value = true;
    }
    loading.value = false;
  }


  function copyLink() {
    navigator.clipboard.writeText(window.location.origin + route.fullPath);
  }


  onMounted(async () => {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}`);

    if (!response.ok) {
      throw new Error ("Server error");
    }

    business.value = await response.json();

    if (await isAuthenticated.value) {
      const favRes = await fetch(`${API_URL}/api/v1/businesses/${businessId}/favorites?user=${user.value.sub}`);

      if (!favRes.ok) {
        throw new Error ("Server error");
      }

      const data = await favRes.json();

      if (data.length) {
        icon.value = 'heart_check';
      }
    }

    getBusinessHours();
    getProducts();
    images.value.push(business.value);
    await getImages();
    loaded.value = true;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <div class="my-business">
    <PageTitle>Business</PageTitle>
    <div class="flexbox">
      <div class="flex-item">
        <Carousel v-if="loaded" :images="images" />
      </div>
      <div class="flex-item">
        <section class="details">
          <span class="material-symbols-outlined">business</span>
          <div class="content">
            <div class="title">{{ business.name }}</div>
            <div>{{ business.short_description }}</div>
            <div v-if="business.long_description" class="long-description">
              {{ business.long_description }}
            </div>
            <div>
              <strong>
                Category:
              </strong>
              {{ business.other_category || business.category }}
            </div>
            <div v-if="business.address">
              <strong>Located at: </strong>{{ business.address }}
            </div>
            <div v-if="business.phone">
              <strong>Phone: </strong>+{{ business.country_code }}{{ business.phone }}
            </div>
            <div v-if="business.email">
              <strong>Email: </strong>{{ business.email }}
            </div>
            <div v-if="business.website">
              <strong>Website: </strong>
              <a :href="business.website" target="_blank">{{ business.website }}</a>
            </div>
            <div class="reactions">
              <div @click="toggleFavorite">
                <span class="material-symbols-outlined">{{ icon }}</span>
                <div>{{ business.favorites_count }}</div>
              </div>
              <div @click="$router.push(`/explore/businesses/${businessId}/reviews`)">
                <span class="material-symbols-outlined">chat</span>
                <div>{{ business.reviews_count }}</div>
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
    <div class="collapsible-container">
      <Collapsible leadingIcon="date_range" title="Business Hours">
        <section>
          <div v-if="hours.length" class="card-container">
            <HourCard
              v-for="hour in hours"
              :day="hour.day"
              :opens_at="hour.opens_at"
              :closes_at="hour.closes_at"
            />
          </div>
          <div v-else class="info-message">
            <span class="material-symbols-outlined">lightbulb</span>
              No business hour added to this business.
            <br>
              Contact the business owner for more info.
          </div>
        </section>
      </Collapsible>
      <Collapsible leadingIcon="local_mall" title="Products" :isOpen="true">
        <section>
          <div v-if="products.length" class="card-container">
            <ProductCard
              @click="$router.push(`/explore/businesses/${businessId}/products/${product.id}`)"
              v-for="product in products"
              :name="product.name"
              :description="product.short_description"
              :currency="product.currency"
              :amount="product.amount"
              :availability="product.availability"
              :favorites="product.favorites_count"
              :reviews="product.reviews_count"
              :image="API_URL+product.image"
            />
          </div>
          <div v-else class="info-message">
            <span class="material-symbols-outlined">lightbulb</span>
              No product added to this business.
            <br>
              Contact the business owner for more info.
          </div>
        </section>
      </Collapsible>
    </div>
    <div v-show="openDialog" class="share">
      <div class="container share-container">
        <div class="image share-image" :style="`background: url('${API_URL+business.image}')`">
          <img :src="API_URL+business.image" alt="Card image">
        </div>
        <div class="content">
          <div class="title">{{ business.name }}</div>
          <div>{{ business.short_description }}</div>
          <div v-if="business.address"><strong>Located at: </strong>{{ business.address }}</div>
          <div v-if="business.phone"><strong>Phone: </strong>+{{ business.country_code }}{{ business.phone }}</div>
          <div class="reactions">
            <div>
              <span class="material-symbols-outlined">favorite</span>
              <div>{{ business.favorites_count }}</div>
            </div>
            <div>
              <span class="material-symbols-outlined">chat</span>
              <div>{{ business.reviews_count }}</div>
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

<style scoped>
  button {
    padding: 16px;
    background: none;
    color: var(--accent);
    font-weight: 700;
    font-size: 14px;
  }
</style>
