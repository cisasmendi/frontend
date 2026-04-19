<script>
    import { onMount } from "svelte";
    import Offer from "../offer/Index.svelte";
    import Postgraduate from "../postgraduate/views/offer/Index.svelte";
    import ContinuingEducation from "../postgraduate/views/ContinuingEducation/IndexQuery.svelte";
    import { title } from "../offer/stores/offerstore";

    export let id;
    let search = undefined;

    const list_offers = [
        { id: "grado", title: "Grado" },
        { id: "ciclo-complementacion", title: "Ciclo de Complementación" },
        { id: "pre-grado", title: "Pre-grado" },
    ];

    const list_id_offer = [
        { id: "cpn", title: "Contador Público Nacional" },
        { id: "cp", title: "Contador Público" },
        { id: "la", title: "Licenciatura en Administración" },
        { id: "ladm2022", title: "Licenciatura en Administración 2022" },
        { id: "lgp", title: "Licenciatura en Gestión Pública" },
        {
            id: "lges",
            title: "Licenciatura en Gestión de la Educación Superior",
        },
        {
            id: "tuap",
            title: "Tecnicatura Universitaria en Administración Pública",
        },
        {
            id: "taes",
            title: "Tecnicatura en Administración de la Educación Superior",
        },
        { id: "tucc", title: "Tecnicatura Universitaria en Contabilidad" },
        {
            id: "tuacd",
            title: "Tecnicatura Universitaria en Administración de la Comercialización Digital",
        },
    ];

    const list_id_postgraduate = [
        {
            id: "drce",
            title: "Doctorado en Ciencias Económicas",
        },
        {
            id: "eage",
            title: "Especialización en Administración y Gestión del Estado (EAGE)",
        },
        {
            id: "ecsa",
            title: "Especialización en Contabilidad Superior y Auditoría (ECSA)",
        },
        {
            id: "etri",
            title: "Especialización en Tributación (ETRI)",
        },
        {
            id: "mcsa",
            title: "Maestría en Contabilidad Superior y Auditoría (MCSA)",
        },
    ];

    const list_id_diplomatura = [
        {
            id: "db",
            modulo: 10,
            courseTitle: "Diplomatura en Bibliotecología",
            title: "Diplomaturas",
        },
        {
            id: "dgts",
            modulo: 11,
            courseTitle: "Diplomatura en Gestión Turística Sustentable",
            title: "Diplomaturas",
        },
    ];

    const list_id_taller = [
        {
            id: "tesis",
            modulo: 11,
            courseTitle: "Taller de Tesis",
            title: "Talleres",
        },
    ];

    const list_id_cursos_postgrado = [
        /*  {
            id: "cce",
            modulo: -12,
            courseTitle: "Taller de Elaboración del Trabajo Final",
            title: "Cursos de Posgrado",
        },*/
        {
            id: "tftp",
            modulo: 9,
            courseTitle:
                "Formación y Empleo en Tecnologías de Datos: Descubre Power BI",
            title: "Cursos de Posgrado",
        },
        {
            id: "catysipce",
            modulo: 10,
            courseTitle:
                "Ciclo de Actualización de Tecnología y Seguridad de la Información para Profesionales en Ciencias Económicas",
            title: "Cursos de Posgrado",
        },
        {
            id: "faep",
            modulo: 11,
            courseTitle: "Formulación, Análisis y Evaluación de Proyectos",
            title: "Cursos de Posgrado",
        },
        {
            id: "ttfp",
            modulo: 13,
            courseTitle: "Taller Trabajo Final de Posgrado",
            title: "Cursos de Posgrado",
        },
        {
            id: "dsmlpce",
            modulo: 14,
            courseTitle:
                "Data Science y Machine Learning para Profesionales de Ciencias Económicas",
            title: "Cursos de Posgrado",
        },
        {
            id: "mi",
            modulo: 15,
            courseTitle: "METODOLOGÍA DE LA INVESTIGACIÓN 1",
            title: "Cursos de Posgrado",
        },
        {
            id: "vyadpbi",
            modulo: 16,
            courseTitle: "Visualización y Análisis de Datos con Power BI",
            title: "Cursos de Posgrado",
        },
        {
            id: "power-bi",
            modulo: 16,
            courseTitle: "Visualización y Análisis de Datos con Power BI",
            title: "Cursos de Posgrado",
        },
        {
            id: "valuacion-determinacion-resultados",
            modulo: 17,
            courseTitle:
                "CUESTIONES ESPECIALES DE VALUACIÓN Y DETERMINACIÓN DE RESULTADOS",
            title: "Cursos de Posgrado",
        },
        {
            id: "auditoria-estados-contables",
            modulo: 18,
            courseTitle: "AUDITORÍA DE ESTADOS CONTABLES",
            title: "Cursos de Posgrado",
        },
        {
            id: "auditoria-control-fiscal",
            modulo: 19,
            courseTitle: "AUDITORÍA Y CONTROL FISCAL",
            title: "Cursos de Posgrado",
        },
        {
            id: "exposicion-analisis-proyeccion-informacion-contable",
            modulo: 20,
            courseTitle:
                "EXPOSICIÓN, ANÁLISIS Y PROYECCIÓN DE LA INFORMACIÓN CONTABLE",
            title: "Cursos de Posgrado",
        },
        {
            id: "historia-estructura-economica-regional",
            modulo: 21,
            courseTitle: "HISTORIA Y ESTRUCTURA ECONÓMICA REGIONAL",
            title: "Cursos de Posgrado",
        },
        {
            id: "programa-ejecutivo-comercio-exterior",
            modulo: 22,
            courseTitle: "PROGRAMA EJECUTIVO EN COMERCIO EXTERIOR",
            title: "Cursos de Posgrado",
        },
    ];

    onMount(() => {
        if (id !== undefined) {
            id = id.toLowerCase();
            let category_ = list_offers.find((element) => element.id === id);

            if (category_ !== undefined) {
                selectedCategory = category_.title;
                showOffer = true;
                return;
            }

            let id_ = list_id_offer.find((element) => element.id === id);

            if (id_ !== undefined) {
                search = id_.title;
                showOffer = true;
                return;
            }
            id_ = list_id_postgraduate.find((element) => element.id === id);
            if (id_ !== undefined) {
                search = id_.title;
                showPostgraduate = true;

                return;
            }
            id_ = list_id_diplomatura.find((element) => element.id === id);
            if (id_ !== undefined) {
                search = id_;
                showContinuingEducation = true;
                return;
            }
            id_ = list_id_cursos_postgrado.find((element) => element.id === id);
            if (id_ !== undefined) {
                search = id_;
                showContinuingEducation = true;
                return;
            }
            id_ = list_id_taller.find((element) => element.id === id);
            if (id_ !== undefined) {
                search = id_;
                showContinuingEducation = true;
                return;
            }
        }
    });

    let showOffer = false;
    let showPostgraduate = false;
    let showContinuingEducation = false;
    let selectedCategory = undefined;
</script>

{#if showOffer}
    <Offer {search} category={selectedCategory} />
{/if}
{#if showPostgraduate}
    <Postgraduate {search} />
{/if}
{#if showContinuingEducation}
    <ContinuingEducation title={search.title} course={search.modulo} />
{/if}
