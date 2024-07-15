<script setup>
  import { ref } from "vue";


  const props = defineProps(["leadingIcon", "title", "isOpen"]);
  const isOpen = ref(props.isOpen || false);
</script>

<template>
  <button @click="isOpen = !isOpen" type="button" class="collapsible-button">
    <span class="material-symbols-outlined">{{ leadingIcon }}</span>
    <div class="collapsible-title" :class="{ open: isOpen }">{{ title }}</div>
    <span class="material-symbols-outlined">
      {{ isOpen ? "expand_circle_up" : "expand_circle_down" }}
    </span>
  </button>
  <div v-show="isOpen" class="collapsible-content">
    <slot />
  </div>
</template>

<style scoped>
  button {
    cursor: pointer;
    width: 100%;
    display: flex;
    padding: 16px;
    gap: 16px;
    background: none;
    align-items: center;
    color: var(--primary);
    letter-spacing: 0.5px;
  }

  .collapsible-title {
    width: 100%;
    text-align: left;
    font-size: 16px;
  }

  .open {
    font-weight: 700;
  }

  .collapsible-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
