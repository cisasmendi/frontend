<script>
    import Grade from "./views/Grade.svelte";
    import Pregrade from "./views/Pregrade.svelte";

    export let title = "";
    // @ts-ignore
    import BoardLayout from "$BoardLayout";
    // @ts-ignore
    import Accordion from "$utilsMain/Accordion.svelte";
</script>

<BoardLayout {title}>
    <br /><br />

    <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-6">
        <h3 class="text-xl font-semibold text-[#6d0205] mb-2">
            Inscripciones Abiertas hasta el viernes 6 de marzo de 2026
        </h3>
        <ul class="list-disc list-inside space-y-1 text-gray-700">
            <li>Tecnicatura en Administración de la Educación Superior</li>
            <li>Licenciatura en Gestión Pública</li>
            <li>Licenciatura en Gestión de la Educación Superior</li>
        </ul>
    </div>

    <h3 class="text-xl font-semibold pt-4 text-[#6d0205]">
        Tutorial de Inscripción 2026 <a
            class="text-xl font-semibold pt-4 text-blue-600"
            href="https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/ingresantes/TUTORIAL INGRESO 2026.pdf"
            target="_blank"
        >
            Descargar tutorial
        </a>
    </h3>

    <br />
    <h3 class="text-xl font-semibold pt-4 text-[#6d0205]">
        Programa ingreso 2026 <a
            class="text-xl font-semibold pt-4 text-blue-600"
            href="https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/ingresantes/Programas Ingreso 2026.pdf"
            target="_blank"
        >
            Descargar programa
        </a>
    </h3>

    <br />
    <h3 class="text-xl font-semibold pt-4 text-[#6d0205]">
        Preinscripción 2026
        <a
            class="text-xl font-semibold pt-4 text-blue-600"
            href="https://preinscripcion.unca.edu.ar/"
            target="_blank"
        >
            Ir a la preinscripción
        </a>
    </h3>
    <br />

    <Accordion title={"CARRERAS DE Pregrado"}>
        <div slot="content">
            <Pregrade></Pregrade>
        </div>
    </Accordion>

    <Accordion title={"CARRERAS DE GRADO"}>
        <div slot="content">
            <Grade></Grade>
        </div>
    </Accordion>
</BoardLayout>
