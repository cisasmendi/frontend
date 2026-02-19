<script>
    import News from "./news/News.svelte";
    import Presentation from "./presentations/Presentation.svelte";
    import Shortcuts from "./shortcuts/Shortcuts.svelte";
    import Youtube from "./youtube/Youtube.svelte";
    // @ts-ignore
    import Lightbox from "$utilsMain/Lightbox.svelte";

    import { onMount } from "svelte";
    let showLightbox = true;

    export let showBanner = true;

    onMount(() => {
        window.scrollTo(0, 0);
        // Recupera el tiempo de la última visualización del banner desde localStorage
        const lastSeenTime = localStorage.getItem("bannerTime");
        const ahora = new Date().getTime(); // Tiempo actual en milisegundos
        showLightbox = false;
        if (!lastSeenTime) {
            localStorage.setItem("bannerTime", ahora.toString());
            openLightbox();
            return;
        }
        const diffInMillis = ahora - parseInt(lastSeenTime);
        if (diffInMillis > 60 * 60 * 1000) {
            openLightbox();
            localStorage.setItem("bannerTime", ahora.toString());
            return;
        }
    });

    const urlImage = "/assets/ingreso/banner2026_2.jpg";

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
    <a href="/community/I">
        <img
            src={urlImage}
            alt="Logo de la Facultad de Ciencias Económicas y de Administración"
            class="w-auto h-auto"
        /></a
    >
</Lightbox>
<!--<button on:click={openLightbox}>Ver Publicación</button>-->
<main class="">
    <div class="container mx-auto p-6">
        <section class="mb-8 p-6">
            <Presentation />
        </section>
    </div>
    <div class="container mx-auto p-6">
        <h2 class="text-2xl font-semibold text-[#6d0205] pl-5">
            Accesos Directos
        </h2>
    </div>
    <section class="container mx-auto p-6">
        <Shortcuts />
    </section>
    <div></div>
    <section class=" bg-black">
        <News />
    </section>
    <div class="bg-[#d7d7d7]">
        <div class="container mx-auto p-6">
            <Youtube />
        </div>
    </div>
</main>
