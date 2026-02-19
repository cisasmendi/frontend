<script>
    import PdfReader from "../../../utils/PdfView.svelte";
    export let title = "";
</script>

<div class="w-full lg:w-3/4 p-4">
    <h2 class="text-2xl font-semibold text-[#6d0205] mb-4">{title}</h2>
    <PdfReader url="/assets/pdf/infografiaInstitucional.pdf" />
</div>