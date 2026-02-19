<script>
    import PdfReader from "$utilsMain/PdfView.svelte";
    import BoardLayout from "$BoardLayout";

    let url = "";

    export let items = [       
        {
            title: "Contador Público",
            Files: [
                {
                    subtitle: "Contador publico 1er año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 1º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 2do año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 2º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 3er año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 3º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 4to año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 4º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 5to año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 5º CP-LADM.pdf",
                },
                {
                    subtitle: "REEDICION Y OPTATIVAS",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - REEDICION.pdf",
                },
            ],
        },
        {
            title: "Licenciatura en Administración",
            Files: [
                {
                    subtitle: "Licenciatura en administracion 1er año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 1º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 2do año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 2º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 3er año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 3º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 4to año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 4º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 5to año",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 5º CP-LADM.pdf",
                },
                {
                    subtitle: "REEDICION Y OPTATIVAS",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - REEDICION.pdf",
                },
            ],
        },
        {
            title: "Licenciatura en Gestión en Educación Superior",
            Files: [
                {
                    subtitle:
                        "Licenciatura en gestion en educacion superior COHORTE VIII-IX-X",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - LGES VIII-IX-X COHORTE.pdf",
                },
            ],
        },
        {
            title: "Licenciatura en Gestión en Publica",
            Files: [
                {
                    subtitle: "Licenciatura en gestion publica COHORTE VIII-IX-X",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026  - LGP VIII-IX-X COHORTE .pdf",
                },
            ],
        },
        {
            title: "Tecnicatura en Administración de Educación Superior (DISTANCIA)",
            Files: [
                {
                    subtitle:
                    "Tecnicatura en administracion de educacion superior",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 -  TAES.pdf",
                },
            ],
        },
        {
            title: "Tecnicatura Universitaria en Administración Pública",
            Files: [
                {
                    subtitle:
                        "Tecnicatura universitaria en administracion publica FIAMBALA",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUAP 2026 - FIAMBALA.pdf",
                },
            ],
        },
        {
            title: "Tecnicatura Universitaria en Contabilidad",
            Files: [
                {
                    subtitle: "Tecnicatura universitaria en Contabilidad",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUC.pdf",
                },
            ],
        },
        {
            title: "Tecnicatura Universitaria en Administración de la Comercialización Digital",
            Files: [
                {
                    subtitle: "Tecnicatura universitaria en Administración de la Comercialización Digital",
                    url: "/assets/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUACD.pdf",
                },
            ],
        },
    ];

    function handleClick(file) {
        url = file.url;
    }
    function handleBack() {
        url = "";
    }

    function descargarPdf(pdfUrl) {
        const link = document.createElement("a");
        link.href = pdfUrl;
        link.download = pdfUrl.split("/").pop(); // Usa el nombre del archivo para la descarga
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
</script>

<BoardLayout title={"Horarios de Clases - Primer Cuatrimestre 2026"}>
    {#if url !== ""}
        <div>
            <button
                on:click={handleBack}
                class="bg-[#6d0205] text-white py-2 px-4 rounded mb-4"
            >
                Atras
            </button>
            <PdfReader {url} />
        </div>
    {:else}
        <div class="p-4">
            {#each items as item}
                <h3 class="text-lg font-bold text-[#6d0205] mb-2">
                    {item.title} 
                </h3>
                {#if item.Files}
                    <ul class="list-disc ml-4 mb-4">
                        {#each item.Files as file}
                            <li class="flex items-center gap-2">
                                <!-- svelte-ignore a11y_invalid_attribute -->
                                <a
                                    href={file.url}
                                    target="_blank"
                                    class="text-[#555555] hover:text-[#942c2e] cursor-pointer"
                                    aria-label="Ver archivo {file.subtitle}"
                                >
                                    {file.subtitle}
                                </a>

                                <button
                                    on:click={() => handleClick(file)}
                                    class="cursor-zoom-in flex items-center gap-1"
                                    aria-label="Ver archivo"
                                >
                                    <svg
                                        class="w-5 h-5"
                                        fill="none"
                                        stroke="currentColor"
                                        viewBox="0 0 24 24"
                                    >
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            stroke-width="2"
                                            d="M15 10l4.94 4.94a3 3 0 01-4.24 4.24L10 15m5-5L9 4m6 6l6 6"
                                        ></path>
                                    </svg>
                                    Ver
                                </button>

                                <button
                                    on:click={() => descargarPdf(file.url)}
                                    class="cursor-pointer flex items-center gap-1"
                                    aria-label="Descargar archivo"
                                >
                                    <svg
                                        class="w-5 h-5"
                                        fill="none"
                                        stroke="currentColor"
                                        viewBox="0 0 24 24"
                                    >
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            stroke-width="2"
                                            d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2M8 12l4 4m0 0l4-4m-4 4V4"
                                        ></path>
                                    </svg>
                                    Descargar
                                </button>
                            </li>
                        {/each}
                    </ul>
                {/if}
            {/each}
        </div>
    {/if}
</BoardLayout>
