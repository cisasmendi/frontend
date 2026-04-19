<script >
    import PdfReader from "../../../utils/PdfView.svelte";
    import BoardLayout from "$BoardLayout";
    let url = "";

    export let items = [
        {
            title: "",
            Files: [
                {
                    subtitle: "Convocatoria Elecciones Consejeros 2023-2025",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/ResolucionCD-FCEyA-010-23.pdf",
                },
            ],
        },
        {
            title: "Acta de Escrutinio Definitivo y Proclamacion de Candidatos",
            Files: [
                {
                    subtitle: "Proclamación Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/proclamaDocentes.pdf",
                },
                {
                    subtitle: "Proclamación Estudiantes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/proclamaEstudiantes.pdf",
                },
                {
                    subtitle: "Proclamación No Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/proclamaNoDocente.pdf",
                },
                {
                    subtitle: "Proclamación Egresados",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/proclamaEgresados.pdf",
                },
            ],
        },
        {
            title: "Oficialización de Votos",
            Files: [
                {
                    subtitle: "Acta N° 6",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/ActaN6.pdf",
                },
            ],
        },
        {
            title: "Fijación del Día y Hora de Elecciones",
            Files: [
                {
                    subtitle: "Acta N° 5",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/ActaN5.pdf",
                },
            ],
        },
        {
            title: "Exhibición de Listas",
            Files: [
                {
                    subtitle: "Acta N° 4",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/ActaN4.pdf",
                },
                {
                    subtitle: "Acta N° 3",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/ActaN3.pdf",
                },
                {
                    subtitle: "Listado Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/listaDocentes.pdf",
                },
                {
                    subtitle: "Listado Estudiantes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/listaEstudiantes.pdf",
                },
                {
                    subtitle: "Listado No Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/listaNoDocentes.pdf",
                },
                {
                    subtitle: "Listado Egresados",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/listaEgresados.pdf",
                },
            ],
        },
        {
            title: "Publicación de Padrones Definitivos",
            Files: [
                {
                    subtitle: "Acta N° 2",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/ActaN2.pdf",
                },
                {
                    subtitle: "Claustro Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroDocentes.pdf",
                },
                {
                    subtitle: "Claustro Estudiantes Contador Público",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroEstudiantesCP.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Administración",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroEstudiantesLADM.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Pública",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroEstudiantesLGP.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Educación Superior",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroEstudiantesLGES.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Tecnicatura en Administración de la Educación Superior",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroEstudiantesTAES.pdf",
                },
                {
                    subtitle: "Claustro No Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroNoDocentes.pdf",
                },
                {
                    subtitle: "Claustro Egresados",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/claustroEgresados.pdf",
                },
            ],
        },
        {
            title: "Publicación de Padrones Provisorios",
            Files: [
                {
                    subtitle: "Acta N° 1",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/01-actaN1.pdf",
                },
                {
                    subtitle: "Claustro Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/02-claustroDocentes.pdf",
                },
                {
                    subtitle: "Claustro Estudiantes Contador Público",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/03-claustroEstudiantesCP.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Administración",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/04-claustroEstudiantesLADM.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Pública",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/05-claustroEstudiantesLGP.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Licenciatura en Gestión Educación Superior",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/06-claustroEstudiantesLGES.pdf",
                },
                {
                    subtitle:
                        "Claustro Estudiantes Tecnicatura en Administración de la Educación Superior",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/07-claustroEstudiantesTAES.pdf",
                },
                {
                    subtitle: "Claustro No Docentes",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/08-claustroNoDocente.pdf",
                },
                {
                    subtitle: "Claustro Egresados",
                    url: "https://eco.unca.edu.ar/assets2/users/paginaeco/pdf/consejeros/09-claustroEgresados.pdf",
                },
            ],
        },
    ];

    function handleClick(file) {
        console.log("🚀 ~ handleClick ~ file:", file);
        url = file.url;
    }
    function handleBack() {
        url = "";
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

<BoardLayout title={"Consejeros 2023-2025"}>
    {#if url !== ""}
        <div>
            <button
                on:click={handleBack}
                class="bg-[#6d0205] text-white py-2 px-4 rounded mb-4"
            >
                Atras
            </button>
            <PdfReader {url} />
        </div>
    {:else}
        <div class="p-4">
            {#each items as item}
                <h3 class="text-lg font-bold text-[#6d0205] mb-2">
                    {item.title}
                </h3>
                {#if item.Files}
                    <ul class="list-disc ml-4 mb-4">
                        {#each item.Files as file}
                        <li class="flex items-center gap-2">
                         
                            <!-- svelte-ignore a11y_invalid_attribute -->
                            <a
                                href="#" 
                                class="text-[#555555] hover:text-[#942c2e] cursor-pointer"
                                aria-label="Ver archivo {file.subtitle}"
                            >
                                {file.subtitle}
                            </a>
                        
                            <button
                                on:click={() => handleClick(file)}
                                class="cursor-zoom-in flex items-center gap-1"
                                aria-label="Ver archivo"
                            >
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.94 4.94a3 3 0 01-4.24 4.24L10 15m5-5L9 4m6 6l6 6"></path>
                                </svg>
                                Ver
                            </button>
                        
                            <button
                                on:click={() => descargarPdf(file.url)}
                                class="cursor-pointer flex items-center gap-1"
                                aria-label="Descargar archivo"
                            >
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2M8 12l4 4m0 0l4-4m-4 4V4"></path>
                                </svg>
                                Descargar
                            </button>
                      
                        
                    </li>
                    
                        {/each}
                    </ul>
                {/if}
            {/each}
        </div>
    {/if}
</BoardLayout>
