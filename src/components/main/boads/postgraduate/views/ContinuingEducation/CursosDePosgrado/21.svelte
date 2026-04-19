<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "https://eco.unca.edu.ar/assets2/users/paginaeco/posgrado/Cursos de Posgrado/21_qr.png";
  export const courseTitle = "HISTORIA Y ESTRUCTURA ECONÓMICA REGIONAL";
  let startDate = "9 de abril de 2026";
  let modality = "Híbrida";
  let professors = [
    {
      name: "Dr. Jorge Luis Silveti (UNSE)",
    },
    {
      name: "Dr. Nicolás Hernández Aparicio (UNJU)",
    },
  ];

  let recipients = [
    "Profesionales graduados de carreras universitarias de más de 4 años de duración.",
  ];

  let objectives = [
    "Generar habilidades y actitudes que favorezcan la reflexión y el análisis de la estructura económica regional, teniendo en cuenta su formación histórica, las interacciones y significaciones de sus partes, los procesos dinámicos de transformación, los paradigmas dominantes y las instituciones imperantes de cada época. Para ello, se propone una revisión conceptual, teórica y metodológica de las diferentes estrategias de producción, acumulación, distribución y consumo implementadas desde 1930 hasta la actualidad.",
    "Trazar un cuadro de la economía argentina y regional del NOA basándose primordialmente en información empírica proveniente de investigaciones económicas y fuentes estadísticas y censales, centradas especialmente en las transformaciones operadas con posterioridad a 1930. Para ello, se considerarán la composición sectorial de la producción económica, el empleo, la estructura regional, la estratificación social, la dinámica poblacional, el sistema educativo y la dependencia externa del NOA.",
  ];

  let certification =
    "Certificado de aprobación o asistencia según corresponda.";

  let documentation = [
    "DNI, Pasaporte o Cédula Extranjera.",
    "Título de Grado o Certificado de Título en trámite.",
  ];

  let schedule = {
    totalClasses: 4,
    classDuration: "2 encuentros",
    meetings: [
      {
        title: "Encuentro 1",
        dates: ["9 de abril | 17 a 21 hs.", "10 de abril | 9 a 18 hs."],
      },
      {
        title: "Encuentro 2",
        dates: ["7 de mayo | 17 a 21 hs.", "8 de mayo | 9 a 18 hs."],
      },
    ],
  };

  let cost = {
    amount: "2 pagos de $70.000",
    bankDetails: {
      name: "UNIVERSIDAD NACIONAL DE CATAMARCA",
      cuit: "30-64187093-1",
      accountType: "CC $",
      accountNumber: "31554660219296",
      alias: "fceyaunca",
      cbu: "0110466420046602192961",
    },
  };

  let contacts = {
    area: "Unidad de Formación Continua | Secretaría de Posgrado",
    email: "formacioncontinua@eco.unca.edu.ar",
    address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
    inscriptionLink: "https://forms.gle/hHq2fUEw7A1vueJ79",
    paymentEmail: "mluduena@eco.unca.edu.ar",
    paymentSubject: 'Asunto: "PAGO"',
    paymentDetails:
      "Detallando Apellido y Nombres del Alumno, DNI y nombre del Curso a inscribirse.",
    documentationNote:
      "La documentación deberá ser enviada al correo electrónico indicando el nombre del curso.",
  };

  export let open = false;
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content" class="course-content">
    <h1>{courseTitle}</h1>
    <p><strong>Inicio:</strong> {startDate}</p>
    <p><strong>Modalidad:</strong> {modality}</p>

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

    <h2>Destinatarios</h2>
    <ul>
      {#each recipients as recipient}
        <li>{recipient}</li>
      {/each}
    </ul>

    <h2>Cronograma</h2>
    <div style="padding-left: 2rem;">
      {#each schedule.meetings as meeting}
        <p><strong>{meeting.title}</strong></p>
        {#each meeting.dates as date}
          <p>{date}</p>
        {/each}
      {/each}
    </div>

    <h2>Objetivos</h2>
    <ul class="objective-list">
      {#each objectives as objective}
        <li>{objective}</li>
      {/each}
    </ul>

    <h2>Certificación a Entregar</h2>
    <p>{certification}</p>

    <h2>Documentación a Enviar</h2>
    <ul>
      {#each documentation as document}
        <li>{document}</li>
      {/each}
    </ul>
    <p>
      La documentación deberá ser enviados al correo electrónico:
     <a href="mailto:formacioncontinua@eco.unca.edu.ar">formacioncontinua@eco.unca.edu.ar</a> Indicando el nombre del curso.
    </p>

    <h2>Valor del Curso</h2>
    <p>Valor del Curso: {cost.amount}</p>

    <h2>Datos Bancarios</h2>
    <p><strong>Nombre:</strong> {cost.bankDetails.name}</p>
    <p><strong>CUIT:</strong> {cost.bankDetails.cuit}</p>
    <p><strong>Tipo de cuenta:</strong> {cost.bankDetails.accountType}</p>
    <p><strong>Número de cuenta:</strong> {cost.bankDetails.accountNumber}</p>
    <p><strong>Alias:</strong> {cost.bankDetails.alias}</p>
    <p><strong>CBU:</strong> {cost.bankDetails.cbu}</p>
    <p>
      <strong>Envío de comprobante de pago:</strong>
      <a href="mailto:{contacts.paymentEmail}">{contacts.paymentEmail}</a>
    </p>
    <p><strong>{contacts.paymentSubject}</strong></p>
    <p>{contacts.paymentDetails}</p>
    <p>{contacts.documentationNote}</p>

    <h2>Inscripción</h2>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >

    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Código QR de inscripción" class="qr-image" />
    </div>

    <br />

    <h2>Contactos</h2>
    <p>{contacts.area}</p>
    <p>{contacts.address}</p>
    <p>Correo electrónico: <a href="mailto:{contacts.email}">{contacts.email}</a></p>
  </div>
</Accordion>

<style>
  .course-content {
    font-size: 1rem;
  }

  .course-content p,
  .course-content li {
    font-size: 1rem;
  }

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

  .objective-list {
    list-style: disc;
    padding-left: 1.25rem;
    margin: 0.5rem 0;
  }

  .objective-list li {
    margin-bottom: 0.35rem;
  }

  .qr-image {
    width: 180px;
    max-width: 100%;
    height: auto;
  }
</style>
