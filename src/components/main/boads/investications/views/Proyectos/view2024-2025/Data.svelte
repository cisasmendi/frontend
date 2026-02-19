<script lang="ts">
// @ts-nocheck

import Accordion from "$utilsMain/Accordion.svelte";

export let data = {
    periodo: "",
    proyectos: {}
};

let periodo = data.periodo;
let tiposDeProyectos = Object.entries(data.proyectos);
</script>

{#each tiposDeProyectos as [tipo, proyectos]}
    <Accordion title={tipo}>
        <div slot="content">
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {#each proyectos as p}
                    <div class="border p-4 rounded-lg shadow-md">
                        <h3 class="text-xl font-semibold text-[#6d0205]">{p.titulo}</h3>

                        {#if p.director}
                            <p><strong>Director:</strong> {p.director}</p>
                        {:else if p.responsable}
                            <p><strong>Responsable:</strong> {p.responsable}</p>
                        {:else if p.responsables}
                            <p><strong>Responsables:</strong> {p.responsables.join(", ")}</p>
                        {/if}

                        {#if p.contacto}
                            <p><strong>Contacto:</strong> {p.contacto}</p>
                        {:else if p.contactos}
                            <p><strong>Contactos:</strong> {p.contactos.join(", ")}</p>
                        {/if}

                        {#if p.referentes}
                            <p><strong>Referentes:</strong></p>
                            <ul class="list-disc list-inside">
                                {#each p.referentes as r}
                                    <li>{r.nombre} - {r.contacto}</li>
                                {/each}
                            </ul>
                        {/if}

                        {#if p.sector_asociado}
                            <p><strong>Sectores Asociados:</strong></p>
                            <ul class="list-disc list-inside">
                                {#each p.sector_asociado as s}
                                    <li>{s}</li>
                                {/each}
                            </ul>
                        {/if}
                    </div>
                {/each}
            </div>
        </div>
    </Accordion>
    <br>
{/each}
