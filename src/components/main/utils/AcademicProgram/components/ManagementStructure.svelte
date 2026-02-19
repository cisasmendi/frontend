<script>
    import Accordion from "$utilsMain/Accordion.svelte";
    export let managementStructure = "";
    function addStyles(htmlContent) {
        return htmlContent
            .replace(/<p>/g, '<p style="color: #333; padding-top: 0.5em; ">')
            .replace(/<strong>/g, '<strong style="font-weight: bold;">')
            .replace(/<li>/g, '<li style="margin: 5px 0;">');
    }
    let managementStructureHtml = addStyles(managementStructure);
</script>

<Accordion title={"Estructura de Gestión"}>
    <div slot="content">
        <p>{@html managementStructureHtml}</p>
    </div>
</Accordion>
