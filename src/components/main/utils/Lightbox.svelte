<script>
  export let showLightbox = false;
  export let closeLightbox;
</script>

{#if showLightbox}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
  <!-- svelte-ignore a11y_interactive_supports_focus -->
  <div
    class="lightbox fixed inset-0 flex justify-center items-center z-50"
    role="dialog"
    aria-modal="true"
    on:click={closeLightbox}
  >
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class="lightbox-content" on:click|stopPropagation>
      <slot></slot>

      <!-- Botón de cerrar -->
      <button
        class="absolute top-2 right-2 bg-red-600 rounded-full w-12 h-12 flex justify-center items-center shadow-lg cursor-pointer z-20 hover:bg-red-500 transition"
        aria-label="Cerrar"
        on:click={closeLightbox}
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="w-5 h-5 text-white"
        >
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>
  </div>
{/if}

<style>
 .lightbox {
  background: rgba(70, 28, 28, 0.6); /* Fondo oscuro con transparencia */
  backdrop-filter: blur(8px); /* Difumina el fondo */
}

.lightbox-content {
  min-width: 50%;
  max-width: 50%;
  background: rgba(255, 255, 255, 0.8); /* Fondo blanco semitransparente */
  border-radius: 10px; /* Más redondeo */
  overflow: hidden; /* Para que el contenido respete las esquinas */
  box-shadow: 10 8px 32px rgba(255, 255, 255, 0.2); /* Sombra suave */
  backdrop-filter: blur(12px); /* Difuminado interno */
  transition:
    transform 0.3s ease,
    opacity 0.3s ease;
  position: relative;
}

/* Full screen monitor styles */
@media (min-width: 1200px) {
  .lightbox-content {
    min-width: 40%;
    max-width: 40%;
  }
}

@media (max-width: 800px) {
  .lightbox-content {
    min-width: 95%;
    border-radius: 16px;
  }
  .lightbox {
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(10px);
  }
}

</style>
