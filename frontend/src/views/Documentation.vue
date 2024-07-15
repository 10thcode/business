<script setup>
  import PageTitle from '../components/PageTitle.vue';
  import IconButton from '../components/IconButton.vue';
  import AddRatingDialog from '../components/AddRatingDialog.vue';
  import Collapsible from '../components/Collapsible.vue';
  import Loading from "../components/Loading.vue";
  import { ref, onMounted } from 'vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const openAddRating = ref(false);
  const loading = ref(true);
  const ratings = ref([]);


  async function getRatings() {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/ratings`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    ratings.value = await response.json();
    loading.value = false;
  }


  async function closeDialog() {
    openAddRating.value = false;
    await getRatings();
  }


  onMounted(async () => {
    await getRatings();
  });


  setInterval(() => {
    ratings.value.push(ratings.value.shift());
  }, 5000);
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Documentation</PageTitle>
  <div class="hero">
    <div class="text-and-icon">
      <span class="material-symbols-outlined business-icon">business</span>
      <div class="hero-text">This is Business</div>
    </div>
    <div class="hero-content">
      <div>
        A simple web application that allows business
        owners to display their businesses and products to potential customers.
      </div>
      <div>
        Customers can browse and read detailed information about
        various businesses and their offerings.
      </div>
    </div>
    <div class="action-buttons">
      <IconButton
        @click="$router.push('/')"
        icon="rocket_launch"
        color="solid">Try now</IconButton>
    </div>
  </div>
  <div class="collapsible-container">
    <Collapsible leadingIcon="star_outline" title="Key Features">
      <section>
        <div class="sub-section">
          <h2>Business Owners</h2>
          <ul>
            <li>
              <strong>Business Profile Creation: </strong>
              Easily create and manage a detailed profile for your business.
            </li>
            <li>
              <strong>Product Listings: </strong>
              Showcase your products with descriptions, images,
              and other relevant details.
            </li>
            <li>
              <strong>Business Information: </strong>
              Provide essential information such as contact details,
              location, and operating hours.
            </li>
          </ul>
        </div>
        <div class="sub-section">
          <h2>Customers</h2>
          <ul>
            <li>
              <strong>Business Search: </strong>
              Find businesses by name, category, or location.
            </li>
            <li>
              <strong>Product Browsing: </strong>
              View detailed information about products offered by
              different businesses.
            </li>
            <li>
              <strong>Business Details: </strong>
              Access comprehensive profiles of businesses,
              including contact information and business hours.
            </li>
            <li>
              <strong>Favorites: </strong>
              Add businesses or products to your favorites list
              for easy access later.
            </li>
            <li>
              <strong>Reviews: </strong>
              Provide reviews for businesses and products to help
              other customers make informed decisions.
            </li>
          </ul>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="account_circle" title="User Roles">
      <section>
        <div class="sub-section">
          <h2>Business Owners</h2>
          <div>
            Business owners can create an account and log in to manage
            their business profiles and product listings.
          </div>
        </div>
        <div class="sub-section">
          <h2>Customers</h2>
          <div>
            Customers can browse the app without logging in.
            However, to add businesses or products to their
            favorites list and provide reviews, they need to log in.
          </div>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="navigation" title="Navigation Guide">
      <section>
        <div class="sub-section">
          <h2>Home Page</h2>
          <div>
            The home page provides the options to explore
            all businesses or create a new business.
            It also lists all the business you have created.
          </div>
        </div>
        <div class="sub-section">
          <h2>Explore Page</h2>
          <div>
            The explore page lists all registered businesses.
            Customers can browse through categories or use
            the search bar to find specific businesses.
          </div>
        </div>
        <div class="sub-section">
          <h2>Business Page</h2>
          <div>
            Each business has a dedicated profile page that includes:
          </div>
          <ul>
            <li>
              <strong>Business Name: </strong>
              The name of the business.
            </li>
            <li>
              <strong>Description: </strong>
              A brief description of the business and its offerings.
            </li>
            <li>
              <strong>Contact Infomation: </strong>
              Phone number, email address, and physical address.
            </li>
            <li>
              <strong>Operating Hours: </strong>
              Days and times the business is open.
            </li>
            <li>
              <strong>Product Listings: </strong>
              A list of products offered by the business,
              with descriptions and images.
            </li>
            <li>
              <strong>Favorites: </strong>
              Option to add the business to your favorites list.
            </li>
            <li>
              <strong>Reviews: </strong>
              Customer reviews of the business.
            </li>
          </ul>
        </div>
        <div class="sub-section">
          <h2>Product Page</h2>
          <div>
            Each product has its own details page that includes:
          </div>
          <ul>
            <li>
              <strong>Product Name: </strong>
              The name of the product.
            </li>
            <li>
              <strong>Description: </strong>
              A detailed description of the product.
            </li>
            <li>
              <strong>Images: </strong>
              Images showcasing the product.
            </li>
            <li>
              <strong>Favorites: </strong>
              Option to add the product to your favorites list.
            </li>
            <li>
              <strong>Reviews: </strong>
              Customer reviews of the product.
            </li>
          </ul>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="settings_suggest" title="How To Use">
      <section>
        <div class="sub-section">
          <h2>Business Owners</h2>
          <ul>
            <li>
              <strong>Sign Up: </strong>
              Create an account using the sign-up form.
            </li>
            <li>
              <strong>Log In: </strong>
              Log in to your account.
            </li>
            <li>
              <strong>Create Business Profile: </strong>
              Fill in the required fields to create your business profile.
            </li>
            <li>
              <strong>Add Products:</strong>
              Add products by providing descriptions, images, and other details.
            </li>
            <li>
              <strong>Update Infomation: </strong>
              You can update your business profile and product listings
              at any time.
            </li>
          </ul>
        </div>
        <div class="sub-section">
          <h2>Customers</h2>
          <ul>
            <li>
              <strong>Browse Businesses: </strong>
              Use the explore page or search bar to find businesses.
            </li>
            <li>
              <strong>View Business Profiles: </strong>
              Click on a business to view its detailed profile.
            </li>
            <li>
              <strong>Explore Products: </strong>
              Browse through the products listed by a business.
            </li>
            <li>
              <strong>Log In:</strong>
              Log in to your account to access additional features.
            </li>
            <li>
              <strong>Add to Favorites: </strong>
              Add businesses or products to your favorites list
              for quick access later.
            </li>
            <li>
              <strong>Provide Reviews: </strong>
              Write reviews for businesses and products to share
              your experience with other customers.
            </li>
          </ul>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="database" title="Data Management">
      <section>
        <div class="sub-section">
          <h2>Authentication</h2>
          <div>
            We use Auth0 for authentication, ensuring that your personal
            data is secure. Auth0 provides a robust and secure
            authentication mechanism, handling all aspects of user
            identity management, including secure login, logout, and
            password management.
          </div>
        </div>
        <div class="sub-section">
          <h2>Data Storage</h2>
          <div>
            For <strong>business owners</strong>, the data you provide when creating your
            business profile and adding products is stored securely in our
            database.
            <br>
            <br>
            As a <strong>customer</strong>, your personal data is required only when you
            log in to add favorites or provide reviews.
            This data is securely stored and used solely for
            authentication and personalization purposes.
          </div>
        </div>
        <div class="sub-section">
          <h2>Data Privacy</h2>
          <div>
            We are committed to protecting your personal information.
            We follow best practices in data security and comply with
            relevant data protection regulations. Your data will never
            be shared with third parties without your explicit consent.
          </div>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="code" title="Contribution Guidelines">
      <section>
        <div class="sub-section">
          <div>
            This project is open source, and we welcome
            contributions from the community. To contribute:
          </div>
          <ul>
            <li>
              <strong>Fork the Repository: </strong>
              Create a fork of the project repository on <a href="https://github.com/10thcode/business">GitHub</a>.
            </li>
            <li>
              <strong>Clone the Repository: </strong>
              Clone your forked repository to your local machine.
            </li>
            <li>
              <strong>Create a Branch: </strong>
              Create a new branch for your feature or bug fix.
            </li>
            <li>
              <strong>Make Changes: </strong>
              Implement your changes and ensure they are well-tested.
            </li>
            <li>
              <strong>Submit a Pull Request: </strong>
              Push your changes to your forked repository and submit
              a pull request to the main repository.
            </li>
          </ul>
        </div>
        <div class="sub-section">
          <h2>Contribution Guidelines</h2>
          <ul>
            <li>
              <strong>Code Quality: </strong>
              Ensure your code follows the project's coding standards and is
              properly documented.
            </li>
            <li>
              <strong>Testing: </strong>
              Write tests for your code to ensure it works correctly.
            </li>
            <li>
              <strong>Commit Messages: </strong>
              Write clear and concise commit messages that describe your changes.
            </li>
          </ul>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="person" title="About The Developer">
      <section>
        <div class="sub-section">
          <h2>Atta Badu Kwabena</h2>
          <div>
            <strong>Kwabena</strong> is passionate about creating user-friendly and
            efficient web applications to help businesses grow.
            You can read more about Kwabena at his
            <a href="https://10thcode.me"> portfolio website</a>.
          </div>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="question_mark" title="Frequently Asked Questions">
      <section>
        <div class="sub-section">
          <h2>Business Owners</h2>
          <ul>
            <li>
              <strong>How do I update my business profile? </strong>
              Log in to your account, navigate to your business profile,
              and click on the 'Edit' button to update your information.
            </li>
            <li>
              <strong>Can I add multiple products? </strong>
              Yes, you can add as many products as you like to your
              business profile.
            </li>
          </ul>
        </div>
        <div class="sub-section">
          <h2>Customers</h2>
          <ul>
            <li>
              <strong>Do I need to create an account to browse businesses? </strong>
              No, you do not need an account to browse businesses and products.
            </li>
            <li>
              <strong>Can I purchase products through the app? </strong>
              No, this app is for informational purposes only.
              You can contact businesses directly for purchases.
            </li>
            <li>
              <strong>How do I add businesses or products to my favorites? </strong>
              You need to log in to your account to add businesses
              or products to your favorites list.
            </li>
            <li>
              <strong>How do I provide reviews? </strong>
              Log in to your account, navigate to the business or
              product page, and submit your review using the provided form.
            </li>
          </ul>
        </div>
      </section>
    </Collapsible>
    <Collapsible leadingIcon="contact_support" title="Support">
      <section>
        <div class="sub-section">
          <div>
            If you have any questions or need assistance,
            please contact the developer through <a href="mailto:itsblackgenius@gmail.com.">Email</a>.
          </div>
        </div>
      </section>
    </Collapsible>
  </div>
  <div class="rating">
    <div class="section-header">Ratings</div>
    <div v-if="ratings.length" class="stars">
        <span v-for="star in ratings[0].rating" class="material-symbols-outlined">star</span>
    </div>
    <div v-if="ratings.length" class="message">
      {{ ratings[0].content }}
    </div>
    <div v-if="ratings.length" class="name">
      {{ ratings[0].name }}
    </div>
    <div class="action-buttons center">
      <IconButton
        @click="openAddRating = true"
        icon="star_half"
        color="solid">Rate this project &nbsp</IconButton>
    </div>
  </div>
  <div v-if="openAddRating" class="dialog">
    <AddRatingDialog  @close="closeDialog"/>
  </div>
</template>

<style scoped>
  .stars {
    display: flex;
    justify-content: center;
  }

  .rating {
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 32px;
    background: url("https://ik.imagekit.io/prezzgh/business/docs_hero.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    color: white;
  }

  .message {
    text-align: center;
    font-size: 20px;
    font-family: "Stara", sans-serif;
    max-width: 500px;
    margin: auto;
    white-space: pre-wrap;
  }

  .name {
    text-align: center;
    letter-spacing: 1px;
  }

  section {
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 64px;
    letter-spacing: 1px;
    max-width: 700px;
    margin: auto;
  }

  .sub-section {
    display: flex;
    flex-direction: column;
    gap: 16px;
    font-size: 16px;
    font-weight: 300;
  }

  ul {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  h2 {
    font-size: 24px;
    font-weight: 300;
  }

  .hero-content {
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
    text-align: center;
    font-size: 20px;
    font-weight: 300;
    padding: 32px;
    max-width: 700px;
  }

  .text-and-icon {
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
  }

  .business-icon {
    font-size: 70px;
  }

  .hero {
    color: white;
    display: flex;
    flex-direction: column;
    gap: 64px;
    align-items: center;
    justify-content: center;
    padding: 64px 32px;
    background: url("https://ik.imagekit.io/prezzgh/business/docs_hero.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }

  .hero-text {
    font-family: 'Stara', sans-serif;
    font-size: 64px;
    line-height: 60px;
    letter-spacing: 0px;
    text-align: center;
  }
</style>
