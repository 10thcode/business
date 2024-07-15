<script setup>

</script>

<template>
  <div class="error">
    <div class="header">
      <div class="error-icon">
        <span class="material-symbols-outlined">error</span>
      </div>
      <div class="title">Error</div>
    </div>
    <div class="content">
      <div>
        An unexpected error occured.
        Please try again later. If the issue persist after trying for some time,
        please contact the developer or report the issue on
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
