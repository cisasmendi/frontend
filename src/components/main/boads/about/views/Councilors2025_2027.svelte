<script>
    import PdfReader from "../../../utils/PdfView.svelte";
    import BoardLayout from "$BoardLayout";
    let url = "";

    export let items = [
        {
            title: "",
            Files: [
                {
                    subtitle:
                        "Convocatoria a Elecciones y Constitución de la Junta Electoral",
                    url: "/assets/pdf/consejeros/2025-2027/ResolucionCD-FCEyA-018-25.pdf",
                },
            ],
        },
        {
            title: "Publicación de Padrones Provisorios",
            Files: [
                {
                    subtitle: "Acta N° 1",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°1.pdf",
                },
                {
                    subtitle: "Claustro Docentes",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO DOCENTE-.pdf",
                },
                {
                    subtitle: "Claustro Nodocentes",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO NO DOCENTE -.pdf",
                },
                {
                    subtitle: "Claustro Egresados",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO EGRESADOS.pdf",
                },
                {
                    subtitle: "Claustro Estudiantes Contador Público",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO ESTUDIANTE - CPN- C.P.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Administración",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO ESTUDIANTES - LICENCIATURA EN ADMINISTRACION.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Pública",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO ESTUDIANTES - LICENCIATURA EN GESTION PUBLICA.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Educación Superior",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO ESTUDIANTES - LICENCIATURA EN GESTION DE  LA EDUCACION SUPERIOR.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Tecnicatura en Administración de la Educación Superior",
                    url: "/assets/pdf/consejeros/2025-2027/PADRON PROVISORIO - CLAUSTRO ESTUDIANTES - T.A.E.S.pdf",
                },
            ],
        },
        {
            title: "Publicación de Padrones Definitivos",
            Files: [
                {
                    subtitle: "Acta N° 2",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°2.pdf",
                },
                {
                    subtitle: "Claustro Docentes",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO DOCENTE.pdf",
                },
                {
                    subtitle: "Claustro No Docentes",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO NO DOCENTE.pdf",
                },
                {
                    subtitle: "Claustro Egresados",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO EGRESADOS.pdf",
                },

                {
                    subtitle: "Claustro Estudiantes Contador Público",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO ESTUDIANTES- CONTADOR PÚBLICO NACIONAL - CONTADOR PÚBLICO.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Administración",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO ESTUDIANTES - LICENCIATURA EN ADMINISTRACIÓN.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Pública",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO ESTUDIANTES  - LICENCIATURA EN GESTIÓN PÚBLICA.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Educación Superior",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO ESTUDIANTES - LICENCIATURA EN GESTIÓN DE LA EDUCACIÓN SUPERIOR.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Tecnicatura en Administración de la Educación Superior",
                    url: "/assets/pdf/consejeros/2025-2027/PADRÓN DEFINITIVO - CLAUSTRO ESTUDIANTES -T.A.E.S.pdf",
                },
            ],
        },
        {
            title: "Plazo de Presentación de Listas de Candidatos",
            Files: [
                {
                    subtitle: "Acta N° 3",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°3..pdf",
                },
            ],
        },

        {
            title: "Exhibición de Listas",
            Files: [
                {
                    subtitle: "Acta N° 4",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°4.pdf",
                },
                {
                    subtitle: "Listado Docentes",
                    url: "/assets/pdf/consejeros/2025-2027/CLAUSTRO DOCENTE.pdf",
                },
                {
                    subtitle: "Listado Estudiantes",
                    url: "/assets/pdf/consejeros/2025-2027/CLAUSTRO ESTUDIANTES.pdf",
                },
                {
                    subtitle: "Listado Nodocentes",
                    url: "/assets/pdf/consejeros/2025-2027/CLAUSTRO NODOCENTE.pdf",
                },
                {
                    subtitle: "Listado Egresados",
                    url: "/assets/pdf/consejeros/2025-2027/CLAUSTRO EGRESADOS.pdf",
                },
            ],
        },

        {
            title: "Oficialización de Listas",
            Files: [
                {
                    subtitle: "Acta N° 5",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°5.pdf",
                },
            ],
        },

        {
            title: "Oficialización Firme de Listas de Candidatos",
            Files: [
                {
                    subtitle: "Acta N° 6",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°6.pdf",
                },
            ],
        },

        {
            title: "Fijación del Día y Hora de Elecciones",
            Files: [
                {
                    subtitle: "Acta N° 7",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°7.pdf",
                },
            ],
        },
        {
            title: "DESIGNACION PTES. MESAS Y OFICIALIZACON DE VOTOS",
            Files: [
                {
                    subtitle: "Acta N° 8",
                    url: "/assets/pdf/consejeros/2025-2027/ACTA N°8.pdf",
                },
            ],
        },
        {
            title: "ESCRUTINIO DEFINITIVO Y PROCLAMACION DE CANDIDATOS",
            Files: [
                {
                    subtitle: "CLAUSTRO NODOCENTES",
                    url: "/assets/pdf/consejeros/2025-2027/Claustro Nodocentes .pdf",
                },
                {
                    subtitle: "CLAUSTRO ESTUDIANTES",
                    url: "/assets/pdf/consejeros/2025-2027/Claustro Estudiantes .pdf",
                },
                 {
                    subtitle: "CLAUSTRO EGRESADOS",
                    url: "/assets/pdf/consejeros/2025-2027/Claustro Egresados .pdf",
                },
                 {
                    subtitle: "CLAUSTRO DOCENTES",
                    url: "/assets/pdf/consejeros/2025-2027/Claustro Docentes .pdf",
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

<BoardLayout title={"Consejeros 2025-2027"}>
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
    {/if}
</BoardLayout>
