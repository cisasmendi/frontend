<script>
    // @ts-ignore
    import Accordion from "$utilsMain/Accordion.svelte";
    export let cost = "";
   
</script>

<Accordion title={"Costos y Formas de Pago"}>
    <div slot="content">
        {@html cost}
    </div>
</Accordion>
