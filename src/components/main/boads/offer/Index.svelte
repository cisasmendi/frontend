<script>
  // @ts-ignore
  import Menu from "$utilsMain/Menu.svelte";
  import { title } from "./stores/offerstore";
  import { onMount } from "svelte";
  // @ts-ignore
  import AcademicProgram from "$utilsMain/AcademicProgram/Index.svelte";

  //let title = "Contador Público Nacional";

  // Imports de componentes
  import Comp_ContadorPublicoNacional from "./views/grade/Tables/Contador Público Nacional.svelte";
  import Comp_ContadorPublico from "./views/grade/Tables/Contador Público.svelte";
  import Comp_LicenciaturaenAdministracion2022 from "./views/grade/Tables/Licenciatura en Administración 2022.svelte";
  import Comp_LicenciaturaenAdministracion from "./views/grade/Tables/Licenciatura en Administración.svelte";
  import Comp_LicenciaturaenGestiondelaEducacionSuperior from "./views/grade/Tables/Licenciatura en Gestión de la Educación Superior.svelte";
  import Comp_LicenciaturaenGestionPublica from "./views/grade/Tables/Licenciatura en Gestión Pública.svelte";
  import Comp_TecnicaturaenAdministracindelaEducacinSuperior from "./views/pregrade/Tables/Tecnicatura en Administración de la Educación Superior.svelte";
  import Comp_TecnicaturaUniversitariaenAdministracinPublica from "./views/pregrade/Tables/Tecnicatura Universitaria en Administración Pública.svelte";
  import Comp_TecnicaturaUniversitariaenContabilidad from "./views/pregrade/Tables/Tecnicatura Universitaria en Contabilidad.svelte";
  import Comp_TecnicaturaUniversitariaenAdministracióndelaComercializaciónDigital from "./views/pregrade/Tables/Tecnicatura Universitaria en Administración de la Comercialización Digital.svelte";

  // Import del JSON predeterminado
  import json_ContadorPublicoNacional from "./views/grade/Contador Público Nacional.json";

  let programInfo = json_ContadorPublicoNacional;

  // Cargar automáticamente todos los archivos JSON en la carpeta `grade` y `pregrade`
  let programFiles = {
    ...import.meta.glob("./views/grade/*.json"),
    ...import.meta.glob("./views/pregrade/*.json"),
  };

  export let search;

  onMount(async () => {
    if (search !== undefined) {
      $title = search;
    }
    promesa = loadProgram($title);
    selected = reload($title);
  });

  let menuItems = [
    {
      title: "Grado",
      submenu: [
        "Contador Público Nacional",
        "Contador Público",
        "Licenciatura en Administración",
        "Licenciatura en Administración 2022",
        "Licenciatura en Gestión Pública",
        "Licenciatura en Gestión de la Educación Superior",
      ],
    },
    {
      title: "Pre-grado",
      submenu: [
        "Tecnicatura Universitaria en Administración Pública",
        "Tecnicatura en Administración de la Educación Superior",
        "Tecnicatura Universitaria en Contabilidad",
        "Tecnicatura Universitaria en Administración de la Comercialización Digital",
      ],
    },
  ];

  let options = [
    {
      id: "Contador Público Nacional",
      component: Comp_ContadorPublicoNacional,
    },
    { id: "Contador Público", component: Comp_ContadorPublico },
    {
      id: "Licenciatura en Administración",
      component: Comp_LicenciaturaenAdministracion,
    },
    {
      id: "Licenciatura en Administración 2022",
      component: Comp_LicenciaturaenAdministracion2022,
    },
    {
      id: "Licenciatura en Gestión de la Educación Superior",
      component: Comp_LicenciaturaenGestiondelaEducacionSuperior,
    },
    {
      id: "Licenciatura en Gestión Pública",
      component: Comp_LicenciaturaenGestionPublica,
    },
    {
      id: "Tecnicatura en Administración de la Educación Superior",
      component: Comp_TecnicaturaenAdministracindelaEducacinSuperior,
    },
    {
      id: "Tecnicatura Universitaria en Administración Pública",
      component: Comp_TecnicaturaUniversitariaenAdministracinPublica,
    },
    {
      id: "Tecnicatura Universitaria en Contabilidad",
      component: Comp_TecnicaturaUniversitariaenContabilidad,
    },
    {
      id: "Tecnicatura Universitaria en Administración de la Comercialización Digital",
      component:
        Comp_TecnicaturaUniversitariaenAdministracióndelaComercializaciónDigital,
    },
  ];

  async function loadProgram(programName) {
    const programKey = `./views/grade/${programName}.json`;
    const programKeyPregrade = `./views/pregrade/${programName}.json`;
    if (programFiles[programKey]) {
      const program = await programFiles[programKey]();
      // @ts-ignore
      programInfo = program.default;
    } else if (programFiles[programKeyPregrade]) {
      const program = await programFiles[programKeyPregrade]();
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
    promesa = loadProgram($title);
    selected = reload($title);
  }

  async function reload(title) {
    const valor = options.find((Element) => Element.id === title);
    return valor;
  }

  let promesa = loadProgram($title);
  let selected = reload($title);
</script>

<main class="mx-auto flex flex-col lg:flex-row w-full lg:w-auto">
  <Menu {menuItems} on:click={handleClick} />
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
</main>
