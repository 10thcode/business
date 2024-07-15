<template>
  <div class="loading">
    <img src="https://ik.imagekit.io/prezzgh/invoice/loading.gif?updatedAt=1718501627657" alt="Loading">
  </div>
</template>

<style scoped>
  .loading {
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    width: 100%;
    background: var(--dialog-background); 
    z-index: 9999;
  }

  img {
    width: 100px;
    height: auto;
  }
</style>
