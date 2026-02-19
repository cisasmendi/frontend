<script>
    import { onMount } from "svelte";
    import { writable } from "svelte/store";

    export let title = "";
    export let course = -1;

    const components = writable([]);
    const isLoading = writable(true); // Estado para saber si se están cargando los componentes
    const error = writable(null); // Estado para almacenar posibles errores

    onMount(async () => {
        try {
            isLoading.set(true); // Inicia el proceso de carga
            let modules;
            // Selección de carpeta de acuerdo con el valor de title
            switch (title) {
                case "Talleres":
                    modules = import.meta.glob("./Talleres/[^_]*.svelte");
                    if (course !== -1) {
                        modules = Object.fromEntries(
                            Object.entries(modules).filter(([key]) =>
                                key.includes(`/${course}.svelte`),
                            ),
                        );
                        props = {
                            open: true,
                        };
                    }
                    break;
                case "Cursos de Posgrado":
                    //busacar todos los archivos svelte en la carpeta CursosDePosgrado menos los que tengan _ delante
                    modules = import.meta.glob(
                        "./CursosDePosgrado/[^_]*.svelte",
                    );
                    if (course !== -1) {
                        modules = Object.fromEntries(
                            Object.entries(modules).filter(([key]) =>
                                key.includes(`/${course}.svelte`),
                            ),
                        );
                        props = {
                            open: true,
                        };
                    }
                    break;
                case "Diplomaturas":
                    modules = import.meta.glob("./Diplomaturas/[^_]*.svelte");
                    // si course es != -1, filtrar los módulos por el número de curso
                    if (course !== -1) {
                        modules = Object.fromEntries(
                            Object.entries(modules).filter(([key]) =>
                                key.includes(`/${course}.svelte`),
                            ),
                        );
                        props = {
                            open: true,
                        };
                    }
                    break;
                default:
                    throw new Error(
                        "No se encontraron módulos para este título.",
                    );
            }

            // Cargar los componentes dinámicamente
            const loadedComponents = await Promise.all(
                Object.keys(modules).map(async (path) => {
                    const module = await modules[path]();
                    return module.default;
                }),
            );

            components.set(loadedComponents);
        } catch (err) {
            error.set(err.message);
            console.error("Error al cargar los componentes:", err);
        } finally {
            isLoading.set(false); // Finaliza el proceso de carga
        }
    });

    let props = {};
</script>

<div class="w-full p-4">
    <h2 class="text-2xl font-semibold text-[#6d0205] pt-4">{title}</h2>
    {#if $isLoading}
        <!-- Mostrar un mensaje o un spinner mientras se cargan los componentes -->
        <div>Cargando componentes...</div>
    {:else if $error}
        <!-- Mostrar mensaje de error si algo sale mal -->
        <div class="text-red-500">Error: {$error}</div>
    {:else}
        <!-- Mostrar los componentes cargados -->
        {#each $components as Component}
            <svelte:component this={Component} {...props} />
        {/each}
    {/if}
</div>
