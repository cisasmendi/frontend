
<script>
  // @ts-ignore
  import Accordion from "$utilsMain/Accordion.svelte";
  export let open = false;
  export const courseTitle =
       "Diplomatura en Bibliotecología";
  let startDate = "INICIO DE CLASES 06 AGOSTO 2024 ";
  let modality = "Modalidad A Distancia";
  

</script>

<Accordion
  title={"Diplomatura en Bibliotecología"}
  isOpen={open}
>
  <div slot="content">     
       <h1>{courseTitle}</h1>
       <p>
            <strong>Inicio de Clases:</strong>
            {startDate} | <strong>Modalidad:</strong>
            {modality}
       </p>

  </div>
</Accordion>

<style>
  h1 {
       /*text-lg font-semibold text-[#6d0205]*/
       font-weight: 600;

       font-family: "Merriweather", serif;
       font-size: 1.5rem;
       color: #6d0205;
       padding-top: 1rem;
  }

 
</style>
