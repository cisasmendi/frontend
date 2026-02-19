<script>
    export let title = "";
    import BoardLayout from "$BoardLayout";
</script>

<BoardLayout {title}>
    <!-- Descripción del instituto -->
    <p class="mb-4">
        Tiene la misión de realizar investigaciones demográficas, cuyo objetivo
        sean el estudio de fenómenos económicos- sociales, poblacionales
        vinculados con la realidad regional y nacional y de otras áreas del
        conocimiento propiciando la constitución de equipos interdisciplinarios.
    </p>

    <!-- Sección Contacto -->
    <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Contacto</h3>
    <p>
        <strong>Email:</strong><br />
        <a class="text-blue-600" href="mailto:ied@eco.unca.edu.ar"
            >ied@eco.unca.edu.ar</a
        >
    </p>

    <!-- Dirección del edificio -->
    <p class="mt-2">
        Edificio de Profesores, Facultad de Ciencias Económicas y de
        Administración. UNCA<br />
        Av. José Figueroa 275, San Fernando del Valle de Catamarca (4700), Catamarca,
        Argentina.
    </p>

    <div class="flex items-center gap-2 mt-4">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 text-blue-700"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 4v16m8-8H4"
            />
        </svg>
        <a
            href="https://iiedfaceya.unca.edu.ar/"
            target="_blank"
            rel="noopener"
            class="text-blue-700 font-black hover:underline transition-all text-lg"
        >
            Sitio web del instituto
        </a>
    </div>
</BoardLayout>
