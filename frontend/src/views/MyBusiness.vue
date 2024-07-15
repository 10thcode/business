<script setup>
  import { ref, onMounted } from 'vue';
  import PageTitle from '../components/PageTitle.vue';
  import Carousel from '../components/Carousel.vue';
  import IconButton from '../components/IconButton.vue';
  import Collapsible from '../components/Collapsible.vue';
  import HourCard from '../components/HourCard.vue';
  import ProductCard from '../components/ProductCard.vue';
  import ActionButton from '../components/ActionButton.vue';
  import AddHourDialog from '../components/AddHourDialog.vue';
  import EditHourDialog from '../components/EditHourDialog.vue';
  import Loading from "../components/Loading.vue";
  import { useRoute, useRouter } from 'vue-router';
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const openDialog = ref(false);
  const openAddHour = ref(false);
  const openEditHour = ref(false);
  const confirmDeleteBusiness = ref(false);
  const icon = ref('favorite');
  const business = ref({});
  const hours = ref([]);
  const hour = ref({});
  const products = ref([]);
  const route = useRoute();
  const router = useRouter();
  const businessId = route.params.businessId;
  const images = ref([]);
  const loaded = ref(false);


  async function getBusiness() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}?user=${user.value.sub}`);

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


  async function deleteBusiness() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/`, {
      method: 'DELETE'
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    router.push('/');
    loading.value = false;
  }


  function openEditBusinessHour(businessHour) {
    hour.value = businessHour;
    openEditHour.value = true;
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

        icon.value = 'heart_check'
      }

      await getBusiness();
    } else {
      openLoginRequiredDialog.value = true;
    }
    loading.value = false;
  }


  function copyLink() {
    navigator.clipboard.writeText(window.location.origin + '/explore' +route.fullPath);
  }


  async function closeAddHour() {
    openAddHour.value = false;
    await getBusinessHours();
  }


  async function closeEditHour() {
    openEditHour.value = false;
    await getBusinessHours();
  }


  onMounted(async () => {
    loading.value = true;
    if (await isAuthenticated.value) {
      const favRes = await fetch(`${API_URL}/api/v1/businesses/${businessId}/favorites?user=${user.value.sub}`);

      if (!favRes.ok) {
        throw new Error("Server error");
      }

      const data = await favRes.json();

      if (data.length) {
        icon.value = 'heart_check'
      }

      await getBusiness();
      await getBusinessHours();
      await getProducts();
      images.value.push(business.value);
      await getImages();
      loaded.value = true;
    } else {
      router.push('/account/login');
    }
    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <div class="my-business">
    <PageTitle>My Business</PageTitle>
    <div class="flexbox">
      <div class="flex-item">
        <Carousel v-if="loaded" :images="images"/>
        <div class="action-buttons center">
          <IconButton
            @click="$router.push(`/businesses/${businessId}/images`)"
            icon="gallery_thumbnail"
            color="solid">Manage images</IconButton>
        </div>
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
                @click="openDialog = !openDialog"
                icon="share"
                color="accent"
              >Share</IconButton>
              <IconButton
                @click="$router.push(`/businesses/${businessId}/edit`)"
                icon="edit"
                color="accent"
              />
              <IconButton @click="confirmDeleteBusiness = true" icon="delete" color="accent"/>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div class="collapsible-container">
      <Collapsible leadingIcon="date_range" title="Business Hours">
        <section>
          <div class="action-buttons center">
            <IconButton
              @click="openAddHour = true"
              icon="add"
              color="solid-accent">Add business hour</IconButton>
          </div>
          <div v-if="hours.length" class="card-container">
            <HourCard
              v-for="hour in hours"
              :day="hour.day"
              :opens_at="hour.opens_at"
              :closes_at="hour.closes_at"
              @click="openEditBusinessHour(hour)"
            />
          </div>
          <div v-else class="info-message">
            <span class="material-symbols-outlined">lightbulb</span>
              No business hour added.
            <br>
            Click on the "Add business hour" button above to add a business hour.
          </div>
        </section>
      </Collapsible>
      <Collapsible leadingIcon="local_mall" title="Products" :isOpen="true">
        <section>
          <div class="action-buttons center">
            <IconButton
              @click="$router.push(`/businesses/${businessId}/products/add`)"
              icon="add"
              color="solid-accent">Add product &nbsp</IconButton>
          </div>
          <div v-if="products.length" class="card-container">
            <ProductCard
              @click="$router.push(`/businesses/${businessId}/products/${product.id}`)"
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
              No product added.
            <br>
            Click on the "Add product" button above to add a product
            to your business.
          </div>
        </section>
      </Collapsible>
    </div>
    <div v-if="openAddHour" class="dialog">
      <AddHourDialog :businessId="businessId" @close="closeAddHour"/>
    </div>
    <div v-if="openEditHour" class="dialog">
      <EditHourDialog :hour="hour" @close="closeEditHour"/>
    </div>
    <div v-if="confirmDeleteBusiness" class="dialog">
      <div class="dialog-container">
        <div class="dialog-title">Confirm</div>
        <div>
          Are you sure you want to delete this business?
          <br> <br>
          This operation cannot be undone.
        </div>
        <div class="dialog-action-buttons">
          <button type="button" @click="confirmDeleteBusiness = false">Cancel</button>
          <button type="button" @click="deleteBusiness">Delete forever</button>
        </div>
      </div>
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
