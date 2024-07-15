<script setup>
  defineProps(["color", "icon", "type"])
</script>

<template>
  <button :class="color" :type="type">
    <span class="material-symbols-outlined">{{ icon }}</span>
    <slot />
  </button>
</template>

<style scoped>
  button {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 16px;
    border-radius: 100px;
    font-weight: 700;
    letter-spacing: 0.5px;
    cursor: pointer;
    background: none;
  }

  .accent {
    border: 1px solid var(--accent);
    color: var(--accent);
  }

  .solid-accent {
    background: var(--accent);
    color: white;
  }

  .solid {
    border: 1px solid var(--accent);
    background: white;
    color: var(--accent);
  }

  .white {
    border: 1px solid white;
    color: white;
  }
</style>
