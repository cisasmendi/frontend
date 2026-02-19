<script>
    // @ts-ignore
    import Accordion from "$utilsMain/Accordion.svelte";
    //  export let studyPlan = [];
</script>

<Accordion title={"Plan de Estudios"}>
    <div slot="content">
        <slot></slot>
    </div>
</Accordion>

