<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";

    const examSchedules = [
        {
            title: "Turno Ordinario de Exámenes Feb/Mar 2026",
            items: [
                {
                    label: "CONTADOR PÚBLICO NACIONAL - CONTADOR PÚBLICO - LICENCIATURA EN ADMINISTRACIÓN - PLANES DE ESTUDIOS: 2001 - 2018 & 2001 - 2022",
                    url: "/assets/pdf/alumnos/TurnosExamenes/febrero-marzo/CP LA - FEB MAR 26.pdf",
                },
                {
                    label: "LICENCIATURA EN GESTIÓN PÚBLICA y LICENCIATURA EN GESTIÓN DE LA EDUCACIÓN SUPERIOR - PLANES DE ESTUDIOS: 2015 - 2017",
                    url: "/assets/pdf/alumnos/TurnosExamenes/febrero-marzo/LGP LGES - FEB MAR 26.pdf",
                },
                {
                    label: "TECNICATURA EN ADMINISTRACIÓN DE LA EDUCACIÓN SUPERIOR (TAES) - PLAN DE ESTUDIOS: 2015",
                    url: "/assets/pdf/alumnos/TurnosExamenes/febrero-marzo/TAES  - FEB MAR 2026.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN PÚBLICA (TUAP) - PLAN DE ESTUDIOS: 1999",
                    url: "/assets/pdf/alumnos/TurnosExamenes/febrero-marzo/TUAP - FEB MAR 2026.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN CONTABILIDAD (TUC) TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN DE LA COMERCIALIZACIÓN DIGITAL (TUACD)",
                    url: "/assets/pdf/alumnos/TurnosExamenes/febrero-marzo/TUC TUACD - FEB MAR 2026.pdf",
                },
            ],
        },

 {
            title: "Turno Ordinario de Exámenes Nov/ dic 2025",
            items: [
                {
                    label: "CONTADOR PÚBLICO NACIONAL - CONTADOR PÚBLICO - PLANES DE ESTUDIOS: 2001 - 2018 & LICENCIATURA EN ADMINISTRACION - PLANES DE ESTUDIOS: 2001 - 2022",
                    url: "/assets/pdf/alumnos/TurnosExamenes/noviembre-diciembre2025/CP LA - NOV DIC 25.pdf",
                },
                {
                    label: "LICENCIATURA EN GESTIÓN PÚBLICA y LICENCIATURA EN GESTIÓN DE LA EDUCACÍON SUPERIOR - PLANES DE ESTUDIOS: 2015 - 2017",
                    url: "/assets/pdf/alumnos/TurnosExamenes/noviembre-diciembre2025/LGP LGES - NOV DIC 25.pdf",
                },
                {
                    label: "TECNICATURA EN ADMINISTRACION DE LA EDUCACION SUPERIOR (TAES) - PLAN DE ESTUDIOS: 2015",
                    url: "/assets/pdf/alumnos/TurnosExamenes/noviembre-diciembre2025/TAES  - NOV DIC 2025.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN PÚBLICA (TUAP) - PLAN DE ESTUDIOS: 1999",
                    url: "/assets/pdf/alumnos/TurnosExamenes/noviembre-diciembre2025/TUAP - NOV DIC 2025.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN CONTABILIDAD (TUC) TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN DE LA COMERCIALIZACIÓN DIGITAL (TUACD)",
                    url: "/assets/pdf/alumnos/TurnosExamenes/noviembre-diciembre2025/TUC TUACD - NOV DIC 2025.pdf",
                },
            ],
        },

        {
            title: "Turno de Exámenes Especiales Octubre 2025",
            items: [
                {
                    label: "Examenes Especiales Octubre 2025",
                    url: "/assets/pdf/alumnos/TurnosExamenes/Examenes Especiales OCTUBRE.2025.pdf",
                },
            ],
        },
        {
            title: "Turno Ordinario de Exámenes Jul/Ago 2025",
            items: [
                {
                    label: "CONTADOR PÚBLICO NACIONAL - CONTADOR PÚBLICO - PLANES DE ESTUDIOS: 2001 - 2018",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/CP LA - Jul Ago 25-1.pdf",
                },
                {
                    label: "LICENCIATURA EN ADMINISTRACIÓN - PLANES DE ESTUDIOS: 2001 - 2022",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/CP LA - Jul Ago 25-2.pdf",
                },
                {
                    label: "LICENCIATURA EN GESTIÓN PÚBLICA - PLANES DE ESTUDIOS: 2015 - 2017",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/LGP LGES - Jul Ago 25-1.pdf",
                },
                {
                    label: "LICENCIATURA EN GESTIÓN DE LA EDUCACIÓN SUPERIOR - PLANES DE ESTUDIOS: 2015 - 2017",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/LGP LGES - Jul Ago 25-2.pdf",
                },
                {
                    label: "TECNICATURA EN ADMINISTRACIÓN DE LA EDUCACIÓN SUPERIOR (TAES) - PLAN DE ESTUDIOS: 2015",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/TAES  - Jul Ago 25.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN PÚBLICA (TUAP)  - PLAN DE ESTUDIOS: 1999 SEDE BELEN",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/TUAP - Jul Ago 25-1.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN PÚBLICA (TUAP)  - PLAN DE ESTUDIOS: 1999 SEDE LOS ALTOS",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/TUAP - Jul Ago 25-2.pdf",
                },
                {
                    label: "TECNICATURA UNIVERSITARIA EN CONTABILIDAD (TUC) TECNICATURA UNIVERSITARIA EN ADMINISTRACIÓN DE LA COMERCIALIZACIÓN DIGITAL (TUACD)",
                    url: "/assets/pdf/alumnos/TurnosExamenes/julio-agosto/TUC TUACD - Jul Ago 25.pdf",
                },
            ],
        },
        {
            title: "Turno de Exámenes Especiales ABRIL 2025",
            items: [
                {
                    label: "Examenes Especiales ABRIL 2025",
                    url: "/assets/pdf/alumnos/TurnosExamenes/Examenes Especiales ABRIL.2025.pdf",
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
    {#each examSchedules as schedule}
        <h3 class="text-xl font-semibold text-[#6d0205] pt-4">
            {schedule.title}
        </h3>
        <ul class="pt-2 pl-10">
            {#each schedule.items as item}
                <li class="pt-2">
                    <a
                        class="text-xl font-semibold pt-4"
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        {item.label}
                    </a>
                </li>
            {/each}
        </ul>
    {/each}
</BoardLayout>
