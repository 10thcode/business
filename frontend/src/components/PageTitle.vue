<template>
  <div class="page-title">
    <slot />
  </div>
</template>

<style scoped>
  .page-title {
    background: white;
    position: sticky;
    top: 0;
    font-weight: 300;
    padding: 16px;
    font-size: 24px;
    border-bottom: 1px solid var(--outline);
  }

  @media (min-width: 640px) {
    .page-title {
      padding: 16px 32px;
    }
  }

  @media (min-width: 768px) {
    .page-title {
      padding: 16px 64px;
    }
  }

  @media (min-width: 1024px) {
    .page-title {
      padding: 16px 128px;
    }
  }
</style>
