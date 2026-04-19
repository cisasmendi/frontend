<script>
  // @ts-ignore
  import Menu from "$utilsMain/Menu.svelte";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();
  import { title } from "./stores/offerstore";
  import { onMount } from "svelte";
  // @ts-ignore
  import AcademicProgram from "$utilsMain/AcademicProgram/Index.svelte";

  // Imports de componentes

  import Comp_EspecializaciónenAdministraciónyGestióndelEstado from "./views/postgrade/tables/Especialización en Administración y Gestión del Estado.svelte";
  import Comp_EspecializaciónenContabilidadSuperioryAuditoría from "./views/postgrade/tables/Especialización en Contabilidad Superior y Auditoría.svelte";
  import Comp_EspecializaciónenTributación from "./views/postgrade/tables/Especialización en Tributación.svelte";
  import Comp_MaestríaenContabilidadSuperioryAuditoría from "./views/postgrade/tables/Maestría en Contabilidad Superior y Auditoría.svelte";
  import Comp_DoctoradoenCienciasEconómicas from "./views/postgrade/tables/Doctorado Regional en Ciencias Económicas.svelte";
  // Import del JSON predeterminado
  import json_EAGE from "./views/postgrade/Especialización en Administración y Gestión del Estado (EAGE).json";

  let programInfo = json_EAGE;

  // Cargar automáticamente todos los archivos JSON en la carpeta `grade` y `pregrade`
  let programFiles = {
    ...import.meta.glob("./views/postgrade/*.json"),
  };

  export let search = undefined;
  export let show = true;
  let expand = true;
  const Posgrado = {
    title: "Carreras De Posgrado",
    submenu: [
      "Doctorado en Ciencias Económicas",
      "Maestría en Contabilidad Superior y Auditoría (MCSA)",
      "Especialización en Contabilidad Superior y Auditoría (ECSA)",
      "Especialización en Tributación (ETRI)",
      "Especialización en Administración y Gestión del Estado (EAGE)",
    ],
  };

  let actrivarMain = false;

  onMount(() => {
    if (search !== undefined) {
      $title = search;
      expand = true;
      menuItems = [Posgrado];
      actrivarMain = true;
    }
    promesa = loadProgram($title);
    selected = reload($title);
  });

  let menuItems = [
    "Contacto",
     "Formación Continua",     
    Posgrado,
  ];

  let options = [
    {
      id: "Doctorado en Ciencias Económicas",
      component: Comp_DoctoradoenCienciasEconómicas,
    },
    {
      id: "Especialización en Administración y Gestión del Estado (EAGE)",
      component: Comp_EspecializaciónenAdministraciónyGestióndelEstado,
    },
    {
      id: "Especialización en Contabilidad Superior y Auditoría (ECSA)",
      component: Comp_EspecializaciónenContabilidadSuperioryAuditoría,
    },
    {
      id: "Especialización en Tributación (ETRI)",
      component: Comp_EspecializaciónenTributación,
    },
    {
      id: "Maestría en Contabilidad Superior y Auditoría (MCSA)",
      component: Comp_MaestríaenContabilidadSuperioryAuditoría,
    },
  ];

  async function loadProgram(programName) {
    const programKey = `./views/postgrade/${programName}.json`;
    if (programFiles[programKey]) {
      const program = await programFiles[programKey]();
      // @ts-ignore
      programInfo = program.default;
    } else {
      programInfo = null;
    }
    return programInfo;
  }

  function handleClick(event) {
    let typedat = typeof event.detail;
    if (typedat === "object") {
      $title = event.detail.submenu[0];
    }
    if (typedat === "string") {
      $title = event.detail;
    }
    // buscar el la lista de opciones el componente que corresponde al título si esta en la lista de opciones
    if (options.find((Element) => Element.id === $title)) {
      promesa = loadProgram($title);
      selected = reload($title);
      show = true;
      dispatch("click", null);
    } else {
      show = false;
      dispatch("click", $title);
    }
  }

  async function reload(title) {
    const valor = options.find((Element) => Element.id === title);
    return valor;
  }

  let promesa = loadProgram($title);
  let selected = reload($title);
</script>

{#if actrivarMain}
  <main
    class={actrivarMain
      ? "mx-auto flex flex-col lg:flex-row w-full lg:w-auto"
      : ""}
  >
    <Menu {expand} {menuItems} on:click={handleClick} />
    {#if show}
      {#await promesa}
        <p>Cargando...</p>
      {:then programInfo}
        <AcademicProgram {programInfo}>
          <div slot="plan">
            {#await selected}
              <p>Cargando...</p>
            {:then selected}
              <svelte:component this={selected.component} />
            {/await}
          </div>
        </AcademicProgram>
      {/await}
    {/if}
  </main>
{:else}
  <Menu {expand} {menuItems} on:click={handleClick} />
  {#if show}
    {#await promesa}
      <p>Cargando...</p>
    {:then programInfo}
      <AcademicProgram {programInfo}>
        <div slot="plan">
          {#await selected}
            <p>Cargando...</p>
          {:then selected}
            <svelte:component this={selected.component} />
          {/await}
        </div>
      </AcademicProgram>
    {/await}
  {/if}
{/if}
