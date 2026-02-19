<script>
  import Menu from "../../utils/Menu.svelte";
  import SecreteriaDeExtension from "./views/SecreteriaDeExtension.svelte";
  import ActividadesCulturalesYDeportivas from "./views/ActividadesCulturalesYDeportivas.svelte";
  import ProgramaDeExtension from "./views/ProgramaDeExtension.svelte";
  import ProyectosDeExtension from "./views/ProyectosDeExtension.svelte";
  import ConvocatoriasProyectosDeExtension from "./views/ConvocatoriasProyectosDeExtension.svelte";
  import Pasantias from "./views/Pasantias.svelte";


  let menuItems = [
    "Secretaría de Extensión",
    "Actividades Culturales y Deportivas",
    "Programa de Extensión",
    "Proyectos de Extensión",
    "Convocatorias Proyectos de Extensión",
    "Pasantías",
  ];

  let imageUrl = "https://via.placeholder.com/400";
  let title = "Secretaría de Extensión";
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
  {#if title === "Secretaría de Extensión"}
    <SecreteriaDeExtension
      title={"Secretaría de Extensión"}  
    />
  {/if} 
  {#if title === "Actividades Culturales y Deportivas"}
    <ActividadesCulturalesYDeportivas
      title={"Actividades Culturales y Deportivas"}  
    />
  {/if} 
  {#if title === "Programa de Extensión"}
    <ProgramaDeExtension
      title={"Programa de Extensión"}  
    />
  {/if} 
  {#if title === "Proyectos de Extensión"}
    <ProyectosDeExtension
      title={"Proyectos de Extensión"}  
    />
  {/if} 
  {#if title === "Convocatorias Proyectos de Extensión"}
    <ConvocatoriasProyectosDeExtension
      title={"Convocatorias Proyectos de Extensión"}  
    />
  {/if} 
  {#if title === "Pasantías"}
    <Pasantias
      title={"Pasantías"}  
    />
  {/if}
</main>
