<script>
    import PdfViewer from 'svelte-pdf';


    // Usa un worker desde una CDN


    export let url = '';
    const showButtons = ["navigation", "zoom", "print","pageInfo",];
</script>

  
    <PdfViewer {url} {showButtons} data={null} 
     showBorder={false}/>
