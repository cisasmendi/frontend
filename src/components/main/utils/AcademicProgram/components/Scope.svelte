<script>
       // @ts-ignore
       import Accordion from "$utilsMain/Accordion.svelte";
    export let scope = "";

    function addStyles(htmlContent) {
        return htmlContent
            .replace(/<ul>/g, '<ul style="list-style: decimal; padding-left:1rem;">')
            .replace(/<p>/g, '<p style="color: #333; padding-top: 0.5em; ">')
            .replace(/<strong>/g, '<strong style="font-weight: bold;">')
            .replace(/<li>/g, '<li style="margin: 5px 0;">') // Estilo para <li>
            .replace(/<ol>/g, '<ol style="padding-left: 20px;">') // Estilo para <ol>
            .replace(
                /<hr>/g,
                '<hr style="border: 1px solid #ccc; margin: 20px 0;">',
            ); // Estilo opcional para el <hr>
    }
    let scopeHtml = addStyles(scope);
</script>

<Accordion title={"Alcance"}>
    <div slot="content">
        <p>{@html scopeHtml}</p>
    </div>
</Accordion>
