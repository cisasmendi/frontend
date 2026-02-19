<script>
    import BoardLayout from "$BoardLayout";
    export let title = "";
</script>

<BoardLayout imageUrl={"/assets/otros/biblioteca.jpg"} {title}>
    <div class="mt-4">
        <h3 class="text-xl font-semibold text-[#6d0205]">Misión</h3>
        <p>
            La Biblioteca tiene como misión gestionar, preservar y organizar el
            acervo bibliográfico de la Facultad en un entorno de información en
            continua evolución, para contribuir al aprendizaje, la investigación
            y la innovación en la Universidad, mediante estrategias y servicios
            de excelencia que promuevan la generación y transferencia del
            conocimiento.
        </p>
    </div>

    <div class="mt-4">
        <h3 class="text-xl font-semibold text-[#6d0205]">Visión</h3>
        <ul class="list-disc list-inside">
            <li>
                Apoyo a la institución en el cumplimiento de sus objetivos y
                metas organizacionales.
            </li>
            <li>
                Generación de espacios adecuados para el estudio y el trabajo
                individual o en grupo.
            </li>
            <li>
                Gestión, preservación y acceso eficaz de las colecciones y de la
                producción científica y académica de la Facultad y de la
                Universidad.
            </li>
            <li>
                Poner en marcha servicios innovadores que apoyen a los
                estudiantes en su formación integral y a los profesores e
                investigadores en todo el proceso de creación del conocimiento.
            </li>
            <li>
                Lograr una gestión excelente con recursos humanos proactivos y
                competentes.
            </li>
        </ul>
    </div>

    <div class="mt-4">
        <h3 class="text-xl font-semibold text-[#6d0205]">
            Horario de Atención
        </h3>
        <p>De 7:15 a 12:45 y a la tarde desde las 15:15 hasta las 20:45.</p>
    </div>

    <div class="mt-4">
        <h3 class="text-xl font-semibold text-[#6d0205]">Contacto</h3>
        <p>
            Correo electrónico: <a
                href="mailto:biblioteca@eco.unca.edu.ar"
                class="text-blue-500">biblioteca@eco.unca.edu.ar</a
            >
        </p>
        <p>Teléfono: +54 383 4424099 interno 159</p>
    </div>

    <section>
        <h3 class="text-xl font-semibold text-[#6d0205] pt-4">
            ¿Dónde Estamos?
        </h3>
        <div class="mt-4 flex justify-center">
            <!-- svelte-ignore a11y-missing-attribute -->
            <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d721.6268617811295!2d-65.78390717082085!3d-28.459822998905377!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjjCsDI3JzM1LjQiUyA2NcKwNDcnMDAuMSJX!5e1!3m2!1ses-419!2sar!4v1551971186802"
                frameborder="0"
                class="w-full h-80 sm:w-3/4 lg:w-2/3"
            ></iframe>
        </div>
    </section>
</BoardLayout>
