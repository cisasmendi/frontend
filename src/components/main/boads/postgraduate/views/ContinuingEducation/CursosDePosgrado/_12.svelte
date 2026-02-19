<script>
    import Accordion from "$utilsMain/Accordion.svelte";

    let qrCode = "/assets/posgrado/Cursos de Posgrado/12_qr.png";
  
    export const courseTitle = "Taller de Elaboración del Trabajo Final";
    let startDate = "8 de mayo de 2025";
    let modality = "Híbrida";
    let professors = ["Esp. Raúl Mura"];
  
    let objectivesGeneral = "Guiar a los estudiantes en la elaboración del Trabajo Final Integrador, abordando metodologías de desarrollo de proyectos profesionales.";
    let objectivesSpecific = [
      "Identificación de la problemática y elección del tema.",
      "Desarrollo del marco teórico y metodología del trabajo.",
      "Redacción, análisis de datos y formulación de conclusiones y propuestas."
    ];
  
    let schedule = {
      totalClasses: 4,
      classDuration: "4 hs",
      dates: ["8, 9, 15, 16 de mayo"],
      totalHours: 16,
      platform: "Modalidad híbrida"
    };
  
    let analyticalContents = [
      "Unidad I: Identificación de la problemática, elección del tema, objetivos y plan de trabajo.",
      "Unidad II: Técnicas de redacción de informes y requisitos formales para trabajos de investigación.",
      "Unidad III: Análisis de casos de producción de Trabajos Finales Integradores y reglamentación.",
      "Unidad IV: Presentación y debate grupal de las propuestas de los alumnos como Proyecto de Trabajo Final Integrador."
    ];
  
    let methodology = [
      "Exposición dialogada y lectura de casos.",
      "Búsqueda exploratoria en internet y consulta bibliográfica.",
      "Construcción grupal o individual de informes profesionales.",
      "Práctica de redacción académica y debate grupal de ideas para el trabajo final."
    ];
  
    let evaluationCriteria = [
      "Presentación del proyecto de un Trabajo Final Integrador.",
      "Asistencia al 80% de las clases.",
      "Aprobación del trabajo final del curso."
    ];
  
    let targetAudience = [
      "Profesionales graduados de carreras universitarias de más de 4 años de duración."
    ];
  
    let admissionRequirements = [
      "DNI, Pasaporte o Cédula Extranjera.",
      "Título de Grado o Certificado de Título en trámite."
    ];
  
    let expectedOutcomes = "Elaborar un Trabajo Final Integrador sólido, aplicando herramientas de investigación y redacción académica.";
  
    let cost = {
      paymentAmount: "$60.000",
      paymentMethod: "Transferencia",
      bankDetails: {
        alias: "FCEyA.UNCA",
        accountNumber: "31554660081889",
        cbu: "0110466420046600818894",
        name: "FC.CS.ECON.Y ADM.",
        cuit: "30641870931"
      }
    };
  
    let contacts = {
      email: "formacioncontinua@eco.unca.edu.ar",
      address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
      inscriptionLink: "https://acortar.link/IgrYE1"
    };
  
    let inscriptionDeadline = "8 de mayo de 2025";
  </script>
  
<Accordion title={courseTitle} isOpen={open}>
    <div slot="content">
    
  
      <h1>{courseTitle}</h1>
      <p>INICIO DE CLASES: {startDate} | {modality}</p>
  
      <h2>Docente a cargo</h2>
      <ul>{#each professors as professor}<li>{professor}</li>{/each}</ul>
  
      <h2>Objetivos</h2>
      <h3>Objetivo General</h3>
      <p>{objectivesGeneral}</p>
      <h3>Objetivos Específicos</h3>
      <ul>{#each objectivesSpecific as objective}<li>{objective}</li>{/each}</ul>
  
      <h2>Programación de Actividades y Carga Horaria</h2>
      <p>Fecha de inicio: {startDate}. Modalidad híbrida. Fechas: {schedule.dates.join(', ')}. Carga horaria total: {schedule.totalHours} hs.</p>
  
      <h2>Contenidos Analíticos</h2>
      <ul>{#each analyticalContents as content}<li>{content}</li>{/each}</ul>
  
      <h2>Metodología</h2>
      <ul>{#each methodology as method}<li>{method}</li>{/each}</ul>
  
      <h2>Modalidad de Evaluación</h2>
      <ul>{#each evaluationCriteria as criterion}<li>{criterion}</li>{/each}</ul>
  
      <h2>Destinatarios</h2>
      <ul>{#each targetAudience as audience}<li>{audience}</li>{/each}</ul>
  
      <h2>Requisitos de Admisión</h2>
      <ul>{#each admissionRequirements as requirement}<li>{requirement}</li>{/each}</ul>
  
      <h2>Resultados Esperados</h2>
      <p>{expectedOutcomes}</p>
  
      <h2>Costos</h2>
      <p>Un (1) pago de {cost.paymentAmount}.</p>
      <p>Formas de Pago: {cost.paymentMethod}</p>
      <p><strong>Datos Bancarios:</strong></p>
      <p>Alias: {cost.bankDetails.alias}</p>
      <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
      <p>CBU: {cost.bankDetails.cbu}</p>
      <p>Nombre: {cost.bankDetails.name}</p>
      <p>CUIT: {cost.bankDetails.cuit}</p>
  
      <h2>Inscripciones</h2>
      <p>Reservá tu cupo hasta el {inscriptionDeadline}.</p>
      <a href={contacts.inscriptionLink} target="_blank"  style="color:blue">► FORMULARIO DE INSCRIPCIÓN</a>
  
      <div class="animate-slide-in-up">
        <img src={qrCode} alt="Código QR de inscripción" />
      </div>
  
      <h2>Contactos</h2>
      <p>Unidad de Formación Continua. Secretaría de Posgrado</p>
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
  </style>
  