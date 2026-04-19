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
    {#if title == "Formación Continua"}
      <div class="w-full p-4">
        <h2 class="text-2xl font-bold text-[#6d0205]">Formación Continua</h2>
        <br>
        <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-6">
          <div class="flex flex-col">
            <ContinuingEducation title="Cursos de Posgrado" />
          </div>
          <div class="flex flex-col">
            <ContinuingEducation title="Diplomaturas" />
          </div>
          <div class="flex flex-col">
            <ContinuingEducation title="Talleres"/>
          </div>
        </div>
      </div>
    {/if}
  {/if}
</main>
