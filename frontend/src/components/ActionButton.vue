<template>
    <div class="fab">
      <div class="fab-text">Create business</div>
      <span class="fab-icon material-symbols-outlined">business</span>
    </div>
</template>

<style scoped>
  .fab {
    background: linear-gradient(63deg, rgba(0,255,255,0.3) 0%, rgba(0,144,255,0.8) 50%, rgba(255,0,238,0.5) 100%);
    color: white;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    gap: 8px;
    justify-content: center;
    padding: 10px 0;
    border-radius: 12px;
    align-items: center;
    width: 100%;
  }

  .fab-icon {
    margin: 16px 0;
  }

  @media (min-width: 768px) {
    .fab {
      max-width: 500px;
    }
  }
</style>
