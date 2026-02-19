<script>
  import Offer from "./views/offer/Index.svelte";
  import ContinuingEducation from "./views/ContinuingEducation/Index.svelte";
  import Contact from "./views/Contact.svelte";
  let title = "Contacto";
  let show = true;
  function handleClick(e) {
    title = e.detail;
    if (title !== null) {
      show = true;
    } else {
      show = false;
    }
  }
</script>

<main class=" mx-auto flex flex-col lg:flex-row w-full lg:w-auto">
  <Offer show={!show} on:click={handleClick}></Offer>
  {#if show}
    {#if title == "Contacto"}
      <Contact />
    {/if}
    {#if title == "Cursos de Posgrado"}
      <ContinuingEducation {title} />
    {/if}
    {#if title == "Diplomaturas"}
      <ContinuingEducation {title} />
    {/if}
    {#if title == "Talleres"}
      <ContinuingEducation {title} />
    {/if}
  {/if}
</main>
