<script>
    import BoardLayout from "$BoardLayout";
    import PdfReader from "../../../../utils/PdfView.svelte";
    export let title = "";
</script>

<BoardLayout {title}>
    <PdfReader url="https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/noDocentesConvenioFatun.pdf" />
</BoardLayout>
