<script>
    import PdfReader from "../../../utils/PdfView.svelte";
    export let title = "";
</script>

<div class="w-full lg:w-3/4 p-4">
    <h2 class="text-2xl font-semibold text-[#6d0205] mb-4">{title}</h2>
    <PdfReader url="https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/infografiaInstitucional.pdf" />
</div>