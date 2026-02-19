<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "/assets/posgrado/Cursos de Posgrado/17_qr.png";
  let imageUrl = null; //"/assets/posgrado/Cursos de Posgrado/17.jpg";
  export const courseTitle =
    "CUESTIONES ESPECIALES DE VALUACIÓN Y DETERMINACIÓN DE RESULTADOS";
  let startDate = "3 de octubre de 2025";
  let modality = "Virtual";
  let professors = [
    {
      name: "Mg. Ana María Campo",
     
    },
    {
      name: "Esp. Nestor H. Bursesi",
     
    },
  ];

   let objectivesSpecific = [
    "Comprender la incidencia de la coyuntura económica en la definición de los modelos contables.",
    "Conocer los factores que determinan las diferencias en la información contable en el ámbito nacional e internacional.",
    "Comprender las normas contables de medición (valuación) vigentes en el país sobre cuestiones de aplicación general y particular, comparándolas con las de otros países.",
    "Realizar el análisis crítico de la doctrina y las normas contables vigentes.",
    "Aplicar los conceptos adquiridos en la resolución de casos de situaciones reales y/o simuladas planteadas.",
    "Realizar trabajos de investigación en materia contable sobre cuestiones planteadas en los contenidos del módulo.",
  ];

  let analyticalContents = [
    "Los modelos contables: Conceptos fundamentales que los definen y temas conflictivos relacionados. Casos especiales de medición del patrimonio y la determinación de resultados.Otras mediciones contables. Patrimonio Neto y sus particularidades en la valuación.",
  ];

  let schedule = {
    totalClasses: 4,
    classDuration: "5 horas por encuentro",
    dates: [
      "Inicio: 3 de octubre de 2025",
      "Fechas: 3, 4, 31 de octubre; 1 de noviembre",
      "Horario: viernes de 16 a 21 hs; sábados de 8 a 13 hs",
    ],
    totalHours: "20 horas presenciales virtuales",
  };


  let cost = {
    paymentMethod: "Transferencia",
    bankDetails: {
      alias: "FCEyA.UNCA",
      accountNumber: "31554660081889",
      cbu: "0110466420046600818894",
      name: "FC.CS.ECON.Y ADM.",
      cuit: "30641870931",
    },
  };

  let contacts = {
    email: "formacioncontinua@eco.unca.edu.ar",
    address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
    inscriptionLink: "https://forms.gle/KACEyGdHZ2ZjaEYi7",
  };

  export let open = false;
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <!--
    <div class="animate-slide-in-up">
      <img
        src={imageUrl}
        alt="Imagen del curso Power BI"
        class="transition-all duration-300 hover:scale-105 w-full rounded-lg mb-4 ml-4 max-w-[800px]"
      />
    </div>-->
    <p>INICIO: {startDate} | MODALIDAD: {modality}</p>

    <h2>Docentes</h2>
    <ul class="professor-list">
      {#each professors as professor}
        <li class="professor-item">
          <div class="professor-info">
            <strong>{professor.name}</strong>          
          </div>
        </li>
      {/each}
    </ul>

    <h2>Objetivos</h2>  
    <h3>Específicos</h3>
    <ul>
      {#each objectivesSpecific as objective}<p>- {objective}</p>
        <br />{/each}
    </ul>

    <h2>Cronograma</h2>
    <div style="padding-left: 2rem;">
      {#each schedule.dates as date}<p>{date}</p>{/each}
      <p>Total de encuentros: {schedule.totalClasses}</p>
      <p>Duración: {schedule.classDuration}</p>
    </div>



    <h2>Contenidos Minimos</h2>
    <ul>
      {#each analyticalContents as content}
        <li><p>{content}</p></li>
        <br />
      {/each}
    </ul>

    <h2>Valor del Curso</h2>
    <div style="padding-left: 2rem;">
      <p>Valor: $60.000 (pago único)</p>
      <p>Forma de Pago: {cost.paymentMethod}</p>
      <p><strong>Datos Bancarios:</strong></p>
      <p>Alias: {cost.bankDetails.alias}</p>
      <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
      <p>CBU: {cost.bankDetails.cbu}</p>
      <p>Nombre: {cost.bankDetails.name}</p>
      <p>CUIT: {cost.bankDetails.cuit}</p>
      <p>
        Enviar comprobante a <a
          href="mailto:formacioncontinua@eco.unca.edu.ar"
          style="color:#007bff;text-decoration:none;"
          >formacioncontinua@eco.unca.edu.ar</a
        >
        detallando Apellido y nombre del alumno, nombre del curso a inscribirse.
      </p>
    </div>

    <h2>Inscripciones</h2>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >

    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Código QR de inscripción" />
    </div>

    <br />

    <h2>Contactos</h2>
    <p>Unidad de Formación Continua | Secretaría de Posgrado</p>
    <p>Email: {contacts.email}</p>
    <p>Dirección: {contacts.address}</p>
  </div>
</Accordion>

<style>
  h1 {
    font-weight: 600;
    font-family: "Merriweather", serif;
    font-size: 1.5rem;
    color: #6d0205;
    padding-top: 1rem;
  }
  h2 {
    font-family: "Merriweather", serif;
    font-weight: 600;
    font-size: 1.25rem;
    padding-top: 1rem;
    color: #7a1c0b;
  }

  .professor-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .professor-item {
    margin-bottom: 1.5rem;
    overflow: auto;
  }



  .professor-info {
    text-align: justify; /* Para que se vea más prolijo */
  }



</style>
