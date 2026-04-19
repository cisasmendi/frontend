<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";

    function descargarPdf(pdfUrl) {
        const link = document.createElement("a");
        link.href = pdfUrl;
        link.download = pdfUrl.split("/").pop();
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    const examSchedules = [
        {
            title: "Turno Especial de Exámenes Finales Abril 2026",
            items: [
                {
                    label: "Examenes Especiales ABRIL 2026",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/TurnosExamenes/especiales/RESOL.096-26.pdf",
                },
            ]
        },
        {
            title: "Turno Ordinario de Exámenes Feb/Mar 2026",
            items: [
                {
                    label: "CONTADOR PÚBLICO NACIONAL - CONTADOR PÚBLICO - LICENCIATURA EN ADMINISTRACIÓN - PLANES DE ESTUDIOS: 2001 - 2018 & 2001 - 2022",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/TurnosExamenes/febrero-marzo/CP LA - FEB MAR 26.pdf",
                },
                {
                    label: "LICENCIATURA EN GESTIÓN PÚBLICA y LICENCIATURA EN GESTIÓN DE LA EDUCACIÓN SUPERIOR - PLANES DE ESTUDIOS: 2015 - 2017",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/TurnosExamenes/febrero-marzo/LGP LGES - FEB MAR 26.pdf",
                },
                {
                    label: "TECNICATURA EN ADMINISTRACIÓN DE LA EDUCACIÓN SUPERIOR (TAES) - PLAN DE ESTUDIOS: 2015",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/TurnosExamenes/febrero-marzo/TAES  - FEB MAR 2026.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN PÚBLICA (TUAP) - PLAN DE ESTUDIOS: 1999",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/TurnosExamenes/febrero-marzo/TUAP - FEB MAR 2026.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN CONTABILIDAD (TUC) TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN DE LA COMERCIALIZACIÓN DIGITAL (TUACD)",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/alumnos/TurnosExamenes/febrero-marzo/TUC TUACD - FEB MAR 2026.pdf",
                },
            ],
        },
    ];
</script>

<BoardLayout title="Turnos de Examenes">
    <!--  <div class="pt-6 pb-4 px-4 rounded-lg bg-[#ffffff] border border-[#6d0205]">
      
        <h2 class="text-2xl font-bold text-[#dd4247] flex items-center gap-2">
        
            <span>𝗘𝘅𝗮́𝗺𝗲𝗻𝗲𝘀 𝗙𝗶𝗻𝗮𝗹𝗲𝘀 - 𝗧𝘂𝗿𝗻𝗼 𝗘𝘀𝗽𝗲𝗰𝗶𝗮𝗹 𝗢𝗰𝘁𝘂𝗯𝗿𝗲 𝟮𝟬𝟮𝟱</span>
        </h2>
        <p class="mt-2 text-lg text-[#5f44f8] font-semibold">¡Atención estudiantes! Les informamos que el turno especial de exámenes finales se llevará a cabo del <span class="font-bold">09 al 17 de octubre de 2025</span>.</p>
        <div class="mt-4">
            <h3 class="text-xl font-bold text-[#070707]">𝗖𝗔𝗥𝗥𝗘𝗥𝗔𝗦:</h3>
            <ul class="list-disc pl-6 ">
                <li><span class="font-semibold">Contador Público Nacional / Contador Público / Lic. en Administración:</span></li>
                <ul class="pl-6">
                    <li>Los alumnos de <span class="font-semibold">CP (Plan de Estudios 2018)</span> que adeuden hasta <span class="font-bold">12 materias</span>.</li>
                    <li>Los alumnos de <span class="font-semibold">CPN (Plan de Estudios 2001)</span> que adeuden hasta <span class="font-bold">11 materias</span>.</li>
                    <li>Los alumnos de <span class="font-semibold">Lic. en Administración</span> que adeuden hasta <span class="font-bold">10 materias</span>.</li>
                </ul>
            </ul>
            <div class="mt-2 flex items-center gap-2">
   
                <span class=" ">𝗦𝗼𝗹𝗶𝗰𝗶𝘁𝘂𝗱 𝗱𝗲 𝗮𝗽𝗲𝗿𝘁𝘂𝗿𝗮 𝗱𝗲 𝗺𝗲𝘀𝗮:</span>
            </div>
            <p class="pl-8 ">Realizar entre el <span class="font-bold">24 y 29 de septiembre</span>, mediante nota formal en unidad alumnos de la Facultad, de lunes a viernes de <span class="font-bold">08:00 a 12:30</span> y de <span class="font-bold">15:30 a 20:30</span>.</p>
            <div class="mt-2 flex items-center gap-2">
                <span class="">𝗜𝗻𝘀𝗰𝗿𝗶𝗽𝗰𝗶𝗼́𝗻:</span>
            </div>
            <p class="pl-8 ">Una vez aprobada la apertura, podrán inscribirse los alumnos que adeuden hasta el <span class="font-bold">40% de las materias</span>:</p>
            <ul class="pl-12 ">
                <li>CP (Plan de Estudios 2018): hasta <span class="font-bold">16 materias</span>.</li>
                <li>CPN (Plan de Estudios 2001): hasta <span class="font-bold">14 materias</span>.</li>
                <li>Lic. en Administración: hasta <span class="font-bold">14 materias</span>.</li>
            </ul>
            <p class="pl-8 ">Recuerden que la inscripción cierra <span class="font-bold">48 horas hábiles antes del examen</span> (sin contar el día del examen). Se puede rendir hasta <span class="font-bold">1 materia</span>.</p>
            <h3 class="mt-4 text-xl">𝗖𝗔𝗥𝗥𝗘𝗥𝗔𝗦:</h3>
            <ul class="list-disc pl-6 ">
                <li><span class="font-semibold">Lic. en Gestión Pública / Lic. en Gestión de la Educación Superior / TAES/TUAP:</span></li>
            </ul>
            <p class="pl-8 ">La solicitud de apertura de mesa se realiza del <span class="font-bold">24 al 29 de septiembre</span> mediante nota formal en unidad alumnos.<br>Podrán presentarse a rendir hasta <span class="font-bold">2 materias</span>.</p>
        </div>
    </div>-->
    <div class="p-3 sm:p-4 md:p-6 max-w-7xl mx-auto">
        {#each examSchedules as schedule}
            <section class="mb-6 sm:mb-8">
                <h3 class="text-base sm:text-lg md:text-xl font-bold text-[#6d0205] mb-3 sm:mb-4 border-b-2 border-[#6d0205] pb-2">
                    {schedule.title}
                </h3>

                <ul class="space-y-3 sm:space-y-4">
                    {#each schedule.items as item}
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
