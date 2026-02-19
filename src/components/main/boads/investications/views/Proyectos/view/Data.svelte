<script>
// @ts-nocheck

    import Accordion from "$utilsMain/Accordion.svelte";
    export let  data={
        title:"",
        proyectos:[]
    };
    let title = data.title;
    let convenios = data.proyectos;
</script>

<Accordion {title}>
    <div slot="content">        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each convenios as convenio}
                <div class="border p-4 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold text-[#6d0205]">
                        {convenio.titulo}
                    </h3>
                    <p>Director: {convenio.director}</p>
                </div>
            {/each}
        </div>
        <br>
    </div>
</Accordion>