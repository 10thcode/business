<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import PageTitle from '../components/PageTitle.vue';
  import IconButton from '../components/IconButton.vue';
  import AddBusinessReviewDialog from '../components/AddBusinessReviewDialog.vue';
  import EditBusinessReviewDialog from '../components/EditBusinessReviewDialog.vue';
  import LoginRequiredDialog from '../components/LoginRequiredDialog.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0()
  const loading = ref(true);
  const reviews = ref([]);
  const review = ref({});
  const route = useRoute();
  const businessId = route.params.businessId;
  const business = ref({});
  const openAddReview = ref(false);
  const openEditReview = ref(false);
  const openLoginRequiredDialog = ref(false);


  async function getBusiness() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    business.value = await response.json();
    loading.value = false;
  }

  async function getReviews() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/reviews`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    reviews.value = await response.json();
    loading.value = false;
  }


  async function openAddReviewDialog() {
    if (await isAuthenticated.value) {
      openAddReview.value = true;
    } else {
      openLoginRequiredDialog.value = true;
    }
  }


  async function closeAddReviewDialog() {
    openAddReview.value = false;
    await getReviews();
  }


  async function openEditReviewDialog(businessReview) {
    if (await isAuthenticated.value) {
      if (businessReview.user_id === user.value.sub) {
        review.value = businessReview;
        openEditReview.value = true;
      }
    } else {
      openLoginRequiredDialog.value = true;
    }
  }


  async function closeEditReviewDialog() {
    openEditReview.value = false;
    await getReviews();
  }


  onMounted(async () => {
    await getReviews();
    await getBusiness();
  });
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Business Reviews</PageTitle>
  <section>
    <div class="action-buttons center">
      <IconButton
        @click="openAddReviewDialog"
        icon="add"
        color="solid-accent">Add review &nbsp</IconButton>
    </div>
    <div v-if="reviews.length" class="card-container">
      <div
        @click="openEditReviewDialog(review)"
        v-for="review in reviews"
        class="small container">
        <div class="details">
          <span class="material-symbols-outlined">chat</span>
          <div class="content">
            <div class="title">{{ review.title }}</div>
            <div>{{ review.content }}</div>
            <div class="date">{{ (new Date(review.created_at)).toLocaleString() }}</div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="info-message">
      <span class="material-symbols-outlined">lightbulb</span>
        No review.
      <br>
        Be the first person to review this business.
    </div>
    <div v-if="openAddReview" class="dialog">
      <AddBusinessReviewDialog :business="business" @close="closeAddReviewDialog"/>
    </div>
    <div v-if="openEditReview" class="dialog">
      <EditBusinessReviewDialog
        :businessId="businessId"
        :review="review"
        @close="closeEditReviewDialog"/>
    </div>
    <div v-if="openLoginRequiredDialog" class="dialog">
      <LoginRequiredDialog @close="openLoginRequiredDialog = false"/>
    </div>
  </section>
</template>

<style scoped>
  .date {
    font-size: 12px;
    color: var(--faded-text);
  }
</style>
