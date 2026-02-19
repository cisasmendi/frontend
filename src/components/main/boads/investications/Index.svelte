<script>
  import Menu from "../../utils/Menu.svelte";
  import SecretariaDeInvestigacionYTransferencia from "./views/SecretariaDeInvestigacionYTransferencia.svelte";
  import InstitutoDeInvestigacionEnContabilidad from "./views/UnidadesDeInvestigacion/InstitutoDeInvestigacionEnContabilidad.svelte";
  import InstitutoDeInvestigacionEnEconomiaYFinanzas from "./views/UnidadesDeInvestigacion/InstitutoDeInvetigaciónEnEconomíaYFinanzas.svelte";
  import InstitutoDeInvestigacionEnAdministracion from "./views/UnidadesDeInvestigacion/InstitutodeinvestigaciónenAdministración.svelte";

  import QuienesSomos from "./views/UnidadesDeInvestigacion/InstitutodeInvestigaciónEstadoyPolíticasPúblicas/QuienesSomos.svelte";
  import CatedraAbierta from "./views/UnidadesDeInvestigacion/InstitutodeInvestigaciónEstadoyPolíticasPúblicas/CatedraAbierta.svelte";

  import UnidadesDeVinvulacionYTransferencia from "./views/UnidadesDeVinvulacionYTransferencia.svelte";
  import ActividadesDeInvestigacionInnovacionYTransferencia from "./views/ActividadesDeInvestigacionInnovacionYTransferencia.svelte";
  import Investigadores from "./views/Investigadores.svelte";
  import Proyectos from "./views/Proyectos/Proyectos.svelte";

  import EnContruccion from "../../utils/ComponeteEnContruccion.svelte";
  import InstitutoDeInvestigacionEnEStadisticaYDemografia from "./views/UnidadesDeInvestigacion/InstitutoDeInvestigacionEnEStadisticaYDemografia.svelte";

  let menuItems = [
    "Secretaría de Investigación, Innovación y Transferencia",
    {
      title: "Unidades de Investigación",
      submenu: [
        "Instituto de investigación en Contabilidad",
        "Instituto de investigación en Economía y Finanzas",
        "Instituto de investigación en Administración",
        "Instituto de Estadística y Demografía",

        {
          title: "Instituto de investigación en Estado y Políticas Públicas",
          submenu: [
            "Quienes somos",
            "Cátedra abierta",
            //    {
            //      title: "Proyectos",
            //      submenu: [
            //       "Investigación y Desarrollo",
            //        "Investigación y Tecnología",
            //         "Extensión",
            //      ],
            //    },
         //   "Publicaciones",
          ],
        },
      ],
    },
    "Unidad de Vinculación y Transferencia",
   // "Actividades de Investigación, Innovación y Transferencia",
    //   "Investigadores",
    "Proyectos",
  ];

  let imageUrl = "https://via.placeholder.com/400";
  let title = "Secretaría de Investigación, Innovación y Transferencia";

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
  <Menu {menuItems} on:click={handleClick} expand={true} />
  {#if title === "Secretaría de Investigación, Innovación y Transferencia"}
    <SecretariaDeInvestigacionYTransferencia
      title={"Investigación | Secretaría de Investigación"}
    />
  {/if}
  {#if title === "Instituto de investigación en Contabilidad"}
    <InstitutoDeInvestigacionEnContabilidad
      title={"Instituto de Investigación en Contabilidad"}
    />
  {/if}
  {#if title === "Quienes somos"}
    <QuienesSomos
      title={"Instituto de Investigación en Estado y Políticas Públicas"}
      imageUrl={"/assets/logos/LogoIIEyPP.png"}
    />
  {/if}
  {#if title === "Cátedra abierta"}
    <CatedraAbierta
      title={"Instituto de Investigación en Estado y Políticas Públicas"}
      imageUrl={"/assets/logos/LogoIIEyPP.png"}
    />
  {/if}

  {#if title === "Unidad de Vinculación y Transferencia"}
    <UnidadesDeVinvulacionYTransferencia
      title={"Unidad de Vinculación y Transferencia"}
    />
  {/if}

  {#if title === "Instituto de Estadística y Demografía"}
    <InstitutoDeInvestigacionEnEStadisticaYDemografia
      title={"Instituto de Investigación en Estadística y Demografía"}
    />
  {/if}

  {#if title === "Proyectos"}
    <Proyectos title={"Proyectos de Investigación"} />
  {/if}

  {#if title === "Instituto de investigación en Economía y Finanzas"}
    <InstitutoDeInvestigacionEnEconomiaYFinanzas
      title={"Instituto de Investigación en Economía y Finanzas"}
    />
  {/if}

  {#if title === "Instituto de investigación en Administración"}
    <InstitutoDeInvestigacionEnAdministracion
      title={"Instituto de Investigación en Administración"}
    />
  {/if}

  {#if title === "Investigadores"}
    <Investigadores title={"Investigadores"} />
  {/if}

  {#if title === "Actividades de Investigación, Innovación y Transferencia"}
    <ActividadesDeInvestigacionInnovacionYTransferencia
      title={"Actividades de Investigación, Innovación y Transferencia"}
    />
  {/if}

  {#if title === "Publicaciones"}
    <EnContruccion title={"Publicaciones"} />
  {/if}

  {#if title === "Eventos"}
    <EnContruccion title={"Eventos"} />
  {/if}

  {#if title === "Recursos"}
    <EnContruccion title={"Recursos"} />
  {/if}
</main>
