<script>
    export let title = "";
    import BoardLayout from "$BoardLayout";
    let imageUrl = "https://eco.unca.edu.ar/assets2/users/paginaeco/logos/IIEF.png";
    let imageUrl2 = "https://eco.unca.edu.ar/assets2/users/paginaeco/imagenes/IIEF.jpg";
    let imageUrl3 = "https://eco.unca.edu.ar/assets2/users/paginaeco/logos/logo-campus2.png";
    import Lightbox from "$utilsMain/Lightbox.svelte";

    import { onMount } from "svelte";
    let showLightbox = true;

    export let showBanner = true;

    onMount(() => {
        window.scrollTo(0, 0);
        // Recupera el tiempo de la última visualización del banner desde localStorage
        const lastSeenTime = localStorage.getItem("bannerTimeIIEF");
        const ahora = new Date().getTime(); // Tiempo actual en milisegundos
        showLightbox = true;
        if (!lastSeenTime) {
            localStorage.setItem("bannerTimeIIEF", ahora.toString());
            openLightbox();
            return;
        }
        const diffInMillis = ahora - parseInt(lastSeenTime);
        if (diffInMillis > 60 * 60 * 1000) {
            openLightbox();
            localStorage.setItem("bannerTimeIIEF", ahora.toString());
            return;
        }
    });

    const urlImage = "https://eco.unca.edu.ar/assets2/users/paginaeco/ingreso/banner2026_2.jpg";

    function openLightbox() {
        if (!showBanner) {
            return;
        }
        showLightbox = true;
    }

    function closeLightbox() {
        const today = new Date().toISOString().split("T")[0]; // Guardar solo la fecha en formato YYYY-MM-DD
        localStorage.setItem("bannerDate", today);
        showLightbox = false;
    }
</script>

<Lightbox {showLightbox} {closeLightbox}>
    <div
        class="rounded-lg p-6 shadow-md bg-[#222A59] flex flex-col md:flex-row md:items-start"
    >
        <img
            src={imageUrl3}
            alt="Logo Campus de Entrenamiento Laboral"
            class="w-40 md:w-48 h-auto"
        />
        <div class="flex-1 text-white text-center md:text-left">
            <h4 class="text-xl md:text-2xl font-semibold mb-2">
                Conocé el Campus de Entrenamiento Laboral
            </h4>
            <p class="mb-4 text-sm md:text-base">
                Accedé a capacitaciones y recursos útiles para mejorar tus
                habilidades laborales.
            </p>
            <a
                href="https://share.google/JrmqBb9c3xaCiboS4"
                target="_blank"
                class="inline-block px-5 py-2 bg-white text-[#222A59] font-semibold rounded hover:bg-gray-200 transition-colors"
            >
                Ir al Campus
            </a>
        </div>
    </div>
</Lightbox>

<BoardLayout imageUrl={imageUrl2}>
    <div
        class="rounded-lg p-6 shadow-md bg-[#222A59] flex flex-col md:flex-row items-center md:items-start gap-6 mb-6"
        slot="subbanner"
    >
        <img
            src={imageUrl3}
            alt="Logo Campus de Entrenamiento Laboral"
            class="w-40 md:w-48 h-auto"
        />
        <div class="flex-1 text-white text-center md:text-left">
            <h4 class="text-xl md:text-2xl font-semibold mb-2">
                Conocé el Campus de Entrenamiento Laboral
            </h4>
            <p class="mb-4 text-sm md:text-base">
                Accedé a capacitaciones y recursos útiles para mejorar tus
                habilidades laborales.
            </p>
            <a
                href="https://share.google/JrmqBb9c3xaCiboS4"
                target="_blank"
                class="inline-block px-5 py-2 bg-white text-[#222A59] font-semibold rounded hover:bg-gray-200 transition-colors"
            >
                Ir al Campus
            </a>
        </div>
    </div>
    <img
        src={imageUrl}
        alt="Prototipo de imagen"
        class="w-25 h-25 lg:w-25 lg:h-25 rounded-lg mb-4 float-left mr-4"
    />
    <h2 class="text-2xl font-semibold text-[#6d0205]">{title}</h2>
    <!-- Descripción del instituto -->
    <p class="mb-4">
        Tiene la misión de abordar temas vinculados con el problema económico
        entendido como las cuestiones que se relacionan con la organización de
        los recursos productivos escasos; la asignación de estos recursos entre
        sus usos alternativos; la distribución de los bienes y servicios
        producidos; el mantenimiento de una producción real y creciente y el
        análisis de la realidad en cuanto a las leyes que rijan las relaciones
        humanas que se derivan de la actividad económica.
    </p>

    <!-- Sección Autoridades -->
    <p><strong>Director:</strong> Lic. Marcelo Luis Altamirano</p>

    <!-- Sección Contacto -->
    <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Contacto</h3>
    <p>
        <strong>Email:</strong><br />
        <a class="text-blue-600" href="mailto:IIEF.FCEYA@eco.unca.edu.ar"
            >IIEF.FCEYA@eco.unca.edu.ar</a
        >
    </p>

    <p>
        <strong>Email:</strong><br />
        <a class="text-blue-600" href="mailto:IIEF@eco.unca.edu.ar"
            >IIEF@eco.unca.edu.ar</a
        >
    </p>

    <!-- Dirección del edificio -->
    <p class="mt-2">
        Edificio de Profesores, Facultad de Ciencias Económicas y de
        Administración. UNCA<br />
        Av. José Figueroa 275, San Fernando del Valle de Catamarca (4700), Catamarca,
        Argentina.
    </p>
</BoardLayout>
