<script>
    import PdfReader from "../../../utils/PdfView.svelte";
    export let title = "";
    import BoardLayout from "$BoardLayout";
</script>

<BoardLayout {title}>
    <PdfReader url="/assets/pdf/biblioteca/guiaSimplificada.pdf" />
</BoardLayout>