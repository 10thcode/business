<script setup>

</script>

<template>
  <div class="error">
    <div class="header">
      <div class="error-icon">
        <span class="material-symbols-outlined">warning</span>
      </div>
      <div class="title">Not Found</div>
    </div>
    <div class="content">
      <div>
        The page you are looking for doesn't exist.
        It may have been moved or deleted.
        Please check the URL and try again.
        If you believe this is an error,
        contact the developer or report the issue on
        <a href="https://github.com/10thcode/business/issues">GitHub</a>.
      </div>
    </div>
  </div>
</template>

<style scoped>
  .error {
    display: flex;
    flex-direction: column;
    gap: 32px;
    color: var(--faded-text);
    margin: 64px;
    max-width: 400px;
  }

  .header {
     display: flex;
     gap: 16px;
     align-items: center;
  }

  .title {
    font-size: 32px;
    font-weight: 700;
  }

  .error-icon span {
    font-size: 60px;
  }

  .content {
    letter-spacing: 1px;
    font-size: 16px;
    line-height: 23px;
  }

  @media (min-width: 768px) {
      .error {
        padding-left: 64px;
      }
  }
</style>
