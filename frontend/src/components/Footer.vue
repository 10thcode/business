<script setup>
  import { ref, onMounted } from 'vue';


  const quotes = [
    `"A great business isn't built overnight;
    it's crafted with vision and persistence."`,

    `"Success in business is not about luck;
    it's about relentless pursuit and unwavering dedication."`,

    `"Innovation distinguishes the leader from the
    follower in the business world."`,

    `"Great businesses are built on solving problems,
    not just selling products."`,

    `"The heart of any business is its people;
    nurture them, and your business will thrive."`,

    `"In business, adaptability is key.
    Embrace change and turn challenges into opportunities."`,

    `"Your business vision is the roadmap;
    passion and perseverance are the fuel."`,

    `"Customer trust is the currency of successful business;
    earn it and invest in it."`,

    `"Every setback in business is a setup for a stronger comeback."`,

    `"Successful businesses are built on the
    foundation of integrity and authenticity."`,

    `"Business growth comes from taking calculated
    risks and learning from every experience."`,

    `"Empower your team to innovate, and your business will be unstoppable."`,

    `"In business, the only limits are the ones you set for yourself.
    Dream big and go beyond."`,

    `"Persistence in the face of adversity is the hallmark
    of a true business leader."`,

    `"Great businesses don't just sell products;
    they create experiences that resonate with customers."`,

    `"Your business brand is your story; make it compelling and memorable."`,

    `"In the world of business, the best investment
    is in continuous learning and improvement."`,

    `"A successful business is a reflection of the passion and drive of its leaders."`,

    `"Innovation is not just about new ideas;
    it's about making those ideas come to life in meaningful ways."`,

    `"The journey of a thousand miles begins with a single step;
    take that step with confidence in your business endeavors."`,

    `"The journey of a thousand miles begins with a single step;
    take that step with confidence in your business endeavors."`
  ];

  const quote = ref("");

  quote.value = quotes[Math.round(Math.random() * 20)];
  setInterval(() => {
    quote.value = quotes[Math.round(Math.random() * 20)];
  }, 10000);
</script>

<template>
  <div @click="quote = quotes[Math.round(Math.random() * 20)]" class="quote">
    {{ quote }} - ChatGPT
  </div>
  <footer>
    <div class="production">BlackGenius 💀 Production</div>
    <div class="production-year">SINCE 2024</div>
  </footer>
</template>

<style scoped>
  footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 32px;
    color: white;
    background: url(https://ik.imagekit.io/prezzgh/business/hero.jpg?updatedAt=1719020717994);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }

  .production {
    font-weight: 900;
    font-size: 16px;
  }

  .production-year {
    font-weight: 300;
    font-size: 12px;
    letter-spacing: 3px;
  }
</style>
