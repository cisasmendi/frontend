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
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 1º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 2do año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 2º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 3er año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 3º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 4to año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 4º CP-LADM.pdf",
                },
                {
                    subtitle: "Contador publico 5to año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 5º CP-LADM.pdf",
                },
                {
                    subtitle: "REEDICION Y OPTATIVAS",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - REEDICION.pdf",
                },
            ],
        },
        {
            title: "Licenciatura en Administración",
            Files: [
                {
                    subtitle: "Licenciatura en administracion 1er año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 1º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 2do año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 2º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 3er año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 3º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 4to año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 4º CP-LADM.pdf",
                },
                {
                    subtitle: "Licenciatura en administracion 5to año",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - 5º CP-LADM.pdf",
                },
                {
                    subtitle: "REEDICION Y OPTATIVAS",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - REEDICION.pdf",
                },
            ],
        },
        {
            title: "Licenciatura en Gestión en Educación Superior",
            Files: [
                {
                    subtitle:
                        "Licenciatura en gestion en educacion superior COHORTE VIII-IX-X",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - LGES VIII-IX-X COHORTE.pdf",
                },
            ],
        },
        {
            title: "Licenciatura en Gestión en Publica",
            Files: [
                {
                    subtitle: "Licenciatura en gestion publica COHORTE VIII-IX-X",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026  - LGP VIII-IX-X COHORTE .pdf",
                },
            ],
        },
        {
            title: "Tecnicatura en Administración de Educación Superior (DISTANCIA)",
            Files: [
                {
                    subtitle:
                    "Tecnicatura en administracion de educacion superior",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 -  TAES.pdf",
                },
            ],
        },
        {
            title: "Tecnicatura Universitaria en Administración Pública",
            Files: [
                {
                    subtitle:
                        "Tecnicatura universitaria en administracion publica FIAMBALA",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUAP 2026 - FIAMBALA.pdf",
                },
            ],
        },
        {
            title: "Tecnicatura Universitaria en Contabilidad",
            Files: [
                {
                    subtitle: "Tecnicatura universitaria en Contabilidad",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUC.pdf",
                },
            ],
        },
        {
            title: "Tecnicatura Universitaria en Administración de la Comercialización Digital",
            Files: [
                {
                    subtitle: "Tecnicatura universitaria en Administración de la Comercialización Digital",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUACD.pdf",
                },
                {
                    subtitle: "Tecnicatura universitaria en Administración de la Comercialización Digital LOS ALTOS",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/horarios/2026/HORARIO CLASES 1er CUATRIMESTRE 2026 - TUACD 2026 - LOS ALTOS.pdf",
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
        <div class="p-2 sm:p-4">
            <button
                on:click={handleBack}
                class="bg-[#6d0205] text-white py-2 px-4 sm:py-3 sm:px-6 rounded-lg mb-4 hover:bg-[#8a0307] transition-colors text-sm sm:text-base flex items-center gap-2"
            >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                </svg>
                Atrás
            </button>
            <PdfReader {url} />
        </div>
    {:else}
        <div class="p-3 sm:p-4 md:p-6 max-w-7xl mx-auto">
            {#each items as item}
                <div class="mb-6 sm:mb-8">
                    <h3 class="text-base sm:text-lg md:text-xl font-bold text-[#6d0205] mb-3 sm:mb-4 border-b-2 border-[#6d0205] pb-2">
                        {item.title} 
                    </h3>
                    {#if item.Files}
                        <ul class="space-y-3 sm:space-y-4">
                            {#each item.Files as file}
                                <li class="bg-gray-50 hover:bg-gray-100 rounded-lg p-3 sm:p-4 transition-colors border border-gray-200">
                                    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                                        <!-- Nombre del archivo -->
                                        <div class="flex-1 min-w-0">
                                            <!-- svelte-ignore a11y_invalid_attribute -->
                                            <a
                                                href={file.url}
                                                target="_blank"
                                                class="text-[#555555] hover:text-[#942c2e] cursor-pointer font-medium text-sm sm:text-base block break-words"
                                                aria-label="Ver archivo {file.subtitle}"
                                            >
                                                {file.subtitle}
                                            </a>
                                        </div>

                                        <!-- Botones de acción -->
                                        <div class="flex gap-2 sm:gap-3 flex-shrink-0">
                                            <button
                                                on:click={() => handleClick(file)}
                                                class="bg-[#6d0205] hover:bg-[#8a0307] text-white px-3 py-2 sm:px-4 sm:py-2 rounded-md flex items-center gap-1.5 text-xs sm:text-sm transition-colors flex-1 sm:flex-initial justify-center"
                                                aria-label="Ver archivo"
                                            >
                                                <svg
                                                    class="w-4 h-4 sm:w-5 sm:h-5"
                                                    fill="none"
                                                    stroke="currentColor"
                                                    viewBox="0 0 24 24"
                                                >
                                                    <path
                                                        stroke-linecap="round"
                                                        stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                                                    ></path>
                                                    <path
                                                        stroke-linecap="round"
                                                        stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                                                    ></path>
                                                </svg>
                                                <span class="hidden sm:inline">Ver</span>
                                            </button>

                                            <button
                                                on:click={() => descargarPdf(file.url)}
                                                class="bg-gray-600 hover:bg-gray-700 text-white px-3 py-2 sm:px-4 sm:py-2 rounded-md flex items-center gap-1.5 text-xs sm:text-sm transition-colors flex-1 sm:flex-initial justify-center"
                                                aria-label="Descargar archivo"
                                            >
                                                <svg
                                                    class="w-4 h-4 sm:w-5 sm:h-5"
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
                                                <span class="hidden sm:inline">Descargar</span>
                                            </button>
                                        </div>
                                    </div>
                                </li>
                            {/each}
                        </ul>
                    {/if}
                </div>
            {/each}
        </div>
    {/if}
</BoardLayout>
