<script>
    import PdfReader from "$utilsMain/PdfView.svelte";
    import BoardLayout from "$BoardLayout";
    let url = "";
/*
    export let items = [
        {
            title: "",
            Files: [
              
            ],
        },
        {
            title: "Publicación de Padrones Provisorios",
            Files: [
                
            ],
        },
        {
            title: "Publicación de Padrones Definitivos",
            Files: [],
        },

        {
            title: "Exhibición de Listas",
            Files: [],
        },
        {
            title: "Fijación del Día y Hora de Elecciones",
            Files: [],
        },

        {
            title: "Oficialización de Votos",
            Files: [],
        },
        {
            title: "Acta de Escrutinio Definitivo y Proclamacion de Candidatos",
            Files: [],
        },

        {
            title: "",
            Files: [],
        },
    ];*/

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

<BoardLayout title={"Elecciones Centro de Estudiantes"}>
    <!--
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
                                <span
                                    class="text-[#555555]"
                                    aria-label={`Ver archivo ${file.subtitle}`}
                                >
                                    {file.subtitle}
                                </span>

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
    {/if}-->
</BoardLayout>
