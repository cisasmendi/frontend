<script>
    import Accordion from "$utilsMain/Accordion.svelte";

    let qrCode = "/assets/posgrado/Cursos de Posgrado/14_qr.png";
    let imageUrl = "/assets/posgrado/Cursos de Posgrado/14.jpg";
    export const courseTitle = "Data Science y Machine Learning para Profesionales de Ciencias Económicas";
    let startDate = "6 de mayo de 2025";
    let modality = "A distancia";
    let professors = ["Dr. Marcos Ariel Argañaraz"];

    let objectivesGeneral = "Formar profesionales capacitados en el uso de Ciencias de Datos y Machine Learning aplicados a la economía, finanzas y negocios, con el fin de optimizar la toma de decisiones mediante el análisis de grandes volúmenes de datos y el uso de modelos predictivos y de clasificación.";
    let objectivesSpecific = [
        "Capacitar en el uso de modelos de predicción de series temporales como ARIMA, Random Forest y LSTM.",
        "Fomentar la comprensión de modelos de clasificación como regresión logística, árboles de decisión, Gradient Boosting y redes neuronales.",
        "Enseñar técnicas de optimización de precios con Machine Learning (Bayesian Optimization y Reinforcement Learning).",
        "Brindar una base sólida en segmentación de clientes usando algoritmos de clustering como K-Means y DBSCAN.",
        "Aplicar conocimientos en proyectos reales del ámbito económico, financiero y empresarial.",
        "Propiciar oportunidades laborales colaborando con empresas del sector."
    ];

    let schedule = {
        totalClasses: 8,
        classDuration: "2 hs",
        dates: ["6, 13, 20, 27 de mayo", "3, 10, 17, 23 de junio"],
        totalHours: 16,
        platform: "A distancia"
    };

    let methodology = [
        "Enfoque práctico y aplicado a problemas reales.",
        "Uso de datos económicos reales.",
        "Proyectos individuales y grupales.",
        "Actividades interactivas, estudios de caso y debates.",
        "Trabajo Final integrador aplicando conocimientos adquiridos."
    ];

    let evaluationCriteria = [
        "Participación activa en las actividades y proyectos.",
        "75% de asistencia a clases.",
        "Aprobación del Trabajo Final integrador."
    ];

    let targetAudience = [
        "Docentes de las carreras de Ciencias Económicas.",
        "Público en general interesado."
    ];

    let admissionRequirements = [
        "DNI, Pasaporte o Cédula Extranjera.",
        "Título universitario o constancia de título en trámite."
    ];

    let expectedOutcomes = "Desarrollar habilidades en ciencia de datos y machine learning aplicadas a la economía, finanzas y negocios.";

    let cost = {
        paymentAmount: "Dos (2) pagos de $80.000",
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
        inscriptionLink: "https://forms.gle/wyHkjHAEUPfCgsGEA"
    };

export let open = false; // Controla si el acordeón está abierto o cerrado
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>

    <p>INICIO DE CLASES: {startDate} | {modality}</p>
    
    <h2>Docente</h2>
    <ul>{#each professors as professor}<li>{professor}</li>{/each}</ul>
    
    <h2>Objetivos</h2>
    <h3>General</h3>
    <p>{objectivesGeneral}</p>
    <h3>Específicos</h3>
    <ul>{#each objectivesSpecific as objective}<li>- {objective}</li>{/each}</ul>

    <h2>Programación</h2>
    <p>Fechas: {schedule.dates.join(', ')}. Horario: 19 a 21 hs. Carga horaria total: {schedule.totalHours} hs.</p>
    
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
    <p>{cost.paymentAmount}</p>
    <p>Forma de Pago: {cost.paymentMethod}</p>
    <p><strong>Datos Bancarios:</strong></p>
    <p>Alias: {cost.bankDetails.alias}</p>
    <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
    <p>CBU: {cost.bankDetails.cbu}</p>
    <p>Nombre: {cost.bankDetails.name}</p>
    <p>CUIT: {cost.bankDetails.cuit}</p>
    <div>
      <p>
        Los comprobantes de pago deberán ser enviados a 
        <a href="mailto:mluduena@eco.unca.edu.ar" style="color: #007bff; text-decoration: none;">mluduena@eco.unca.edu.ar</a> 
        con el asunto <strong>"PAGO"</strong>, detallando:
      </p>
      <ul>
        <li><strong>Apellido y Nombres</strong> del Alumno</li>
        <li><strong>DNI</strong></li>
        <li><strong>Nombre del Curso</strong> a inscribirse</li>
      </ul>
    </div>
    
    <h2>Inscripciones</h2>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue">► FORMULARIO DE INSCRIPCIÓN</a>
    
    <div class="animate-slide-in-up">
        <img src={qrCode} alt="Código QR de inscripción" />
    </div>

    <br>
    DOCUMENTACIÓN A ENVIAR
DNI, Pasaporte o Cédula Extranjera
Título universitario o constancia de título en trámite
Deberá ser enviado al correo electrónico 
<a href="formacionconti-nua@eco.unca.edu.ar" style="color: #007bff; text-decoration: none;">formacionconti-nua@eco.unca.edu.ar</a> 
indicando el nombre del curso.


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
