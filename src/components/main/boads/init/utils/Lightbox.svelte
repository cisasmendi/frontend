<script>
  export let showLightbox = false;
  export let closeLightbox;

  let expanded = false;

  function toggleReadMore() {
    expanded = !expanded;
  }
</script>

{#if showLightbox}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="lightbox-overlay" on:click={closeLightbox}>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class="lightbox-content" on:click|stopPropagation>
      <slot></slot>
    </div>

    <!-- Botón de cerrar -->
    <button class="close-button" on:click={closeLightbox}>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="icon"
      >
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
  </div>
{/if}

<style>
  .lightbox-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
  }

  .lightbox-content {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    width: 90%;
    max-width: 600px;
    position: relative;
    z-index: 10000;
  }

  .close-button {
    position: relative;
    top: 0px;
    right: 0px;
    background-color: white;
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    z-index: 10001;
  }

  .close-button .icon {
    width: 20px;
    height: 20px;
  }

  .close-button:hover {
    background-color: #f0f0f0;
  }
</style>
