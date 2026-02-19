<script>
      // @ts-ignore
      import Accordion from "$utilsMain/Accordion.svelte";

    export let objectives = {
        general: [],
        specific: [],
    };
   
</script>

<Accordion title={"Objetivos"}>
    <div slot="content">
        {#if objectives.general.length > 0}
            <h3 class="text-lg font-semibold text-[#6d0205]">
                Objetivos generales
            </h3>
            <ul class="pl-6 list-disc">
                {#each objectives.general as objective}
                    <li class="pt-2"><p>{objective}</p></li>
                {/each}
            </ul>
        {/if}
        {#if objectives.specific.length > 0}
            <h3 class="text-lg pt-4 font-semibold text-[#6d0205]">
                Objetivos específicos
            </h3>
            <ul class="pl-6 list-disc">
                {#each objectives.specific as objective}
                    <li class="pt-2"><p>{objective}</p></li>
                {/each}
            </ul>
        {/if}
    </div>
</Accordion>
