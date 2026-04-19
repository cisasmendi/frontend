<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";
    const urlReadmicion = "https://forms.gle/E3gZniyPAs84fgmF8";

    const documentSections = [
        {
            title: "Reglamentos",
            items: [
                {
                    label: "Reglamento de Alumnos",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/ReglamentoGeneralAlumnos.pdf",
                },
                {
                    label: "Reglamento Disciplinario",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/ReglamentoDisciplinarioAlumnos.pdf",
                },
            ],
        },
        {
            title: "Formularios",
            items: [
                {
                    label: "Certificado de Examen Parcial",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/certificado-examen-parcial.pdf",
                },
                {
                    label: "Certificado de Examen Final",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/certificado-examen-final.pdf",
                },
                {
                    label: "Postergación de Examen",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/certificadoPostergacionExamen.jpg",
                },
                {
                    label: "Inscripción de Examen",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/inscripcionExamen.jpg",
                },
                {
                    label: "Solicitud de Equivalencias",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/covid19/solicitudEquivalencias.pdf",
                },
                {
                    label: "Solicitud de Cambio de Plan CP",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/formularioSolicitudCambioPlanCP.pdf",
                },
                {
                    label: "Solicitud de Cambio de Plan LGP",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/formularioSolicitudCambioPlanLGP.pdf",
                },
                {
                    label: "Solicitud de Cambio de Plan LGES",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/formularioSolicitudCambioPlanLGES.pdf",
                },
                {
                    label: "Solicitud de Cambio de Plan LADM",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/formularioSolicitudCambioPlanLADM.pdf",
                },
                {
                    label: "Solicitud de Cambio de Plan TAES",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/formularioSolicitudCambioPlanTAES.pdf",
                },
            ],
        },
        {
            title: "Equivalencias",
            items: [
                {
                    label:
                        "Plan de Estudios LADM ordenamiento 2001 con el nuevo Plan LADM 2022",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/planEstudioLADM2001-2022.pdf",
                },
                {
                    label:
                        "Plan de Estudios CPN ordenamiento 2001 con el nuevo Plan LADM 2022",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/planEstudioCPN2001-LADM2022.pdf",
                },
                {
                    label:
                        "Plan de Estudios CPN ordenamiento 2018 con el nuevo Plan LADM 2022",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/planEstudioCPN2018-LADM2022.pdf",
                },
                {
                    label: "Tabla de equivalencia LADM 2001 a CP 2018",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/covid19/tablaEquivalenciasLADM2001-CP2018.pdf",
                },
                {
                    label: "Tabla de equivalencia LADM 2001 a CPN 2001",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/covid19/tablaEquivalenciasLADM2001-CPN2001.pdf",
                },
            ],
        },
    ];

    function descargarPdf(pdfUrl) {
        const link = document.createElement("a");
        link.href = pdfUrl;
        link.download = pdfUrl.split("/").pop();
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
</script>

<BoardLayout title="Información General | Alumnos">
    <h3 class="text-xl font-semibold text-[#6d0205] pt-4">
        Tramites Académicos
    </h3>
    los siguientes trámites académicos pueden ser realizados por los alumnos de la
    facultad a través de los formularios disponibles
    <ul class="pt-2 pl-10">
        <li class="pt-2">
            <h2>• Trámite de Pase y Baja de Matrícula</h2>
        </li>

        <li class="pt-2">
            <h2>• Solicitud Readmisión</h2>
        </li>

        <li class="pt-2">
            <h2>• Solicitud Cambio de Plan</h2>
        </li>

        <li class="pt-2">
            <h2>• Solicitud de Equivalencias Internas</h2>
        </li>

        <li class="pt-2">
            <h2>• Solicitud de Equivalencias Externas</h2>
        </li>
    </ul>
    <!-- Información Adicional -->
    <div class="pt-4">
        <p class="text-lg">
            Para más información, consulta la sección <strong
                >Alumnos → Guía de Trámites</strong
            > del Menú.
        </p>
        <p class="text-lg">
            Los formularios correspondientes se encuentran a continuación.
        </p>
    </div>
    <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Links:</h3>
    <ul class="pt-2 pl-10">
        <li>
            <a
                href={urlReadmicion}
                class="a-oscuro text-[#1c12a7]"
                target="_blank"
                ><i class="fa fa-link"></i> SOLICITUD DE READMISION
            </a>
        </li>
    </ul>
    <div class="pt-4 space-y-6 sm:space-y-8">
        {#each documentSections as section}
            <section>
                <h3 class="text-base sm:text-lg md:text-xl font-bold text-[#6d0205] mb-3 sm:mb-4 border-b-2 border-[#6d0205] pb-2">
                    {section.title}
                </h3>

                <ul class="space-y-3 sm:space-y-4">
                    {#each section.items as item}
                        <li class="bg-gray-50 hover:bg-gray-100 rounded-lg p-3 sm:p-4 transition-colors border border-gray-200">
                            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                                <div class="flex-1 min-w-0">
                                    <a
                                        class="text-[#555555] hover:text-[#942c2e] cursor-pointer font-medium text-sm sm:text-base block break-words"
                                        href={item.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                    >
                                        {item.label}
                                    </a>
                                </div>

                                <div class="flex gap-2 sm:gap-3 flex-shrink-0">
                                    <a
                                        href={item.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
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
                                    </a>

                                    <button
                                        on:click={() => descargarPdf(item.url)}
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
            </section>
        {/each}
    </div>
</BoardLayout>
