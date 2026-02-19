<script>
    import Accordion from "$utilsMain/Accordion.svelte";
  

    let qrCode = "/assets/posgrado/Cursos de Posgrado/11_qr.png";
  
    export const courseTitle = "Formulación, Análisis y Evaluación de Proyectos";
    let startDate = "3 de abril de 2025";
    let modality = "Híbrida";
    let professors = ["Esp. Natalia Martini"];
  
    let objectivesGeneral = "Proporcionar las bases conceptuales de la herramienta formulación y evaluación de proyectos, fortaleciendo habilidades y competencias profesionales.";
    let objectivesSpecific = [
      "Desarrollar el aprendizaje de herramientas de diagnóstico e identificación de proyectos.",
      "Comprender y aplicar los distintos estudios de formulación y evaluación de proyectos.",
      "Identificar, formular y evaluar un proyecto a lo largo del curso."
    ];

    let analyticalContents = [
    "Unidad I: Toma de Decisiones Económicas. Proyectos de Inversión Proceso estructurado para la toma de decisiones. Distintos modelos. Como tomar decisiones acertadas. Errores frecuentes cuando se toman decisiones. Importancia de la toma de decisiones en los proyectos de inversión. Proyectos de inversión. Introducción. Concepto. Clasificación. Conceptos de for-mulación y evaluación de proyectos. Enfoques en la evaluación de proyectos: eva-luación privada y evaluación pública. Distintas etapas en la formulación y evalua-ción de proyectos. Identificación de la idea. Etapa de preinversión. Etapa de inver-sión. Ejecución del proyecto.",
    "Unidad II: Preparación y Evaluación de un Proyecto de Inversión Recopilación de la información. Antecedentes. Distintos estudios: legal, de merca-do, técnico organizacional y económico financiero.Estudio Legal: formas jurídicas, contratos. Impacto en el estudio económico. Estudio de mercado: Conceptos económicos básicos para el análisis de inversiones. Análisis de la demanda, oferta y comportamiento de los costos. Estudio de los dis-tintos mercados: proveedor, competidor, distribuidor y consumidos. Estudio técnico-organizacional: Localización. Proceso de producción. Descripción de la tecnología a utilizar. Capacidad productiva: tamaño. Programa de producción. Requerimientos de Servicios. Proceso administrativo. Funciones administrativas. Instrumentos administrativos. Requerimientos de personal. Estudio económico- financiero: Inversiones iniciales: inversiones fijas, intangibles y en capital de trabajo. Métodos para el cálculo del capital de trabajo. Ingresos: cla-sificación. Egresos: clasificación. Valor residual: métodos de cálculo. Tratamiento de las depreciaciones y amortizaciones. Financiamiento de un proyecto. Punto de equilibrio. Conocimientos básicos de Matemática Financiera: Su objeto de estudio. El valor tiempo del dinero. Operaciones Financieras, la colocación y toma de fondos. Teoría del interés. Interés y tasa de interés. Operaciones fundamentales de capitalización y actualización. Las rentas ciertas: concepto financiero. Valor actual y final de las rentas ciertas. Sistemas de Amortización o extinción de préstamos. Cálculo de indicadores de rentabilidad: Métodos que tienen en cuenta el valor tem-poral del dinero. Valor Actual Neto (VAN), Tasa Interna de Retorno (TIR) (distin-tas variantes). Relación Beneficio/Costo Ajustado y Periodo de Recupero de la In-versión Ajustado.",
    "Unidad III: Proyectos de Interés Público – Proyectos Sociales Planeamiento estratégico. Diferencias entre plan, programa, proyecto, actividad y tarea. Definición de proyectos. Ciclo de vida de un proyecto. Actores sociales. Aná-lisis de la idea. Diseño a nivel de perfil. Estudio organizacional. Tipos de proyectos. Evaluación de proyectos de interés público. Requisitos para la buena formulación de un proyecto. Guía de presentación."
  ];
  
    let schedule = {
      totalClasses: 6,
      classDuration: "4 hs",
      dates: ["3, 4, 10, 11, 24, 25 de abril"],
      totalHours: 24,
      platform: "Modalidad híbrida"
    };
  
    let methodology = [
      "Clases magistrales dialogadas.",
      "Uso de procesadores de cálculo para evaluación de proyectos.",
      "Trabajo en talleres y discusión grupal.",
      "Uso de Excel para cálculos financieros."
    ];
  
    let evaluationCriteria = [
      "Examen final integrado, teórico y práctico.",
      "Asistencia al 80% de las clases.",
      "Aprobación con nota mínima de 5 (escala 1 a 10)."
    ];
  
    let targetAudience = [
      "Profesionales graduados de carreras universitarias de más de 4 años de duración."
    ];
  
    let admissionRequirements = [
      "DNI, Pasaporte o Cédula Extranjera.",
      "Título de Grado o Certificado de Título en trámite."
    ];
  
    let expectedOutcomes = "Adquirir capacidades para aplicar modelos de evaluación de proyectos de inversión en organizaciones estatales y privadas.";
  
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
      inscriptionLink: "https://acortar.link/murk72"
    };
  
    let inscriptionDeadline = "3 de abril de 2025";
    export let open = false; // Controla si el acordeón está abierto o cerrado
  </script>
  
<Accordion title={courseTitle} isOpen={open}>
    <div slot="content">    
  
      <h1>{courseTitle}</h1>
      <p>INICIO DE CLASES: {startDate} | {modality}</p>
  
      <h2>Docente a cargo</h2>
      <ul>{#each professors as professor}<li>{professor}</li>{/each}</ul>
  
        <h2>Programación de Actividades y Carga Horaria</h2>
      <p>Fecha de inicio: {startDate}. Modalidad híbrida. Fechas: {schedule.dates.join(', ')}. Carga horaria total: {schedule.totalHours} hs.</p>

      <h2>Objetivos</h2>
      <h3>Objetivo General</h3>
      <p>{objectivesGeneral}</p>
      <h3>Objetivos Específicos</h3>
      <ul>{#each objectivesSpecific as objective}<li>{objective}</li>{/each}</ul>
  
    
  
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

      <h2>Contenidos Analíticos</h2>
      <ul>{#each analyticalContents as content}<li>{@html content}</li> <br>{/each}</ul>
  
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
  