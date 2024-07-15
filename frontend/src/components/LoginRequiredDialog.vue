<template>
  <div class="dialog-container">
    <div class="dialog-title">Login required!</div>
    <div class="dialog-message">
      You must log in to access this feature.
    </div>
    <div class="dialog-action-buttons">
      <button type="button" @click="$emit('close')">Not now</button>
      <button type="button" @click="$router.push('/account/login')">Login</button>
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
