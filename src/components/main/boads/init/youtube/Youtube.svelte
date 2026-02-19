<script>
    import { onMount } from "svelte";

    let isShow = false;
    let videos = [
        {
            id: "V_eLtZpbau4",
            title: "Video Festejo Día de la Zamba.",
        },
    ]; 
    let selectedVideo = videos[0];
    let isLoading = true;

    const url = import.meta.env.VITE_HOST + "/api/youtube-videos";

    onMount(async () => {
        try {
            const response = await fetch(url);
            const data = await response.json();
            if (data.error) throw new Error(data.error.message);
            videos = data.videos;
            // truncar array a 6 elementos
            videos = videos.slice(0, 6);
            selectedVideo = videos[0];
        } catch (error) {
            console.error("Error fetching YouTube videos:", error);
        } finally {
            isLoading = false;
            isShow = true;
        }
    });

    function selectVideo(video) {
        selectedVideo = video;
    }
</script>

<div class="youtube-section">
    <div class="header-section">
        <h2 class="section-title fade-in-slide-down">
            <svg class="youtube-icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
            </svg>
            Nuestro Canal
        </h2>
        <div class="subtitle">Descubre nuestro contenido exclusivo</div>
    </div>

    {#if isLoading}
        <div class="loading-container">
            <div class="skeleton-loader">
                <!-- Video principal skeleton -->
                <div class="main-skeleton">
                    <div class="video-skeleton"></div>
                    <div class="title-skeleton"></div>
                </div>
                <!-- Lista de videos skeleton -->
                <div class="list-skeleton">
                    {#each Array(6) as _, i}
                        <div class="thumbnail-skeleton">
                            <div class="thumb-img-skeleton"></div>
                            <div class="thumb-title-skeleton"></div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    {:else}
        <div class="container">
            <!-- Video Player -->
            <div class="video-player fade-in-slide-up">
                <div class="video-wrapper">
                    <iframe
                        width="100%"
                        height="100%"
                        src={`https://www.youtube.com/embed/${selectedVideo.id}?rel=0&modestbranding=1&showinfo=0`}
                        title={selectedVideo.title}
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen
                    ></iframe>
                </div>
                <div class="video-info">
                    <h3 class="video-title">{selectedVideo.title}</h3>                  
                </div>
            </div>

            <!-- Video List -->
            <div class="video-list fade-in-slide-left">
                <div class="list-header">
                    <h4 class="list-title">Más videos</h4>
                    <span class="video-count">{videos.length} videos</span>
                </div>
                <div class="video-grid">
                    {#each videos as video, index}
                        <div
                            class="video-thumbnail {selectedVideo.id === video.id ? 'active' : ''}"
                            role="button"
                            tabindex="0"
                            on:click={() => selectVideo(video)}
                            on:keydown={(e) => {
                                if (e.key === "Enter") selectVideo(video);
                            }}
                        >
                            <div class="thumbnail-wrapper">
                                <img
                                    src={`https://i.ytimg.com/vi/${video.id}/hqdefault.jpg`}
                                    alt={video.title}
                                    loading="lazy"
                                />
                                <div class="play-overlay">
                                    <svg viewBox="0 0 24 24" fill="currentColor" class="play-icon">
                                        <path d="M8 5v14l11-7z"/>
                                    </svg>
                                </div>
                                <div class="video-duration">
                                    <span>HD</span>
                                </div>
                            </div>
                            <div class="thumbnail-info">
                                <p class="thumbnail-title">{video.title}</p>
                                <span class="video-index">#{index + 1}</span>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    {/if}
</div>

<style>
    .youtube-section {
        padding: 0;
        background: transparent;
        border-radius: 0;
        margin: 0;
        box-shadow: none;
    }

    .header-section {
        text-align: left;
        margin-bottom: 2rem;
        padding-left: 1.25rem;
    }

    .section-title {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 2rem;
        font-weight: 600;
        color: #6d0205;
        margin: 0 0 0.5rem 0;
        padding-top: 1.5rem;
    }

    .youtube-icon {
        width: 32px;
        height: 32px;
        color: #6d0205;
        filter: drop-shadow(0 2px 4px rgba(109, 2, 5, 0.2));
    }

    .subtitle {
        color: #6c757d;
        font-size: 1rem;
        font-weight: 400;
        margin-top: 0.25rem;
        padding-left: 44px;
    }

    .loading-container {
        min-height: 500px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }

    .skeleton-loader {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 2rem;
        width: 100%;
        max-width: 1200px;
    }

    .main-skeleton {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
    }

    .video-skeleton {
        width: 100%;
        height: 350px;
        background: linear-gradient(90deg, #f8f9fa 25%, #e9ecef 50%, #f8f9fa 75%);
        background-size: 200% 100%;
        animation: loading 1.5s infinite;
        border-radius: 12px;
    }

    .title-skeleton {
        width: 70%;
        height: 20px;
        background: linear-gradient(90deg, #f8f9fa 25%, #e9ecef 50%, #f8f9fa 75%);
        background-size: 200% 100%;
        animation: loading 1.5s infinite;
        border-radius: 6px;
    }

    .list-skeleton {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        display: grid;
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .thumbnail-skeleton {
        display: flex;
        gap: 0.75rem;
        align-items: center;
    }

    .thumb-img-skeleton {
        width: 80px;
        height: 60px;
        background: linear-gradient(90deg, #f8f9fa 25%, #e9ecef 50%, #f8f9fa 75%);
        background-size: 200% 100%;
        animation: loading 1.5s infinite;
        border-radius: 8px;
    }

    .thumb-title-skeleton {
        flex: 1;
        height: 16px;
        background: linear-gradient(90deg, #f8f9fa 25%, #e9ecef 50%, #f8f9fa 75%);
        background-size: 200% 100%;
        animation: loading 1.5s infinite;
        border-radius: 6px;
    }

    @keyframes loading {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }

    .container {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 2rem;
        align-items: start;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }

    .video-player {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 0, 0, 0.06);
    }

    .video-player:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }

    .video-wrapper {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 56.25%;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    }

    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    .video-info {
        margin-top: 1.25rem;
    }

    .video-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #2d3748;
        margin: 0;
        line-height: 1.4;
    }

    .video-list {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        max-height: 550px;
        overflow-y: auto;
        border: 1px solid rgba(0, 0, 0, 0.06);
    }

    .list-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.25rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid #e5e7eb;
    }

    .list-title {
        font-size: 1.125rem;
        font-weight: 600;
        color: #374151;
        margin: 0;
    }

    .video-count {
        background: #f3f4f6;
        color: #6b7280;
        padding: 0.25rem 0.75rem;
        border-radius: 8px;
        font-size: 0.875rem;
        font-weight: 500;
    }

    .video-grid {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .video-thumbnail {
        display: flex;
        gap: 0.75rem;
        padding: 0.75rem;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s ease;
        border: 1px solid transparent;
        position: relative;
        background: white;
    }

    .video-thumbnail:hover {
        background: #f9fafb;
        transform: translateX(3px);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border-color: #e5e7eb;
    }

    .video-thumbnail.active {
        background: #fef2f2;
        border-color: #fca5a5;
        box-shadow: 0 2px 8px rgba(239, 68, 68, 0.1);
    }

    .thumbnail-wrapper {
        position: relative;
        flex-shrink: 0;
        width: 90px;
        height: 68px;
        border-radius: 6px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .thumbnail-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.3s ease;
    }

    .video-thumbnail:hover .thumbnail-wrapper img {
        transform: scale(1.05);
    }

    .play-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0, 0, 0, 0.7);
        color: white;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .video-thumbnail:hover .play-overlay {
        opacity: 1;
    }

    .play-icon {
        width: 14px;
        height: 14px;
        margin-left: 1px;
    }

    .video-duration {
        position: absolute;
        bottom: 3px;
        right: 3px;
        background: rgba(0, 0, 0, 0.75);
        color: white;
        padding: 1px 4px;
        border-radius: 3px;
        font-size: 0.7rem;
        font-weight: 500;
    }

    .thumbnail-info {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-width: 0;
    }

    .thumbnail-title {
        font-size: 0.875rem;
        font-weight: 500;
        color: #374151;
        margin: 0;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .video-index {
        font-size: 0.7rem;
        color: #9ca3af;
        font-weight: 500;
        margin-top: 0.5rem;
    }

    /* Animaciones más sutiles */
    .fade-in-slide-down {
        opacity: 0;
        transform: translateY(-10px);
        animation: fadeInSlideDown 0.6s ease forwards;
        animation-delay: 0.1s;
    }

    .fade-in-slide-up {
        opacity: 0;
        transform: translateY(15px);
        animation: fadeInSlideUp 0.7s ease forwards;
        animation-delay: 0.2s;
    }

    .fade-in-slide-left {
        opacity: 0;
        transform: translateX(15px);
        animation: fadeInSlideLeft 0.7s ease forwards;
        animation-delay: 0.3s;
    }

    @keyframes fadeInSlideDown {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInSlideUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInSlideLeft {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    /* Scroll más simple */
    .video-list::-webkit-scrollbar {
        width: 4px;
    }

    .video-list::-webkit-scrollbar-track {
        background: #f3f4f6;
        border-radius: 4px;
    }

    .video-list::-webkit-scrollbar-thumb {
        background: #d1d5db;
        border-radius: 4px;
    }

    .video-list::-webkit-scrollbar-thumb:hover {
        background: #9ca3af;
    }

    /* Responsividad adaptada */
    @media (max-width: 1024px) {
        .container {
            grid-template-columns: 1fr;
            gap: 1.5rem;
            padding: 0 0.5rem;
        }

        .video-list {
            max-height: 350px;
        }

        .video-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.75rem;
        }

        .video-thumbnail {
            flex-direction: column;
            text-align: center;
            padding: 1rem;
        }

        .thumbnail-wrapper {
            width: 100%;
            height: 100px;
        }
    }

    @media (max-width: 768px) {
        .header-section {
            padding-left: 0.5rem;
        }

        .section-title {
            font-size: 1.75rem;
        }

        .skeleton-loader {
            grid-template-columns: 1fr;
        }

        .video-grid {
            grid-template-columns: 1fr;
        }

        .container {
            padding: 0;
        }
    }

    @media (max-width: 480px) {
        .section-title {
            font-size: 1.5rem;
            flex-direction: column;
            align-items: flex-start;
            gap: 6px;
        }

        .youtube-icon {
            width: 28px;
            height: 28px;
        }

        .subtitle {
            padding-left: 0;
        }

        .container {
            gap: 1rem;
        }

        .video-player, .video-list {
            padding: 1rem;
        }

        .video-thumbnail {
            padding: 0.5rem;
        }

        .thumbnail-wrapper {
            height: 80px;
        }
    }
</style>
