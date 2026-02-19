<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";

    export let title = "Área de Educación a Distancia";
    export let imageUrl = "";
</script>

<main>
    <div class="container mx-auto p-6">
        <BoardLayout {imageUrl} {title}>
            <p class="text-center text-2xl font-semibold text-blue-600 my-4">
                TU FUTURO ES HOY
            </p>
            <p class="mb-4">
                Desde la Facultad de Ciencias Económicas y de Administración, te
                ofrecemos las siguientes opciones para que puedas cursar a
                distancia utilizando nuestro campus virtual.
            </p>

            <div
                class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-6"
            >
                <a
                    href="https://eco.unca.edu.ar/taes"
                    target="_blank"
                    class="block p-4 border rounded shadow hover:shadow-lg transition"
                >
                    <h3 class="text-lg font-bold">
                        Tecnicatura en Administración de la Educación Superior
                    </h3>
                    <p class="text-gray-600 mt-2">
                        Con el secundario aprobado puedes inscribirte y cursar
                        esta Carrera que te formará para ejercer funciones de
                        administración en las Instituciones de Educación
                        Superior Universitaria y no Universitaria. +Info                        
                    </p>
                </a>
                <a
                    href="https://eco.unca.edu.ar/lgp"
                    target="_blank"
                    class="block p-4 border rounded shadow hover:shadow-lg transition"
                >
                    <h3 class="text-lg font-bold">
                        Licenciatura en Gestión Pública
                    </h3>
                    <h4 class="font-serif pt-1 pb-1">
                        Ciclo de Complementación Curricular
                    </h4>
                    <p class="text-gray-600 mt-2">
                        Puedes inscribirte en esta carrera si ya eres Técnico
                        Universitario en Administración Pública, Profesor de
                        Economía, Contabilidad o Ciencia Política, o profesional
                        con título a fin a la Carrera. + Info
                    </p>
                </a>
                <a
                    href="https://eco.unca.edu.ar/lges"
                    target="_blank"
                    class="block p-4 border rounded shadow hover:shadow-lg transition"
                >
                    <h3 class="text-lg font-bold">
                        Licenciatura en Gestión de la Educación Superior
                    </h3>
                    <h4 class="font-serif pt-1 pb-1">
                        Ciclo de Complementación Curricular
                    </h4>
                    <p class="text-gray-600 mt-2">
                        Si ya eres TAES o Profesor de cualquier
                        disciplina puedes inscribirte y cursar la
                        carrera desde la comodidad de tu casa. + Info
                    </p>
                </a>
            </div>
            <ul class="list-disc pl-6 mt-6 space-y-2">
                <li>
                    Para poder cursar, es necesario contar con una computadora
                    con acceso a internet.
                </li>
                <li>
                    Todas las materias incluyen encuentros con los docentes en
                    tiempo real a través de videoconferencias.
                </li>
                <li>
                    Se brinda apoyo administrativo y técnico durante toda la
                    cursada.
                </li>
                <li>Las carreras son aranceladas.</li>
                <li>
                    Ya estamos recolectando datos de los interesados a través de
                    los formularios de inscripción para cada carrera.
                </li>
                <li>
                    Toda la información académica y los formularios están
                    disponibles en nuestro sitio web.
                </li>
            </ul>
            <h2 class="text-xl font-semibold text-[#6d0205] pt-10">
                Coordinadora
            </h2>
            <div
                class="bg-white shadow-md rounded-lg p-4 flex flex-col items-center text-center max-w-[60%] mx-auto"
            >
                <!-- Contenido de la tarjeta -->
                <h2 class="text-lg font-semibold text-gray-900">
                    Mg. Ing. Rosana Juri
                </h2>
                <p class="text-sm text-gray-600 mt-1">
                    Responsable del Área de Educación a Distancia
                </p>
            </div>
        </BoardLayout>
    </div>
</main>

<style>
    .bg-white {
        margin-top: 1rem; /* Espacio para la imagen */
    }
</style>
