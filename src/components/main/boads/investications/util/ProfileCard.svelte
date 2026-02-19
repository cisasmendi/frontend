<script>
    export let name = "John Doe";
    export let position = "Software Engineer";
    export let imageUrl = "https://via.placeholder.com/150";
</script>

<div class="bg-white shadow-lg rounded-lg p-6 flex flex-col items-center text-center relative">
    <!-- Imagen del perfil -->
    <!-- svelte-ignore a11y-img-redundant-alt -->
    <img src={imageUrl} alt="Profile Image" 
         class="w-24 h-24 rounded-full border-4 border-white -mt-16 bg-gray-100 object-cover" />
    <!-- Contenido de la tarjeta -->
    <div class="mt-8">
        <h2 class="text-xl font-bold text-gray-900">{name}</h2>
        <p class="text-gray-600">{position}</p>
    </div>
</div>

<style>
    .bg-white {
        margin-top: 3rem; /* Espacio para la imagen */
    }
</style>
