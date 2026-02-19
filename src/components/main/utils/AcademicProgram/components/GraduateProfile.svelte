<script>
      // @ts-ignore
      import Accordion from "$utilsMain/Accordion.svelte";
    export let graduateProfile = "";
    function addStyles(htmlContent) {
        return htmlContent
            .replace(/<p>/g, '<p style="color: #333; padding-top: 0.5em; ">')
            .replace(/<strong>/g, '<strong style="font-weight: bold;">')
            .replace(/<li>/g, '<li style="margin: 5px 0;">');
    }
    let graduateProfileHtml = addStyles(graduateProfile);
</script>

<Accordion title={" Perfil del Egresado"}>
    <div slot="content">
        <p>{@html graduateProfileHtml}</p>
    </div>
</Accordion>
