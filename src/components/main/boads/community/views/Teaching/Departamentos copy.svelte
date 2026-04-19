<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";
    // @ts-ignore
    import Accordion from "$utilsMain/Accordion.svelte";
</script>

<BoardLayout title="Departamentos">
    <div class="w-full">
        <!-- Sección Departamentos -->
        <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Departamentos</h3>

        <h4 class="text-lg font-semibold pt-2">Funciones y Competencias</h4>
        <p>
            El Departamento es una Unidad Académica cuyo eje de funcionamiento
            está centrado en el desarrollo disciplinar. Constituye el ámbito de
            interacción académica de los docentes de una misma disciplina o de
            disciplinas afines, para el crecimiento de la ciencia, la tecnología
            y el mejoramiento de la calidad de la educación. Actualmente están
            en funcionamiento los Departamentos de Administración, Contabilidad,
            Economía y Humanística, Jurídico, Temáticas y Pedagógico;
            dependientes de la Secretaría Académica.
        </p>

        <h5 class="font-semibold pt-2">Funciones</h5>
        <ol class="list-disc pl-5">
            <li>
                Administrar y supervisar el funcionamiento de las cátedras que
                integran su Departamento, requerir a sus responsables la
                Programación Académica y las normas de funcionamiento de las
                cátedras en el marco de las disposiciones vigentes en materia
                académica.
            </li>
            <li>
                Verificar y garantizar que la Programación Académica de las
                asignaturas, cursos, módulos, seminarios u otras denominaciones,
                cumplan con las disposiciones vigentes sobre las formas de
                elaboración y presentación de la misma.
            </li>
            <li>
                Supervisar que las actividades académicas programadas sean
                orientadas a que el alumno adquiera habilidades y destrezas para
                la práctica profesional.
            </li>
            <li>
                Conducir los procesos de modificación de contenidos de las
                materias y exigir la actualización anual de la bibliografía en
                la implementación de las Programaciones Académicas. Universidad
                Nacional de Catamarca Facultad de Ciencias Económicas y de
                Administración Consejo Directivo Ordenanza. CD FCEyA. Nº
                001/2008 Expte. Nº 051/2004
            </li>
            <li>
                Supervisar y coordinar los planes de trabajo de las cátedras y
                proponer metodologías de evaluación.
            </li>
            <li>
                Planificar, proponer y, en su caso, organizar la capacitación y
                actualización científica, técnica y pedagógica del personal
                docente en coordinación con el Departamento Pedagógico de la
                Facultad.
            </li>
            <li>
                Formular los planes de trabajo del Departamento y elevarlo a
                consideración del Secretario Académico.
            </li>
            <li>
                Expedirse en toda cuestión sometida a su consideración por el
                Comité Interdepartamental.
            </li>
            <li>
                Proponer normas generales que mejoren la efectividad de los
                métodos de enseñanza, u otras específicas que resulten del
                análisis de los resultados de los informes elaborados por los
                Responsables de Cátedra, confeccionados en la oportunidad de la
                finalización del dictado de las asignaturas.
            </li>
        </ol>

        <h5 class="font-semibold pt-2">Competencias</h5>
        <ul class="list-disc pl-5">
            <li>
                Analizar, evaluar y coordinar las actividades docentes,
                pedagógicas y administrativas implicadas en el accionar de su
                área específica.
            </li>
            <li>
                Supervisar el cumplimiento de los objetivos de las asignaturas
                que conforman el departamento e integran el plan de estudio de
                las carreras de grado de la Facultad.
            </li>
            <li>
                Coordinar y articular la gestión académica intercátedra que
                aseguren los objetivos y niveles de calidad de la enseñanza en
                la Facultad, articule y garantice que se responda a los perfiles
                de los egresados definidos en el Documento Curricular de las
                Carreras de Grado de la Facultad y en los aspectos definidos en
                la programación académica de las Cátedras.
            </li>
        </ul>

        <Accordion title={"Administración"}>
            <div slot="content">
                <p>
                    <strong>Director:</strong> Dr. Rafael Marcelo Ponzo Florimonte
                </p>
                <p>
                    <strong>Sub-Director:</strong> Lic. Jorge Sebastián Degani
                </p>
                <h5 class="font-semibold">Contador Público Nacional:</h5>
                <ul class="list-disc pl-5">
                    <li>Administración Básica</li>
                    <li>Tecnología de la Administración</li>
                    <li>Administración General y Estratégica</li>
                    <li>Administración y Contabilidad Pública</li>
                    <li>Administración Financiera</li>
                    <li>Administración de Personal</li>
                    <li>Planeamiento a Largo Plazo</li>
                    <li>Organización Contable y Administrativa</li>
                </ul>
                <h5 class="font-semibold">Licenciatura en Administración:</h5>
                <ul class="list-disc pl-5">
                    <li>Administración Básica</li>
                    <li>Comportamiento Organizacional</li>
                    <li>Tecnología de la Información</li>
                    <li>Administración de Personal</li>
                    <li>Administración de la Comercialización</li>
                    <li>Administración y Contabilidad Pública</li>
                    <li>Administración Financiera</li>
                    <li>Teoría de la Decisión</li>
                    <li>Administración de Operaciones</li>
                    <li>Planeamiento a Largo Plazo</li>
                    <li>Dirección General</li>
                    <li>Políticas Públicas</li>
                    <li>Ejercicio Profesional para Administradores</li>
                    <li>Organización Contable y Administrativa</li>
                </ul>
            </div>
        </Accordion>
        <Accordion title={"Contabilidad"}>
            <div slot="content">
                <p>
                    <strong>Director:</strong> CPN Ramon Rubén Aguirre
                </p>
                <p>
                    <strong>Sub-Director:</strong> CPN Juan Marcelo Rivas
                </p>
                <h5 class="font-semibold">Contador Público Nacional:</h5>
                <ul class="list-disc pl-5">
                    <li>Contabilidad I</li>
                    <li>Contabilidad II</li>
                    <li>Contabilidad III</li>
                    <li>Contabilidad de Costos</li>
                    <li>Gestión y Costos</li>
                    <li>Contabilidad IV</li>
                    <li>Auditoría</li>
                    <li>Teoría y Técnica Impositiva I, II, III</li>
                    <li>Ejercicio Profesional para Contadores</li>
                </ul>
                <h5 class="font-semibold">Licenciatura en Administración:</h5>
                <ul class="list-disc pl-5">
                    <li>Teoría Contable</li>
                    <li>Contabilidad para Administradores</li>
                    <li>Gestión y Costos</li>
                    <li>Régimen Tributario</li>
                </ul>
            </div>
        </Accordion>
        <Accordion title={"Economía y Humanística"}>
            <div slot="content">
                <p>
                    <strong>Director:</strong> Lic. María Marta Jalil Colomé
                </p>
                <p>
                    <strong>Sub-Director:</strong> Dr. Rodolfo Ángel Vázquez
                </p>
                <h5 class="font-semibold">Contador Público Nacional:</h5>
                <ul class="list-disc pl-5">
                    <li>Microeconomía</li>
                    <li>Macroeconomía y Política Económica</li>
                    <li>Doctrinas Sociales y Económicas</li>
                    <li>Finanzas Públicas</li>
                    <li>Economía Regional y Provincial</li>
                    <li>Comercio Exterior</li>
                    <li>Introducción a la Investigación Social</li>
                </ul>
                <h5 class="font-semibold">Licenciatura en Administración:</h5>
                <ul class="list-disc pl-5">
                    <li>Microeconomía</li>
                    <li>Macroeconomía y Política Económica</li>
                    <li>Introducción a la Investigación Social</li>
                    <li>Doctrinas Sociales y Económicas</li>
                    <li>Finanzas Públicas</li>
                </ul>
            </div>
        </Accordion>

        <Accordion title={"Jurídico"}>
            <div slot="content">
                <p>
                    <strong>Director:</strong> Dr. Oscar Carrizo Safe
                </p>
                <p>
                    <strong>Sub-Director:</strong> Dr. Fernando Navarro
                </p>

                <h5 class="text-md font-semibold pt-2">
                    Contador Público Nacional
                </h5>
                <ul class="list-disc pl-5">
                    <li>Derecho Público</li>
                    <li>Derecho Civil</li>
                    <li>Derecho Comercial</li>
                    <li>Sociedades Comerciales</li>
                    <li>Derecho Laboral y Previsional</li>
                    <li>Legislación Concursal y Práctica Judicial</li>
                </ul>

                <h5 class="text-md font-semibold pt-2">
                    Licenciatura en Administración
                </h5>
                <ul class="list-disc pl-5">
                    <li>Derecho Público</li>
                    <li>Derecho Civil</li>
                    <li>Derecho Comercial</li>
                    <li>Sociedades Comerciales</li>
                </ul>
            </div>
        </Accordion>

        <Accordion title={"Matemáticas"}>
            <div slot="content">
                <p>
                    <strong>Directora:</strong> Ing. Adriana Mabel Lezana
                </p>

                <h5 class="text-md font-semibold pt-2">
                    Contador Público Nacional
                </h5>
                <ul class="list-disc pl-5">
                    <li>Matemática I</li>
                    <li>Matemática II</li>
                    <li>Matemática III</li>
                    <li>Estadística</li>
                    <li>Cálculo Financiero</li>
                    <li>Métodos Cuantitativos</li>
                </ul>

                <h5 class="text-md font-semibold pt-2">
                    Licenciatura en Administración
                </h5>
                <ul class="list-disc pl-5">
                    <li>Matemática I</li>
                    <li>Matemática II</li>
                    <li>Matemática III</li>
                    <li>Estadística</li>
                    <li>Cálculo Financiero</li>
                    <li>Técnicas Cuantitativas para Administradores</li>
                    <li>Investigación Operativa</li>
                </ul>
            </div>
        </Accordion>

        <Accordion title={"Pedagógico"}>
            <div slot="content">
                <p><strong>Directora:</strong> Lic. Marisa Rosana Juri</p>
                <p>
                    <strong>Email:</strong>
                    <a href="mailto:rosana.juri@gmail.com" class="text-blue-500"
                        >rosana.juri@gmail.com</a
                    >
                </p>
            </div>
        </Accordion>
    </div>
</BoardLayout>
