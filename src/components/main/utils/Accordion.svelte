<script>
  export let title = "Título por defecto";  // Valor predeterminado
  export let isOpen = false;
  export let disabled = false;

  function capitalizeFirstLetterOfEachWord(string) {
    return string
      .split(' ')
      .map(word => {
        // Mantener "y" y "o" en minúsculas, incluso si están en mayúsculas
        if (word.toLowerCase() === "y" || word.toLowerCase() === "o") {
          return word.toLowerCase();
        }
        // Mantener el texto dentro de paréntesis sin cambios
        if (word.startsWith('(') && word.endsWith(')')) {
          return word;
        }
        // Capitalizar la primera letra de las demás palabras
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
      })
      .join(' ');
  }
</script>

<style>
  .container {
    border-radius: 0.5rem;
    border: 1px solid #e0e0e0;
    background-color: white;
  }

  .toggle-button {
    font-size: 1.125rem;
    font-weight: 600;
    color: #6d0205;
    padding: 1rem 1.25rem;
    width: 100%;
    text-align: left;
    background-color: white;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
  }

  .disabled {
    color: gray;
    cursor: not-allowed;
  }

  .arrow-icon {
    margin-left: auto;
    height: 1.25rem;
    width: 1.25rem;
    transition: transform 0.2s ease-in-out;
  }

  .arrow-icon.rotated {
    transform: rotate(180deg);
  }

  .content {
    padding: 0 1.25rem 1rem;
  }
</style>

<div class="container">
  <h2 id="headingOne">
    <button
      class="toggle-button {disabled ? 'disabled' : ''}"
      type="button"
      on:click={() => { if (!disabled) isOpen = !isOpen }}
      aria-expanded={isOpen}
      aria-controls="collapseOne"
    >
      {capitalizeFirstLetterOfEachWord(title)}
      <span class="arrow-icon {isOpen ? 'rotated' : ''}">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
        </svg>
      </span>
    </button>
  </h2>

  {#if isOpen && !disabled}
    <div id="collapseOne" aria-labelledby="headingOne">
      <div class="content">
        <slot name="content">Unknown content</slot>
      </div>
    </div>
  {/if}
</div>
