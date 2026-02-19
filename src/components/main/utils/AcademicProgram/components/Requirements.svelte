<script>
        // @ts-ignore
        import Accordion from "$utilsMain/Accordion.svelte";
    export let requirements = [];
</script>

{#if requirements.length > 0}
    <Accordion title={"Requisitos"}>
        <div slot="content">
            <ul class="pl-6 list-disc">
                {#each requirements as requirement}
                    <li class="pt-2"><p>{requirement}</p></li>
                {/each}
            </ul>
            <br>
        </div>
    </Accordion>
{/if}
