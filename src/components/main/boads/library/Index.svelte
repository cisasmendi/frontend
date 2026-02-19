<script>
  
  import Menu from "../../utils/Menu.svelte";
  import PreguntasFrecuentes from "./views/PreguntasFrecuentes.svelte";
  import LaBiblioteca from "./views/LaBiblioteca.svelte";
  import RevistasEletronicas from "./views/RevistasEletronicas.svelte";
  import GuiaDeAccesoAlCatalogo from "./views/GuiaDeAccesoAlCatalogo.svelte";
  import CatalogoUncaKoha from "./views/CatalogoUncaKoha.svelte";
  import Suscripciones from "./views/Suscripciones.svelte";


  let menuItems = [
    "La Biblioteca",
    "Preguntas Frecuentes",
    "Revistas Electrónicas",
    "Guia de Acceso al catálogo",
    "Catálogo Unca Koha",
    "Suscripciones",
  ];

  let imageUrl = "https://via.placeholder.com/400";
  let title = "La Biblioteca";
  function handleClick(item) {
    // si el item es un submenu, entonces  mostrar el primer item del submenu
    if (typeof item.detail === "object") {
      // si el item es un submenu de segundo nivel, entonces  mostrar el primer item del submenu
      if (typeof item.detail.submenu[0] === "object") {
        title = item.detail.submenu[0].submenu[0];
      } else {
        title = item.detail.submenu[0];
      }
    } else {
      title = item.detail;
    }
  }
</script>

<main class=" mx-auto flex flex-col lg:flex-row w-full lg:w-auto">
  <Menu {menuItems} on:click={handleClick} />
  {#if title === "La Biblioteca"}
    <LaBiblioteca title={"La Biblioteca"} />
  {/if}
  {#if title === "Preguntas Frecuentes"}
    <PreguntasFrecuentes title={"Preguntas Frecuentes"}/>
  {/if}
  {#if title === "Revistas Electrónicas"}
    <RevistasEletronicas title={"Revistas Electrónicas"}/>
  {/if}
  {#if title === "Guia de Acceso al catálogo"}
    <GuiaDeAccesoAlCatalogo title={"Guia de Acceso al catálogo"}/>
  {/if}
  {#if title === "Catálogo Unca Koha"}
    <CatalogoUncaKoha />
  {/if}
  {#if title === "Suscripciones"}
    <Suscripciones title={"Suscripciones"}/>
  {/if}
 
</main>
