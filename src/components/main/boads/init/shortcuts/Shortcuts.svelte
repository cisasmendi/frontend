<script>
    const host = import.meta.env.VITE_HOST;
    
    // Configuración simplificada
    export let numberOfCopies = 4;
    
    const slides = [
        {
            href: `${host}/community/HC`,
            target: "_self",
            src: "/assets/shortcuts/Grises/icono-horarios-clase-gris.png",
            alt: "Horarios de clase",
            text: "Horarios de clase",
            class: "w-16 h-16 mb-2",
        },
        {
            href: `${host}/assets/pdf/calendarioacademico2026.pdf`,
            target: "_blank",
            src: "/assets/shortcuts/Grises/CalendarioAcademico.png",
            alt: "Calendario Académico",
            text: "Calendario Académico",
            class: "w-16 h-16 mb-2",
        },
        {
            href: `${host}/community/turnos`,
            target: "_self",
            src: "/assets/shortcuts/Grises/icono-examenes-gris.png",
            alt: "Fechas de exámenes",
            text: "Fechas de exámenes",
            class: "w-16 h-16 mb-2",
        },
        {
            href: `${host}/postgraduate`,
            target: "_self",
            src: "/assets/shortcuts/Grises/Cursos-Diplomaturas.png",
            alt: "Cursos y diplomaturas",
            text: "Cursos y diplomaturas",
            class: "w-16 h-16 mb-2",
        },
        {
            href: `${host}/library`,
            target: "_self",
            src: "/assets/shortcuts/Grises/Biblioteca.png",
            alt: "Biblioteca",
            text: "Biblioteca",
            class: "w-16 h-16 mb-2",
        },
        {
            href: `${host}/assets/pdf/ResMinisterial3400-2017EstandaresAcreditacionCarreraCPN.pdf`,
            target: "_blank",
            src: "/assets/shortcuts/Grises/CONEAU.png",
            alt: "CONEAU",
            text: "CONEAU",
            class: "w-16 h-16 mb-2",
        },

        {
            href: "http://cvar.sicytar.mincyt.gob.ar/auth/index.jsp",
            target: "_blank",
            src: "/assets/shortcuts/Grises/SICYTar.png",
            alt: "SICYTar",
            text: "SICYTar",
            class: "w-16 h-16 mb-2",
        },
        {
            href: "https://guarani.unca.edu.ar/",
            target: "_blank",
            src: "/assets/shortcuts/Grises/SiuGuarani.png",
            alt: "Siu Guaraní",
            text: "Siu Guaraní",
            class: "w-16 h-16 mb-2",
        },
        {
            href: "https://www.economicasvirtual.edu.ar/",
            target: "_blank",
            src: "/assets/shortcuts/Grises/Ecovirtual.png",
            alt: "Económicas Virtual",
            text: "Económicas Virtual",
            class: "w-16 h-16 mb-2",
        },
        {
            href: "https://ecampus.economicasvirtual.edu.ar/",
            target: "_blank",
            src: "/assets/shortcuts/Grises/Educativa.png",
            alt: "E-ducativa",
            text: "E-ducativa",
            class: "w-16 h-16 mb-2",
        },
        {
            href: "http://190.221.123.226/fceaweb/",
            target: "_blank",
            src: "/assets/shortcuts/Grises/INTERFILE.png",
            alt: "InterFile",
            text: "InterFile",
            class: " w-16 h-16 mb-2",
        },
        /*   {
            href: `${host}/content/tramites.php`,
            target: "_self",
            src: "/assets/shortcuts/Grises/Tramites.png",
            alt: "Trámites",
            text: "Trámites",
            class: "w-16 h-16 mb-2",
        },*/
    ];
</script>

<!-- Contenedor principal simplificado -->
<div class="marquee-wrapper">
    {#each Array(numberOfCopies) as _, i}
        <div class="marquee-container">
            {#each slides as slide}
                <div class="item">
                    <a
                        href={slide.href}
                        target={slide.target}
                        class="menu-link"
                    >
                        <img src={slide.src} alt={slide.alt} class={slide.class} />
                        <span>{slide.text}</span>
                    </a>
                </div>
            {/each}
        </div>
    {/each}
</div>

<style>
    /* Contenedor con efecto fade en los bordes */
    .marquee-wrapper {
        display: flex;
        overflow: hidden;
        mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%);
        -webkit-mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%);
    }
    
    /* Contenedor del marquee con animación */
    .marquee-container {
        display: flex;
        flex-shrink: 0;
        gap: 1rem;
        animation: scroll 20s linear infinite;
    }
    
    /* Pausa al pasar el cursor */
    .marquee-wrapper:hover .marquee-container {
        animation-play-state: paused;
    }
    
    /* Todas las copias se mueven en la misma dirección */
    /* Se eliminó la alternancia de dirección */
    
    /* Animación de desplazamiento */
    @keyframes scroll {
        from { transform: translateX(0); }
        to { transform: translateX(calc(-100% - 1rem)); }
    }
    
    /* Estilos de los elementos */
    .item {
        width: 100px;
        flex-shrink: 0;
        padding: 0 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .menu-link {
        position: relative;
        padding-bottom: 4px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .menu-link::after {
        content: "";
        position: absolute;
        left: 0;
        bottom: 0;
        height: 2px;
        width: 0;
        background-color: #8b1a0b;
        transition: width 0.3s ease;
    }
    
    .menu-link:hover::after {
        width: 100%;
    }
</style>