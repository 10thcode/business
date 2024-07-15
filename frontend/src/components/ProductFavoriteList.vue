<script setup>
  import {ref, onMounted} from 'vue';
  import ProductCard from '../components/ProductCard.vue';
  import { useAuth0 } from '@auth0/auth0-vue';
  import Loading from "../components/Loading.vue";


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0()
  const products = ref([]);
  const loading = ref(true);


  onMounted(async () => {
    loading.value = true;
    if (await isAuthenticated.value) {
      const response = await fetch(`${API_URL}/api/v1/users/${user.value.sub}/favorites/products`);

      if (!response.ok) {
        throw new Error("Server error");
      }

      products.value = await response.json();
    }
    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <section class="my-businesses-section">
    <div v-if="products.length" class="card-container">
      <ProductCard
        @click="$router.push(`explore/businesses/${product.business}/products/${product.id}`)"
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
        No product added to favorite list.
      <br>
      Click on the ♡ icon of a product to add it to your favorite list.
    </div>
  </section>
</template>
