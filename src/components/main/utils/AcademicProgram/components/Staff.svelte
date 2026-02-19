<script>
      // @ts-ignore
      import Accordion from "$utilsMain/Accordion.svelte";
    export let staff = "";
    function addStyles(htmlContent) {
        return htmlContent
            .replace(/<p>/g, '<p style="color: #333; padding-top: 0.5em; ">')
            .replace(/<strong>/g, '<strong style="font-weight: bold;">')
            .replace(/<li>/g, '<li style="margin: 5px 0;">');
    }
    let staffHtml = addStyles(staff);
</script>

<Accordion title={"Plantel Docente"}>
    <div slot="content">
        <p>{@html staffHtml}</p>
    </div>
</Accordion>
