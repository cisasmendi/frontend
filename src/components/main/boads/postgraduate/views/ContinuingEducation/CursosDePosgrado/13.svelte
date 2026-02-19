<script>
    import Accordion from "$utilsMain/Accordion.svelte";

let qrCode = "/assets/posgrado/Cursos de Posgrado/13_qr.png";
let imageUrl = "/assets/posgrado/Cursos de Posgrado/13.jpg";
export const courseTitle = "Taller Trabajo Final de Posgrado";
let startDate = "1 de abril de 2025";
let modality = "Híbrida";
let professors = ["Esp. Raúl Mura", "Mg. Leticia Gallo", "Mg. Laura Arrascaeta"];

let objectivesGeneral = "Brindar un espacio de acompañamiento y asesoramiento metodológico para que los estudiantes avancen en la elaboración de su Trabajo Final de Carrera de Posgrado, sin sustituir la orientación de sus directores y comités evaluadores.";
let objectivesSpecific = [
"Proporcionar herramientas para organizar y estructurar el Trabajo Final de manera efectiva.",
"Guiar en la definición y delimitación del problema de investigación.",
"Orientar en la selección de fuentes y el análisis crítico de la bibliografía.",
"Favorecer el desarrollo de la argumentación y la redacción académica.",
"Fomentar el cumplimiento de plazos y la organización del trabajo."
];

let schedule = {
totalClasses: 4,
classDuration: "2 hs",
dates: ["1 y 29 de abril", "27 de mayo", "25 de junio"],
totalHours: 8,
platform: "Modalidad híbrida"
};

let analyticalContents = [
"Encuentro 1: Introducción y objetivos - Revisión del estado de avance, redacción de objetivos, identificación del problema.",
"Encuentro 2: Marco teórico - Construcción del marco teórico, relación con los objetivos, justificación.",
"Encuentro 3: Marco metodológico - Elección del tipo de estudio, selección de técnicas, redacción del apartado metodológico.",
"Encuentro 4: Cierre y planificación final - Planificación del trabajo final, cronograma de entrega, estrategias de defensa oral."
];

let methodology = [
"Sesiones interactivas de taller.",
"Trabajo sobre proyectos individuales.",
"Tutoría personalizada.",
"Espacios de consulta y retroalimentación."
];

let evaluationCriteria = ["No se realizará una evaluación formal."];
let targetAudience = ["Estudiantes que elaboran su Trabajo Final de Especialización o Maestría."];
let admissionRequirements = ["DNI, Pasaporte o Cédula Extranjera."];
let expectedOutcomes = "Avanzar en la elaboración del Trabajo Final con acompañamiento metodológico.";

let cost = {
paymentAmount: "Cuatro (4) pagos de $30.000",
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
inscriptionLink: "https://forms.gle/iY4C2GVhaxwBs39R9"
};

let inscriptionDeadline = "1 de abril de 2025";
export let open = false; // Controla si el acordeón está abierto o cerrado
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <div class="animate-slide-in-up">
        <img
             src={imageUrl}
             alt="Prototipo de imagen"
             class="transition-all duration-300 hover:scale-105 w-full rounded-lg mb-4 ml-4 max-w-[800px]"
        />
   </div>
    <p>INICIO DE CLASES: {startDate} | {modality}</p>
    
    <h2>Docentes a cargo</h2>
    <ul>{#each professors as professor}<li>{professor}</li>{/each}</ul>
    
    <h2>Objetivos</h2>
    <h3>Objetivo General</h3>
    <p>{objectivesGeneral}</p>
    <h3>Objetivos Específicos</h3>
    <ul>{#each objectivesSpecific as objective}<li>{objective}</li>{/each}</ul>

    <h2>Programación de Actividades</h2>
    <p>Fecha de inicio: {startDate}. Fechas: {schedule.dates.join(', ')}. Carga horaria total: {schedule.totalHours} hs.</p>
    
    <h2>Contenidos Analíticos</h2>
    <ul>{#each analyticalContents as content}<li>{content}</li>{/each}</ul>

    <h2>Metodología</h2>
    <ul>{#each methodology as method}<li>{method}</li>{/each}</ul>
    
    <h2>Evaluación</h2>
    <ul>{#each evaluationCriteria as criterion}<li>{criterion}</li>{/each}</ul>

    <h2>Destinatarios</h2>
    <ul>{#each targetAudience as audience}<li>{audience}</li>{/each}</ul>
    
    <h2>Requisitos de Admisión</h2>
    <ul>{#each admissionRequirements as requirement}<li>{requirement}</li>{/each}</ul>

    <h2>Resultados Esperados</h2>
    <p>{expectedOutcomes}</p>
    
    <h2>Costos</h2>
    <p>{cost.paymentAmount}.</p>
    <p>Formas de Pago: {cost.paymentMethod}</p>
    <p><strong>Datos Bancarios:</strong></p>
    <p>Alias: {cost.bankDetails.alias}</p>
    <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
    <p>CBU: {cost.bankDetails.cbu}</p>
    <p>Nombre: {cost.bankDetails.name}</p>
    <p>CUIT: {cost.bankDetails.cuit}</p>
    <div >
      <p>
        Los comprobantes de pago deberán ser enviados al correo electrónico: 
        <a href="mailto:mluduena@eco.unca.edu.ar" style="color: #007bff; text-decoration: none;">mluduena@eco.unca.edu.ar</a> 
        con el asunto <strong>"PAGO"</strong>, detallando:
      </p>
      <ul style="padding-left: 20px;">
        <li><strong>Apellido y Nombres</strong> del Alumno</li>
        <li><strong>DNI</strong></li>
        <li><strong>Nombre del Curso</strong> a inscribirse</li>
      </ul>
    </div>
    
    
    <h2>Inscripciones</h2>
    <p>Reservá tu cupo hasta el {inscriptionDeadline}.</p>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue">► FORMULARIO DE INSCRIPCIÓN</a>
    
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
