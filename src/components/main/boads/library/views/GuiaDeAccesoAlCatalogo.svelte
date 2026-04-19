<script>
    import PdfReader from "../../../utils/PdfView.svelte";
    export let title = "";
    import BoardLayout from "$BoardLayout";
</script>

<BoardLayout {title}>
    <PdfReader url="https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/biblioteca/guiaSimplificada.pdf" />
</BoardLayout>