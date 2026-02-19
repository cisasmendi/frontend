<script>
    // @ts-ignore
    import Accordion from "$utilsMain/Accordion.svelte";

    export let programInfo = {
        downloads: [],
    };
</script>

<Accordion title={"Lista de Archivos y Documentos"}>
    <div slot="content">
        {#if programInfo?.downloads?.length > 0}     
            {#each programInfo.downloads as download}
                <li>
                    <a
                        href={download.url}
                        class="text-blue-600 s-HL7iPF8fmwQi"
                        target="_blank"
                        ><i class="fas fa-download"></i> {download.name}</a
                    >
                </li>
            {/each}
            <br />
        {/if}
    </div>
</Accordion>
