<script>
    import { onMount } from "svelte";

    let posts = [];
    let errorMessage = "";
    let isLoading = true;
    let retryAttempts = 0;
    const maxRetries = 3;
    const url= import.meta.env.VITE_HOST+"/api/facebook-posts?nro=24";
   
    async function fetchFacebookInit(url, attempt = 1) {
        isLoading = true;
        errorMessage = "";
        
        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 10000); // Timeout de 10 segundos
            
            const response = await fetch(url, {
                signal: controller.signal,
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            
            clearTimeout(timeoutId);
            
            if (!response.ok) {
                throw new Error(`Error del servidor: ${response.status}`);
            }
            
            const data = await response.json();     

            if (data.error) {
                throw new Error(data.error.message || 'Error desconocido del API');
            }
            
            if (data?.noticias && Array.isArray(data.noticias)) {
                posts = data.noticias;
                retryAttempts = 0;
            } else {
                // Si no hay noticias o la estructura no es la esperada
                posts = [];
                if (data?.noticias && !Array.isArray(data.noticias)) {
                    throw new Error('Formato de datos inesperado');
                }
            }
        } catch (error) {
            console.error(`Intento ${attempt} fallido:`, error);
            
            // Para la mayoría de errores, simplemente mostrar que no hay noticias disponibles
            if (error.name === 'AbortError' || error.message.includes('Failed to fetch') || error.message.includes('NetworkError') || error.message.includes('Error del servidor')) {
                // Para errores de conexión y servidor, no mostramos mensaje de error
                errorMessage = "";
                posts = [];
            } else {
                // Solo para errores muy específicos que el usuario necesite saber
                errorMessage = "";
                posts = [];
            }
            
            // Reintentar automáticamente si es un error de red y no hemos excedido el límite
            if (attempt < maxRetries && (error.message.includes('Failed to fetch') || error.name === 'AbortError')) {
                retryAttempts = attempt;
                setTimeout(() => {
                    fetchFacebookInit(url, attempt + 1);
                }, 2000 * attempt); // Espera incremental: 2s, 4s, 6s
                return;
            }
            
            retryAttempts = attempt;
        } finally {
            isLoading = false;
        }
    }

    function formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString();
    }

    onMount(() => {
        fetchFacebookInit(url);
        let max_height = window.innerHeight;
        window.scrollTo(0, max_height);
    });

    // Función para reintentar manualmente
    function handleRetry() {
        fetchFacebookInit(url);
    }

    let expanded = [];
    function toggleExpand(index) {
        expanded[index] = !expanded[index];
    }

    function cleanText(text) {
        // Si el texto es undefined o null, lo convertimos a una cadena vacía
        return (text || "")
            .replace(/undefined/g, "") // Elimina cualquier "undefined"
            .replace(/\n/g, "<br>"); // Reemplaza los saltos de línea con <br>
    }
</script>

<main>
    <div class="container mx-auto p-6">
        <section class="mb-8 p-6">
            {#if isLoading}
                <div class="text-center">
                    <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-4"></div>
                    <p class="text-gray-500">
                        Cargando noticias...
                        {#if retryAttempts > 0}
                            <span class="text-sm text-gray-400">(Intento {retryAttempts + 1}/{maxRetries})</span>
                        {/if}
                    </p>
                </div>
            {:else if errorMessage}
                <div class="text-center p-8 bg-red-50 rounded-lg border border-red-200">
                    <div class="mb-4">
                        <svg class="mx-auto h-12 w-12 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.996-.833-2.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z" />
                        </svg>
                    </div>
                    <h3 class="text-lg font-semibold text-red-800 mb-2">Error al cargar las noticias</h3>
                    <p class="text-red-600 mb-4">{errorMessage}</p>
                    <div class="space-y-2">
                        <button
                            class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded transition-colors duration-200"
                            on:click={handleRetry}
                        >
                            Reintentar
                        </button>
                        {#if retryAttempts >= maxRetries}
                            <p class="text-sm text-gray-600">
                                Se han agotado los intentos automáticos. Puedes intentar de nuevo manualmente.
                            </p>
                        {/if}
                    </div>
                </div>
            {:else if posts.length > 0}
                <div
                    class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
                >
                    {#each posts as post, index}
                        <div
                            class="post-card bg-white shadow-md rounded-lg overflow-hidden"
                        >
                            <div class="p-4">
                                {#if post.full_picture}
                                    <!-- svelte-ignore a11y-img-redundant-alt -->
                                    <img
                                        class="w-full h-48 object-cover mb-4"
                                        src={post.full_picture}
                                        alt="Post image"
                                    />
                                {:else}
                                    <!-- svelte-ignore a11y-img-redundant-alt -->
                                    <img
                                        class="w-full h-48 object-cover mb-4"
                                        src="/assets/logos/logo_FCEyA_1-01.png"
                                        alt="Post image"
                                    />
                                {/if}

                                <h3
                                    class="text-sm font-semibold text-gray-500 mb-2"
                                >
                                    {formatDate(post.created_time)}
                                </h3>
                                {#if post.message}
                                    <div class="text-container">
                                        <p
                                            class={`text-gray-700 text-base mb-4 ${expanded[index] ? "" : "line-clamp"}`}
                                        >
                                            {@html cleanText(post.message)}
                                        </p>
                                        <button
                                            class="text-blue-600 hover:text-blue-800 text-sm"
                                            on:click={() => toggleExpand(index)}
                                        >
                                            {expanded[index]
                                                ? "Mostrar Menos"
                                                : "Mostrar Más"}
                                        </button>
                                    </div>
                                {/if}

                                <a
                                    href={post.permalink_url}
                                    target="_blank"
                                    class="text-blue-600 hover:text-blue-800"
                                    >Ir al Post</a
                                >
                            </div>
                        </div>
                    {/each}
                </div>

            {:else}
                <div class="text-center p-8 bg-blue-50 rounded-lg border border-blue-100">
                    <div class="mb-4">
                        <svg class="mx-auto h-12 w-12 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                    </div>
                    <h3 class="text-lg font-semibold text-blue-800 mb-2">Estamos actualizando las noticias</h3>
                    <p class="text-blue-600 mb-4">En este momento no hay noticias para mostrar. ¡Vuelve en unos minutos!</p>
                    <button
                        class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full transition-colors duration-200 shadow-md"
                        on:click={handleRetry}
                    >
                        Actualizar noticias
                    </button>
                </div>
            {/if}
        </section>
    </div>
</main>

<style>
    .post-card {
        transition: transform 0.2s ease-in-out;
    }

    .post-card:hover {
        transform: translateY(-5px);
    }

    /* Estilos de botones */
    button:disabled {
        cursor: not-allowed;
    }

    .post-card {
        transition: transform 0.2s ease-in-out;
    }

    .post-card:hover {
        transform: translateY(-5px);
    }

    /* Limitar la altura del texto a 3 líneas */
    .line-clamp {
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    /* Animación */
    .text-container button {
        transition: color 0.3s ease;
    }
</style>
