<script>
    import { onMount } from "svelte";
   // @ts-ignore
    import data from "./Data/TUAC.csv";

    let groupedData = [];

    onMount(() => {
        // Agrupar los datos por 'Año'
        groupedData = data.reduce((acc, item) => {
            const { Año } = item;
            if (!acc[Año]) {
                acc[Año] = [];
            }
            acc[Año].push(item);
            return acc;
        }, {});       
    });
</script>

{#each Object.keys(groupedData) as year}
    <br />
    {#if year == "Nota"}
        <table>
            <thead>
                <tr>
                    <th colspan="6">{year}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                   
                </tr>
                {#each groupedData[year] as { Código, Asignatura, Horas_Sem, Horas_Tot, Correlatividades, Cuatrimestre, URL }}
                    <tr>
                        <td>{Código}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {:else}
        <table>
            <thead>
                <tr>
                    <th colspan="6">{year}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th>Código</th>
                    <th>Asignatura</th>
                    <th>Horas/Sem</th>
                    <th>Horas/Tot</th>
                    <th>Correlatividades</th>
                    <th>Cuatrimestre</th>
                </tr>

                {#each groupedData[year] as { Código, Asignatura, Horas_Sem, Horas_Tot, Correlatividades, Cuatrimestre, URL }}
                    <tr>
                        <td>{Código}</td>
                        <td>
                            {#if URL != ""}
                                <a href={URL} target="_blank">
                                    <i class="fas fa-download"></i>
                                    {Asignatura}
                                </a>
                            {:else}{Asignatura}{/if}
                        </td>
                        <td>{Horas_Sem}</td>
                        <td>{Horas_Tot}</td>
                        <td>{Correlatividades}</td>
                        <td>{Cuatrimestre}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {/if}
{/each}
