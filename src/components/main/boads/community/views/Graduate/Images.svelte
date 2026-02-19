<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";
    import Lightbox from "../../../../utils/Lightbox.svelte";

    let lightboxVisible = false;
    let currentImage = "";
    let currentImageTitle = "";

    const images2024 = [
        "/assets/colacion/2024/egresados2024.jpg",
    
    ];

    // Imágenes de colación 2025
    const images2025 = [
        "/assets/colacion/2025/CMU-861.JPG",
        "/assets/colacion/2025/CMU-177.JPG",
        "/assets/colacion/2025/CMU-295.JPG",
        "/assets/colacion/2025/CMU-307.JPG",
    ];

    function openLightbox(imageUrl, title) {
        currentImage = imageUrl;
        currentImageTitle = title;
        lightboxVisible = true;
    }

    function closeLightbox() {
        lightboxVisible = false;
        currentImage = "";
        currentImageTitle = "";
    }

    function handleKeydown(event, imageUrl, title) {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            openLightbox(imageUrl, title);
        }
    }
</script>

<BoardLayout>
    <div class="gallery-container">
        <!-- Encabezado -->
        <div class="header-section">
            <h3 class="text-2xl font-bold text-[#6d0205] mb-4">
                Galería de Colación de Grado
            </h3>
        </div>

        <!-- Colación 2025 -->
        <div class="year-section">
            <h4
                class="text-xl font-semibold text-[#6d0205] mb-4 border-b-2 border-[#6d0205] pb-2"
            >
                Colación 2025
            </h4>
            <div class="image-grid">
                {#each images2025 as image, index}
                    <button
                        class="image-card"
                        type="button"
                        on:click={() =>
                            openLightbox(
                                image,
                                `Colación de Grado 2025 - Imagen ${index + 1}`,
                            )}
                        on:keydown={(event) =>
                            handleKeydown(
                                event,
                                image,
                                `Colación de Grado 2025 - Imagen ${index + 1}`,
                            )}
                        aria-label="Ver imagen {index + 1} de la colación 2025"
                    >
                        <img
                            src={image}
                            alt="Colación de Grado 2025 - Imagen {index + 1}"
                            class="gallery-image"
                            loading="lazy"
                        />
                        <div class="image-overlay">
                            <span class="view-text">Ver imagen</span>
                        </div>
                    </button>
                {/each}
            </div>
        </div>

        <!-- Colación 2024 -->
          <!-- Colación 2025 -->
        <div class="year-section">
            <h4
                class="text-xl font-semibold text-[#6d0205] mb-4 border-b-2 border-[#6d0205] pb-2"
            >
                Colación 2024
            </h4>
            <div class="image-grid">
                {#each images2024 as image, index}
                    <button
                        class="image-card"
                        type="button"
                        on:click={() =>
                            openLightbox(
                                image,
                                `Colación de Grado 2025 - Imagen ${index + 1}`,
                            )}
                        on:keydown={(event) =>
                            handleKeydown(
                                event,
                                image,
                                `Colación de Grado 2025 - Imagen ${index + 1}`,
                            )}
                        aria-label="Ver imagen {index + 1} de la colación 2025"
                    >
                        <img
                            src={image}
                            alt="Colación de Grado 2024 - Imagen {index + 1}"
                            class="gallery-image"
                            loading="lazy"
                        />
                        <div class="image-overlay">
                            <span class="view-text">Ver imagen</span>
                        </div>
                    </button>
                {/each}
            </div>
        </div>

    </div>

    <!-- Lightbox Component -->
</BoardLayout>
<Lightbox showLightbox={lightboxVisible} {closeLightbox}>
    <div class="lightbox-image-container">
        <img
            src={currentImage}
            alt={currentImageTitle}
            class="lightbox-image"
        />
        <h3 class="lightbox-title">{currentImageTitle}</h3>
    </div>
</Lightbox>

<style>
    .gallery-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem;
    }

    .header-section {
        text-align: center;
        margin-bottom: 2rem;
    }

    .year-section {
        margin-bottom: 3rem;
    }

    .image-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }


    .image-card {
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        background: none;
        border: none;
        padding: 0;
        display: block;
        width: 100%;
    }

    .image-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }

    .gallery-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        transition: transform 0.3s ease;
    }

   

    .image-card:hover .gallery-image {
        transform: scale(1.05);
    }

    .image-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(
            to bottom,
            transparent 0%,
            transparent 50%,
            rgba(0, 0, 0, 0.7) 100%
        );
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding: 1rem;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .image-card:hover .image-overlay {
        opacity: 1;
    }

    .view-text {
        color: white;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .image-grid {
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }

        .gallery-image {
            height: 150px;
        }

   
    }

    @media (max-width: 480px) {
        .gallery-container {
            padding: 0.5rem;
        }

        .image-grid {
            grid-template-columns: 1fr;
        }

        .gallery-image {
            height: 180px;
        }

  
    }

    /* Lightbox styles */
    .lightbox-image-container {
        text-align: center;
        padding: 1rem;
    }

    .lightbox-image {
        max-width: 100%;
        max-height: 70vh;
        object-fit: contain;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }

    .lightbox-title {
        margin-top: 1rem;
        color: #6d0205;
        font-size: 1.2rem;
        font-weight: 600;
    }
</style>
