<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "/assets/posgrado/Cursos de Posgrado/18_qr.png";
  let imageUrl = null; //"/assets/posgrado/Cursos de Posgrado/18.jpg";
  export const courseTitle = "AUDITORÍA DE ESTADOS CONTABLES";
  let startDate = "7 de noviembre de 2025";
  let modality = "Híbrida";
  let professors = [
    {
      name: "Mg. Susana Abram",
     // descript: "Magister especialista en Auditoría de Estados Contables y control interno.",
    },
  ];

  let objectivesGeneral = "Orientado a la actualización, mejoramiento y especialización de la práctica del profesional que actúa en el campo de la Auditoría, presentando, desarrollando y poniendo bajo análisis las modernas metodologías aplicadas, la utilización de las herramientas incorporadas por las innovaciones tecnológicas, el marco de Normas Nacionales e Internacionales, el marco ético profesional, la responsabilidad legal y los aspectos contables relevantes. Para el cumplimiento de los objetivos señalados, luego de analizar los lineamientos generales de la Auditoría, de la actuación del profesional en estas especialidades y el rol que éste debe cumplir en una organización, se presentarán y discutirán procedimientos para el conocimiento y desarrollo de las disposiciones normativas y metodológicas. Se analizarán los conceptos y disposiciones de más reciente adopción, incorporados en las Normas Contables y en las de Auditoría, los más relevantes tratados en las Normas Nacionales e Internacionales y los que se encuentran bajo análisis para ser reformados. Para el logro de los objetivos propuestos, se indicarán las fuentes de información, entregando guías y material y se generarán los ambientes de discusión aconsejables para el desarrollo académico – temático. Se incursionará en contextos privados y públicos."
   let objectivesSpecific = [
    "Reconocer la profesión del auditor, así como las cualidades que el mismo debe poseer.",
    "Analizar el proceso de auditoría y sus etapas.",
    "Identificar la responsabilidad social, civil y penal del auditor.",
    "Reconocer la importancia del control interno, sus diferentes formas, así como las forma de revisar de manera formal y real el mismo.",
    "Analizar los diferentes tipos de informes de auditoría, así como los problemas que pueden ocurrir durante el proceso de auditoría y sus consecuencias en los mencionados informes.",
  ];

  let analyticalContents = [
    "Relaciones fundamentales: la auditoría y la profesión de Contador.",
    "La auditoría de Estados Financieros, aceptación y planeación de la auditoría.",
    "Obtención de las evidencias, enfoque de sistemas versus enfoque de riesgo.",
    "Consideraciones respecto a la estructura del control interno.",
    "Auditoría por ciclos, muestreo en pruebas de controles y en pruebas sustantivas de operaciones.",
    "Informes, distintos tipos y casos. Hechos posteriores.",
  ];

  let schedule = {
    totalClasses: 4,
    classDuration: "5 horas por encuentro",
    dates: [
      "Inicio: 7 de noviembre de 2025",
      "Fechas: 7, 8, 14, 15 de noviembre",
      "Horario: viernes de 16 a 21 hs; sábados de 8 a 13 hs",
    ],
    totalHours: "20 horas presenciales (modalidad híbrida)",
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
    inscriptionLink: "https://forms.gle/WJFHsC6c9d5X3yiM9",
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
            {#if professor.descript}
              <p>{professor.descript}</p>
            {/if}
          </div>
        </li>
      {/each}
    </ul>

    <h2>Objetivos</h2>
    <h3>General</h3>
    <p>{objectivesGeneral}</p>
    <br />
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
      <p>Carga horaria total: {schedule.totalHours}</p>
    </div>



    <h2>Contenidos Analíticos</h2>
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

  .professor-info p {
    margin: 0 0 0;
  }
</style>
