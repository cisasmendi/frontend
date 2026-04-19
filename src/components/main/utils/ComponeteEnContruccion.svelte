<script>
  export let title = "";
  export let imageUrl = "https://eco.unca.edu.ar/assets2/users/paginaeco/Sin título-W1.png";
  let currentYear = new Date().getFullYear();
</script>


  <h2 class="text-2xl font-semibold text-[#6d0205]">{title}</h2>
  <div
    class="flex flex-col items-center justify-center min-h-screen bg-gray-100"
  >
    <img
      src={imageUrl}
      alt="Página en Construcción"
      class="w-32 mx-auto mb-6"
    />
    <div class="text-center">
      <h1 class="text-4xl font-bold text-[#6d0205] mb-4">
        Página en Construcción
      </h1>
      <p class="text-xl text-gray-600 mb-6">
        Estamos trabajando para traerte algo increíble. ¡Vuelve pronto!
      </p>
    </div>
  </div>

