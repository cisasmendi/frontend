<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "https://eco.unca.edu.ar/assets2/users/paginaeco/posgrado/Cursos de Posgrado/22_qr.png";
  export const courseTitle = "PROGRAMA EJECUTIVO EN COMERCIO EXTERIOR";
  let startDate = "29 de abril de 2026";
  let modality = "Virtual";
  let duration = "10 clases";
  let focus = "Teórico-práctico";
  let methodology = "Análisis de casos reales + resolución de errores. Lenguaje accesible";
  let scheduleInfo = "Miércoles de 19 a 21 hs.";
  let professors = [
    {
      name: "Abog. Lorena Bartomioli",
      descript:
        "Abogada, especialista en Derecho Aduanero. Graduada con Honores en la Facultad de Derecho y Ciencias Sociales de la Universidad de Buenos Aires (Argentina) y posgraduada en Negocios Internacionales por la Universidad Católica Argentina. Docente universitaria. Miembro de la Academia Internacional de Derecho Aduanero, del Instituto Argentino de Estudios Aduaneros, de la Comisión de Derecho Aduanero del Centro de Estudios de Derecho Financiero y Tributario de la Facultad de Derecho de la Universidad de Buenos Aires y de la Asociación Argentina de Estudios Fiscales. Co-coordinadora de la Comisión de Derecho Aduanero de la Asociación Argentina de Estudios Fiscales. Vicepresidenta de la Asociación de Derecho Aduanero y Comercio Exterior (ADACE). Secretaria de Asuntos Jurisdiccionales del Tribunal Fiscal de la Nación de la República Argentina.",
    },
  ];

  let recipients = [
    "Personal de empresas importadoras y exportadoras.",
    "Responsables de áreas comerciales, administrativas o de compras.",
    "Emprendedores y pymes con proyección internacional.",
    "Profesionales que deseen incorporar herramientas de comercio exterior.",
    "Personas interesadas en iniciarse en la operatoria del comercio internacional.",
  ];

  let objectives = [
    "Comprender los conceptos esenciales del comercio exterior.",
    "Identificar los elementos jurídicos y operativos de una importación y una exportación.",
    "Conocer las destinaciones aduaneras y su función dentro de la operatoria.",
    "Interpretar el marco normativo básico aplicable.",
    "Reconocer la documentación principal de las operaciones y los errores más frecuentes.",
    "Incorporar nociones introductorias sobre clasificación arancelaria, valoración y tributación aduanera.",
    "Desarrollar una mirada práctica orientada a la prevención de contingencias.",
  ];

  let participantProfile =
    "El programa está dirigido a personas que necesiten adquirir una visión clara, ordenada y práctica del comercio exterior, ya sea desde una función empresarial, operativa, administrativa, comercial o de asesoramiento.";

  let certificationIntro = "Al finalizar el cursado se entregarán:";
  let certificationItems = [
    "Certificados de asistencia a quienes completen la cursada.",
    "Certificados de aprobación a quienes, además, aprueben el curso.",
  ];
  let certificationNote =
    "La certificación se emitirá como actividad de posgrado para los participantes que acrediten carreras de grado con una duración mínima de cuatro (4) años. En los demás casos, se otorgará constancia de curso de capacitación.";

  let documentation = [
    "DNI, Pasaporte o Cédula Extranjera.",
    "Título de corresponder.",
  ];

  let schedule = {
    totalClasses: 10,
    classDuration: scheduleInfo,
    meetings: [
      {
        title: "Clase 1. Presupuestos básicos de las operaciones de comercio exterior",
        dates: [
          "Concepto de comercio exterior.",
          "Qué significa importar.",
          "Qué significa exportar.",
          "Concepto de mercadería.",
          "Concepto de territorio aduanero. Zonas francas.",
          "Importancia de estos conceptos como base de toda operatoria.",
          "Acuerdos internacionales que impactan en el comercio exterior.",
          "Primer acercamiento a la lógica de circulación internacional de bienes.",
        ],
      },
      {
        title: "Clase 2. Marco normativo del comercio exterior",
        dates: [
          "Marco normativo interno.",
          "Código Aduanero y normas complementarias.",
          "Organismos que intervienen en el comercio exterior.",
          "Acuerdo General sobre Aranceles Aduaneros y Comercio (GATT).",
          "Acuerdos de integración regional.",
          "Impacto del marco normativo en las operaciones de comercio exterior.",
        ],
      },
      {
        title: "Clase 3. Sujetos y operadores del comercio exterior",
        dates: [
          "Importador y exportador.",
          "Despachante de aduana.",
          "Agentes de transporte aduanero.",
          "Depositarios y auxiliares del comercio y del servicio aduanero.",
          "Intervención de bancos, aseguradoras y otros actores.",
          "Distribución de roles y responsabilidades.",
        ],
      },
      {
        title: "Clase 4. Destinaciones aduaneras de importación y exportación",
        dates: [
          "Concepto de destinación aduanera.",
          "Importancia de las destinaciones para comprender qué es importar y exportar.",
          "Destinación definitiva de importación.",
          "Destinaciones suspensivas de importación.",
          "Destinación definitiva de exportación.",
          "Destinaciones suspensivas de exportación.",
          "Finalidad económica y jurídica de cada destinación.",
          "Relación entre destinación, mercadería y control aduanero.",
        ],
      },
      {
        title: "Clase 5. Documentación comercial y aduanera",
        dates: [
          "Factura comercial.",
          "Lista de empaque.",
          "Documento de transporte.",
          "Certificados de origen.",
          "Certificados sanitarios u otros documentos exigibles según la mercadería.",
          "Documentación complementaria.",
          "Función de cada documento dentro de la operación.",
          "Coherencia documental y trazabilidad.",
        ],
      },
      {
        title: "Clase 6. Errores documentales y contingencias frecuentes",
        dates: [
          "Errores en la descripción de la mercadería.",
          "Diferencias entre factura, packing list y documento de transporte.",
          "Omisiones documentales.",
          "Inconsistencias en cantidades, pesos y valores.",
          "Errores de origen.",
          "Consecuencias operativas y aduaneras de los errores documentales.",
          "Buenas prácticas para su prevención.",
        ],
      },
      {
        title: "Clase 7. Clasificación arancelaria",
        dates: [
          "Qué es la clasificación arancelaria.",
          "Función del Sistema Armonizado.",
          "Nomenclatura Común del Mercosur.",
          "Estructura básica de una posición arancelaria.",
          "Relevancia práctica de la clasificación.",
          "Impacto en tributos, restricciones y documentación.",
          "Problemas frecuentes de clasificación.",
        ],
      },
      {
        title: "Clase 8. Valor en aduana",
        dates: [
          "Noción básica de valor en aduana.",
          "Diferencia entre valor comercial y valor aduanero.",
          "Importancia del valor en la determinación tributaria.",
          "Elementos que inciden en el valor.",
          "Ajustes básicos.",
          "Riesgos frecuentes vinculados a la documentación del valor.",
        ],
      },
      {
        title: "Clase 9. Tributos del comercio exterior",
        dates: [
          "Derechos de importación.",
          "Derechos de exportación.",
          "Tasa de estadística.",
          "IVA, Ganancias e impuestos internos en su vinculación con la importación.",
          "Percepciones.",
          "Incidencia tributaria en el costo de la operación.",
          "Relación entre clasificación, valor y tributación.",
        ],
      },
      {
        title: "Clase 10. Cierre integrador del programa con participación dinámica de los participantes",
        dates: [
          "Lectura integral de la operación.",
          "Identificación de etapas críticas.",
          "Relación entre mercadería, destinación, documentos, clasificación, valor y tributos.",
          "Principales contingencias en la práctica.",
        ],
      },
    ],
  };

  let cost = {
    amount: "2 pagos de $80.000",
    promotional: "Precio promocional hasta el 22/04: $140.000 (pago único).",
    bankDetails: {
      name: "FC.CS.ECON.Y ADM.",
      cuit: "30641870931",
      accountType: "Cuenta bancaria",
      accountNumber: "31554660081889",
      alias: "FCEyA.UNCA",
      cbu: "0110466420046600818894",
    },
  };

  let contacts = {
    area: "Unidad de Formación Continua | Secretaría de Posgrado",
    email: "formacioncontinua@eco.unca.edu.ar",
    address: "Av. José Figueroa 257.",
    inscriptionLink: "https://forms.gle/ctbFE13c3aGbPeE67",
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
    <div class="introduction-block">
      <p>
        El comercio exterior exige hoy una comprensión integrada de los aspectos operativos y documentales que intervienen en una operación internacional. No alcanza con conocer aisladamente la importación o la exportación; resulta necesario entender cómo se articulan la mercadería, el territorio aduanero, las destinaciones, la clasificación, la valoración, la documentación comercial y el régimen tributario dentro de una misma lógica operativa.
      </p>
      <p>
        Sobre esa base, el programa propone una formación práctica y estructurada que permita identificar los presupuestos básicos de toda operatoria de comercio exterior, comprender sus principales riesgos y reconocer los errores más frecuentes que pueden afectar la regularidad, el costo y la trazabilidad de las operaciones.
      </p>
    </div>
    <p><strong>Inicio:</strong> {startDate}</p>
    <p><strong>Modalidad:</strong> {modality}</p>
    <p><strong>Duración:</strong> {duration}</p>
    <p><strong>Enfoque:</strong> {focus}</p>
    <p><strong>Metodología:</strong> {methodology}</p>
    <p><strong>Días y horario:</strong> {scheduleInfo}</p>

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

    <h2>Perfil del participante</h2>
    <p>{participantProfile}</p>

    <h2>Objetivos</h2>
    <ul class="objective-list">
      {#each objectives as objective}
        <li>{objective}</li>
      {/each}
    </ul>
    
    <h2>Destinatarios</h2>
    <ul class="objective-list">
      {#each recipients as recipient}
        <li>{recipient}</li>
      {/each}
    </ul>

    <h2>Estructura del programa</h2>
    <div style="padding-left: 2rem;">
      {#each schedule.meetings as meeting}
        <p><strong>{meeting.title}</strong></p>
        {#each meeting.dates as date}
          <p>{date}</p>
        {/each}
      {/each}
    </div>



    <h2>Certificación a Entregar</h2>
    <p>{certificationIntro}</p>
    <ul class="objective-list">
      {#each certificationItems as item}
        <li>{item}</li>
      {/each}
    </ul>
    <p>{certificationNote}</p>

    <h2>Documentación a Enviar</h2>
    <ul>
      {#each documentation as document}
        <li>{document}</li>
      {/each}
    </ul>
    <p>
      La documentación deberá ser enviada al correo electrónico:
      <a class="email-link" href="mailto:formacioncontinua@eco.unca.edu.ar">formacioncontinua@eco.unca.edu.ar</a>
      indicando el nombre del curso.
    </p>

    <h2>Valor del Curso</h2>
    <p>{cost.amount}</p>
    <p>{cost.promotional}</p>

    <h2>Datos Bancarios</h2>
    <p><strong>Nombre:</strong> {cost.bankDetails.name}</p>
    <p><strong>CUIT:</strong> {cost.bankDetails.cuit}</p>
    <p><strong>Tipo de cuenta:</strong> {cost.bankDetails.accountType}</p>
    <p><strong>Número de cuenta:</strong> {cost.bankDetails.accountNumber}</p>
    <p><strong>Alias:</strong> {cost.bankDetails.alias}</p>
    <p><strong>CBU:</strong> {cost.bankDetails.cbu}</p>
    <p>
      <strong>Envío de comprobante de pago:</strong>
      <a class="email-link" href="mailto:{contacts.paymentEmail}">{contacts.paymentEmail}</a>
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
    <p>Correo electrónico: <a class="email-link" href="mailto:{contacts.email}">{contacts.email}</a></p>
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

  .introduction-block {
    margin: 0.75rem 0 1rem;
    padding: 0.85rem 1rem;
    border-left: 4px solid #7a1c0b;
    background: rgba(122, 28, 11, 0.04);
  }

  .introduction-block p {
    margin: 0 0 0.75rem;
  }

  .introduction-block p:last-child {
    margin-bottom: 0;
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

  .email-link {
    font-weight: 700;
    color: #7a1c0b;
    text-decoration: underline;
    text-underline-offset: 0.16em;
  }

  .qr-image {
    width: 180px;
    max-width: 100%;
    height: auto;
  }
</style>
