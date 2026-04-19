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
  export let category = undefined;

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
        "Licenciatura en Administración 2022"
      ],
    },
     {
      title: "Ciclo de Complementación",
      submenu: [   
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

  function normalizeText(value) {
    if (!value) return "";
    return value
      .toString()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .trim();
  }

  function toSlug(value) {
    return normalizeText(value)
      .replace(/\s+/g, "-")
      .replace(/[^a-z0-9-]/g, "");
  }

  function resolveCategoryTitle(value) {
    if (!value) return undefined;

    const normalizedValue = normalizeText(value);
    const slugValue = toSlug(value);
    const item = menuItems.find((element) => {
      const normalizedTitle = normalizeText(element.title);
      const slugTitle = toSlug(element.title);
      return normalizedTitle === normalizedValue || slugTitle === slugValue;
    });

    return item ? item.title : undefined;
  }

  function getFilteredMenuItems() {
    const titleCategory = resolveCategoryTitle(category);
    if (!titleCategory) {
      return menuItems;
    }

    return menuItems.filter((item) => item.title === titleCategory);
  }

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

  function getFilteredOptions() {
    const filteredMenus = getFilteredMenuItems();
    if (filteredMenus.length === menuItems.length) {
      return options;
    }

    const allowed = filteredMenus[0]?.submenu ?? [];
    return options.filter((item) => allowed.includes(item.id));
  }

  function ensureValidTitleForCategory() {
    const filteredMenus = getFilteredMenuItems();
    if (filteredMenus.length === 0) return;

    const allowed = filteredMenus[0].submenu;
    if (allowed.length === 0) return;

    if (!allowed.includes($title)) {
      $title = allowed[0];
    }
  }

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
    const currentOptions = getFilteredOptions();
    const valor = currentOptions.find((Element) => Element.id === title);
    return valor;
  }

  $: if (category !== undefined) {
    ensureValidTitleForCategory();
    promesa = loadProgram($title);
    selected = reload($title);
  }

  let promesa = loadProgram($title);
  let selected = reload($title);
</script>

<main class="mx-auto flex flex-col lg:flex-row w-full lg:w-auto">
  <Menu
    menuItems={getFilteredMenuItems()}
    expand={Boolean(resolveCategoryTitle(category))}
    on:click={handleClick}
  />
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
