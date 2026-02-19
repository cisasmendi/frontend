<script>
  import PdfReader from "../../../utils/PdfView.svelte";
  export let title = "";
  // @ts-ignore
  import BoardLayout from "$BoardLayout";
  let listaPdf = [
    {
      titulo:
        "Oficina de Orientación al Emprendedor (Resolución FCEYA 161/2014)",
      pdfs: [ //Informe Anual 2024 - Oficina de Orientación
       {
          nombre: "Resultados 2024",
          url: "/assets/pdf/extension/Informe Anual 2024 - Oficina de Orientación.pdf",
        },
        {
          nombre: "Resultados 2023",
          url: "/assets/pdf/extension/Orientaci%C3%B3nEmprendedorResultados2023.pdf",
        },
        {
          nombre: "Resultados 2022",
          url: "/assets/pdf/extension/Orientaci%C3%B3nEmprendedorResultados2022.pdf",
        },
        {
          nombre: "Resultados 2021",
          url: "/assets/pdf/extension/Orientaci%C3%B3nEmprendedorResultados2021.pdf",
        },
        {
          nombre: "Resultados 2020",
          url: "/assets/pdf/extension/Orientaci%C3%B3nEmprendedorResultados2020.pdf",
        },
        {
          nombre: "Resultados 2019",
          url: "/assets/pdf/extension/Orientaci%C3%B3nEmprendedorResultados2019.pdf",
        },
        {
          nombre: "Resultados 2018",
          url: "/assets/pdf/extension/Orientaci%C3%B3nEmprendedorResultados2018.pdf",
        },
      ],
    },
    {
      titulo: "Cátedra Abierta para Emprendedores Universitarios",
      pdfs: [
        {
          nombre: "Resultados 2019",
          url: "/assets/pdf/extension/informeCatedraAbierta2019.pdf",
        },
        {
          nombre: "Resultados 2018",
          url: "/assets/pdf/extension/informeCatedraAbierta2018.pdf",
        },
      ],
    },
  ];

  let selectedCategory = listaPdf[0];
  let pdfSeleccionado = selectedCategory.pdfs[0].url;

  let unique = [{}];

  function selectPdf(category, pdfUrl) {
    selectedCategory = category;
    pdfSeleccionado = pdfUrl;
    unique = [{}];
  }
  function descargarPdf(pdfUrl) {
    const link = document.createElement("a");
    link.href = pdfUrl;
    link.download = pdfUrl.split("/").pop(); // Usa el nombre del archivo para la descarga
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
</script>

<BoardLayout {title}>
  {#each listaPdf as category}
    <section class="section">
      <h2 class="title">{category.titulo}</h2>
      <ul class="pdf-list list-disc pl-5">
        {#each category.pdfs as pdf}
          <li>
            <button
              on:click={() => selectPdf(category, pdf.url)}
              class="pdf-link"
            >
              {pdf.nombre}
            </button>
            <button
              on:click={() => descargarPdf(pdf.url)}
              class="download-button"
            >
              Descargar
            </button>
          </li>
        {/each}
      </ul>
    </section>
  {/each}
  {#each unique as key (key)}
    <PdfReader url={pdfSeleccionado} />
  {/each}
</BoardLayout>

<style>
  .section {
    margin-bottom: 2rem;
  }
  .title {
    color: #6d0205;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }
  .pdf-link {
    margin-right: 0.5rem;
    color: #0056b3;
    cursor: pointer;
    text-decoration: underline;
    background: none;
    border: none;
    font-size: 1rem;
  }
  .download-button {
    color: #007bff;
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1rem;
  }
</style>
