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
    <h3 class="text-xl font-semibold pt-4 text-[#6d0205]">
        Tutorial de Inscripción 2026 <a
            class="text-xl font-semibold pt-4 text-blue-600"
            href="/assets/pdf/ingresantes/TUTORIAL INGRESO 2026.pdf"
            target="_blank"
        >
            Descargar tutorial
        </a>
    </h3>

    <br />
    <h3 class="text-xl font-semibold pt-4 text-[#6d0205]">
        Programa ingreso 2026 <a
            class="text-xl font-semibold pt-4 text-blue-600"
            href="/assets/pdf/ingresantes/Programas Ingreso 2026.pdf"
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
