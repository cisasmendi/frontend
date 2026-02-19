<script>
    import Menu from "../../utils/Menu.svelte";
    import History from "./views/History.svelte";
    import Authorities from "./views/Authorities.svelte";
    import Infographic from "./views/Infographic.svelte";
    import About from "./views/About.svelte";
    import Functions from "./views/Functions.svelte";

    import Members from "./views/Members.svelte";
    import Councilors2025 from "./views/Councilors2025_2027.svelte";
    import Ordenanza from "./views/Ordenanza.svelte";

    let menuItems = [
        "Nuestra Historia",
        "Autoridades",
        "Infografía",
        "Ordenanza",
        {
            title: "Consejo Directivo",
            submenu: ["Acerca de", "Funciones", "Integrantes"],
        },
        "Elecciones Consejeros 2025-2027",
    ];

    let imageUrl = "https://via.placeholder.com/400";
    let title = "Nuestra Historia";

    function handleClick(item) { 
     
        if (typeof item.detail === "object") {
          
            title = item.detail.submenu[0];
        } else {
            title = item.detail;
        }
    }

    
</script>

<main class=" mx-auto flex flex-col lg:flex-row w-full lg:w-auto ">    
    <Menu {menuItems} on:click={handleClick} />
    {#if title === "Nuestra Historia"}
        <History {title} imageUrl={"/assets/imagenes/rector.jpg"} />
    {/if}
    {#if title === "Autoridades"}
        <Authorities {title} />
    {/if}
    {#if title === "Infografía"}
        <Infographic {title} />
    {/if}
    {#if title === "Ordenanza"}
        <Ordenanza {title} />
    {/if}
    {#if title === "Acerca de"}
        <About {title} />
    {/if}
    {#if title === "Funciones"}
        <Functions {title} />
    {/if}
    {#if title === "Integrantes"}
        <Members {title} />
    {/if}
    {#if title === "Elecciones Consejeros 2025-2027"}
        <Councilors2025/>
    {/if}
</main>
