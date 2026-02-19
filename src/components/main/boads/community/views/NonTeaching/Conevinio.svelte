<script>
    import BoardLayout from "$BoardLayout";
    import PdfReader from "../../../../utils/PdfView.svelte";
    export let title = "";
</script>

<BoardLayout {title}>
    <PdfReader url="/assets/pdf/noDocentesConvenioFatun.pdf" />
</BoardLayout>
