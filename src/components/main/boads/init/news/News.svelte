<script>
  import { onMount } from "svelte";
  let noticias = [
    {
      titulo: "Título de la Noticia 1",
      resumen:
        "Resumen breve de la noticia o evento. Este es un ejemplo de cómo podría verse el contenido.",
      imagen: "https://via.placeholder.com/600x400",
      enlace: "/news/1",
      created_time: "2021-09-01T12:00:00",
    },
    {
      titulo: "Título de la Noticia 2",
      resumen:
        "Resumen breve de la noticia o evento. Este es un ejemplo de cómo podría verse el contenido.",
      imagen: "https://via.placeholder.com/600x400",
      enlace: "/news",
      created_time: "2021-09-01T12:00:00",
    },
    {
      titulo: "Título de la Noticia 3",
      resumen:
        "Resumen breve de la noticia o evento. Este es un ejemplo de cómo podría verse el contenido.",
      imagen: "https://via.placeholder.com/600x400",
      enlace: "/news:3",
    },
    {
      titulo: "Título de la Noticia 1",
      resumen:
        "Resumen breve de la noticia o evento. Este es un ejemplo de cómo podría verse el contenido.",
      imagen: "https://via.placeholder.com/600x400",
      enlace: "/news/1",
    },
  ];

  let errorMessage = "";
  let isLoading = true;
  let retryAttempts = 0;
  const maxRetries = 3;
  const url= import.meta.env.VITE_HOST+"/api/facebook-posts?nro=3";
 
  async function fetchFacebookPosts(attempt = 1) {
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
        noticias = data.noticias;
        retryAttempts = 0;
      } else {
        // Si no hay noticias o la estructura no es la esperada
        noticias = [];
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
        noticias = [];
      } else {
        // Solo para errores muy específicos que el usuario necesite saber
        errorMessage = "";
        noticias = [];
      }
      
      // Reintentar automáticamente si es un error de red y no hemos excedido el límite
      if (attempt < maxRetries && (error.message.includes('Failed to fetch') || error.name === 'AbortError')) {
        retryAttempts = attempt;
        setTimeout(() => {
          fetchFacebookPosts(attempt + 1);
        }, 2000 * attempt); // Espera incremental: 2s, 4s, 6s
        return;
      }
      
      retryAttempts = attempt;
    } finally {
      isLoading = false;
    }
  }

  // Función para reintentar manualmente
  function handleRetry() {
    fetchFacebookPosts();
  }

  function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString();
  }
  function toggleText(index) {
    noticias = noticias.map((post, i) =>
      i === index ? { ...post, showFullText: !post.showFullText } : post
    );
  }

  onMount(() => fetchFacebookPosts());
</script>

<style>
  .clamp-3-lines {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .scrollable-text {
  max-height: 10rem;
  overflow-y: auto;
}
  
</style>

<div class="container mx-auto p-6 pb-20">
  <h2 class="text-2xl font-semibold text-[#db1919]">Noticias y Eventos</h2>
  <p class="text-gray-100 mt-2">
    Mantente informado sobre los últimos acontecimientos, conferencias y
    publicaciones de nuestra facultad.
  </p>

  {#if isLoading}
    <div class="text-center mt-8">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-gray-500">
        Cargando noticias...
        {#if retryAttempts > 0}
          <span class="text-sm text-gray-400">(Intento {retryAttempts + 1}/{maxRetries})</span>
        {/if}
      </p>
    </div>
  {:else if errorMessage}
    <div class="text-center p-8 mt-6">
    
      <h3 class="text-lg font-semibold text-blue-800 mb-2">Estamos actualizando las noticias</h3>
      <p class="text-blue-600 mb-4">En este momento no hay noticias para mostrar. ¡Vuelve en unos minutos!</p>
      <button
        class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full transition-colors duration-200 shadow-md"
        on:click={handleRetry}
      >
        Actualizar noticias
      </button>
    </div>
  {:else if noticias.length === 0}
    <div class="text-center p-8 mt-6 ">
     
      <h3 class="text-lg font-semibold text-blue-800 mb-2">Estamos actualizando las noticias</h3>
      <p class="text-blue-600 mb-4">En este momento no hay noticias para mostrar. ¡Vuelve en unos minutos!</p>
      <button
        class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full transition-colors duration-200 shadow-md"
        on:click={handleRetry}
      >
        Actualizar noticias
      </button>
    </div>
  {:else if noticias.length > 0}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
      {#each noticias as post, i}
        <div
          class="object-cover transition-transform duration-300 hover:scale-110 "
        >
          <div class="animate-slide-in-up bg-white shadow-md rounded-lg overflow-hidden h-full">
            <img class="w-full h-[60%] object-cover" src={post.imagen} alt={post.titulo} />
            <div class="p-4">
              <h3 class="text-lg font-semibold text-[#6d0205]">
                {formatDate(post.created_time)}
              </h3>
              <div class={`mt-2 text-gray-700 ${post.showFullText ? 'scrollable-text' : 'clamp-3-lines'}`}>
                {post.resumen}
              </div>
              <button
                on:click={() => toggleText(i)}
                class="text-blue-500 hover:underline mt-2 inline-block"
              >
                {post.showFullText ? 'Ver menos' : 'Ver más'}
              </button>
              <a
                href={post.permalink_url}
                target="_blank"
                class="text-blue-600 hover:text-blue-800 block mt-2"
              >
                VER Post
              </a>
              <a
                href="/news"
                class="text-blue-500 hover:underline mt-2 inline-block"
              >
                Ir a Noticias
              </a>
            </div>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

