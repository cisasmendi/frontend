<script>
    import { onMount } from "svelte";
    import Menu from "../../utils/Menu.svelte";
    import Incoming from "./views/Incoming/Index.svelte";
    import Graduate from "./views/Graduate/Index.svelte";
    import NonTeaching from "./views/NonTeaching/NonTeaching.svelte";
    import Conevinio from "./views/NonTeaching/Conevinio.svelte";
    import Apunca from "./views/NonTeaching/Apunca.svelte";

    import GeneralDocentes from "./views/Teaching/General.svelte";
    import CarreraDocente from "./views/Teaching/CarreraDocente.svelte";
    import Concursos from "./views/Teaching/Concursos.svelte";
    import Departamentos from "./views/Teaching/Departamentos.svelte";
    import MovilidadDocente from "./views/Teaching/MovilidadDocente.svelte";

    import GeneralAlumnos from "./views/Student/General.svelte";
    import GuiaDeTramites from "./views/Student/GuíadeTrámites.svelte";
    import HorariosDeClases from "./views/Student/HorariosDeClases.svelte";
    import Turnos from "./views/Student/Turnos.svelte";
    import MovilidadEstudiante from "./views/Student/Movilidad.svelte";
    import CentroDeEstudiantes from "./views/Student/CentroDeEstudiantes.svelte";
    import EleccionesCentrodeEstudiantes from "./views/Student/EleccionesCentrodeEstudiantes.svelte";

    let menuItems = [
        "Ingresantes",
        {
            title: "Alumnos",
            submenu: [
                "General Alumnos",
                "Guía de Trámites",
                "Horarios de Clases",
                "Turnos de Exámenes",
                "Centro de Estudiantes",
                "Elecciones Centro de Estudiantes",
                "Movilidad Estudiantil",
            ],
        },
        "Graduados",
        {
            title: "Docentes",
            submenu: [
                "General Docentes",
                "Departamentos",
                "Carrera Docente",
                "Concursos",
                "Movilidad Docente",
            ],
        },
        {
            title: "No Docentes",
            submenu: [
                "Capacitaciones",
                "Convenio Colectivo de Trabajo FATUN",
                "APUNCA",
            ],
        },
    ];

    let imageUrl = "https://via.placeholder.com/400";
    export let title = "Ingresantes";

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

    export let id;

    const list_id_offer = [
        { id: "I", title: "Ingresantes" },
        { id: "turnos", title: "Turnos de Exámenes" },       
        { id: "HC", title: "Horarios de Clases" },        
        { id: "Concursos", title: "Concursos" },
        { id: "MovilidadEstudiante", title: "Movilidad Estudiantil" },
        { id: "CentroDeEstudiantes", title: "Centro de Estudiantes" },
        { id: "EleccionesCentrodeEstudiantes", title: "Elecciones Centro de Estudiantes" },
        { id: "GeneralAlumnos", title: "General Alumnos" },
        { id: "GuiaDeTramites", title: "Guía de Trámites" },
        { id: "Graduados", title: "Graduados" },
        { id: "Capacitaciones", title: "Capacitaciones" },
        { id: "Conevinio", title: "Convenio Colectivo de Trabajo FATUN" },
        { id: "APUNCA", title: "APUNCA" },
        { id: "GeneralDocentes", title: "General Docentes" },
        { id: "CarreraDocente", title: "Carrera Docente" },
        { id: "Departamentos", title: "Departamentos" },
        { id: "MovilidadDocente", title: "Movilidad Docente" },    
    ];

    onMount(() => {
        if (id !== undefined) {
            let id_ = list_id_offer.find((element) => element.id === id);
            if (id_ !== undefined) {
                title = id_.title;
            }
        }
    });
</script>

<main class=" mx-auto flex flex-col lg:flex-row w-full lg:w-auto">
    <Menu {menuItems} on:click={handleClick} />
    {#if title === "Ingresantes"}
        <Incoming title={"Ingresantes"} />
    {/if}
    {#if title === "Graduados"}
        <Graduate />
    {/if}
    {#if title === "Capacitaciones"}
        <NonTeaching title={"Capacitación | No docentes"} />
    {/if}
    {#if title === "Convenio Colectivo de Trabajo FATUN"}
        <Conevinio title={"Convenio Colectivo de Trabajo FATUN"} />
    {/if}
    {#if title === "APUNCA"}
        <Apunca />
    {/if}
    {#if title === "General Docentes"}
        <GeneralDocentes />
    {/if}
    {#if title === "Carrera Docente"}
        <CarreraDocente />
    {/if}
    {#if title === "Concursos"}
        <Concursos />
    {/if}
    {#if title === "Departamentos"}
        <Departamentos />
    {/if}
    {#if title === "Movilidad Docente"}
        <MovilidadDocente />
    {/if}

    {#if title === "General Alumnos"}
        <GeneralAlumnos />
    {/if}
    {#if title === "Guía de Trámites"}
        <GuiaDeTramites />
    {/if}
    {#if title === "Horarios de Clases"}
        <HorariosDeClases />
    {/if}
    {#if title === "Turnos de Exámenes"}
        <Turnos />
    {/if}
    {#if title === "Movilidad Estudiantil"}
        <MovilidadEstudiante />
    {/if}
    {#if title === "Centro de Estudiantes"}
        <CentroDeEstudiantes />
    {/if}
    {#if title === "Elecciones Centro de Estudiantes"}
        <EleccionesCentrodeEstudiantes />
    {/if}

</main>
