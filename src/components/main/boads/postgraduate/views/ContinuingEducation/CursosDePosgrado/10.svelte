<script>
     import Accordion from "$utilsMain/Accordion.svelte";
     let imageUrl = "/assets/posgrado/Cursos de Posgrado/10.png";
     let qrCode = "/assets/posgrado/Cursos de Posgrado/10_qr.png";
     export const courseTitle =
          "Ciclo de Actualización de Tecnología y Seguridad de la Información para Profesionales en Ciencias Económicas";
     let startDate = "11 de Noviembre 2024";
     let modality = "Virtual";
     let teacher = "Dr. Diego Sebastián Escobar";
     let generalObjective =
          "Proveer a los docentes y profesionales en Ciencias Económicas de las competencias necesarias para la docencia universitaria y la integración de nuevas tecnologías de la información y la comunicación (NTIC), seguridad informática y gestión de grandes volúmenes de datos en su práctica profesional, cumpliendo con las normativas vigentes.";
     let specificObjectives = [
          "Desarrollar competencias tecnológicas.",
          "Proveer conocimientos sobre las normativas de gestión de tecnología y seguridad de la información.",
          "Enseñar el uso del formato XBRL para la gestión de datos contables.",
          "Explorar la implementación de la tecnología blockchain en la contabilidad.",
          "Analizar el impacto de la legislación sobre protección de datos personales.",
          "Desarrollar habilidades en la gestión y análisis de grandes volúmenes de datos.",
          "Fomentar la aplicación práctica de los conocimientos adquiridos.",
     ];
     let schedule = [
          { class: 1, date: "11 de noviembre", time: "18:00 a 20:00 hs" },
          { class: 2, date: "18 de noviembre", time: "18:00 a 20:00 hs" },
          { class: 3, date: "25 de noviembre", time: "18:00 a 20:00 hs" },
          { class: 4, date: "2 de diciembre", time: "18:00 a 20:00 hs" },
          { class: 5, date: "9 de diciembre", time: "18:00 a 20:00 hs" },
          { class: 6, date: "16 de diciembre", time: "18:00 a 20:00 hs" },
     ];
     let cost = "$40,000";
     let paymentDetails = {
          alias: "FCEyA.UNCA",
          accountNumber: "31554660081889",
          cbu: "0110466420046600818894",
          name: "FC.CS.ECON.Y ADM.",
          cuit: "30641870931",
          email: "lahumada@eco.unca.edu.ar",
     };
     let contactInfo = {
          unit: "Unidad de Formación Continua. Secretaría de Posgrado",
          email: "formacioncontinua@eco.unca.edu.ar",
          address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca",
     };
     export let open = false; // Controla si el acordeón está abierto o cerrado
</script>

<Accordion
     title={"Ciclo de Actualización de Tecnología y Seguridad de la Información para Profesionales en Ciencias Económicas"}
     disabled={true}
     isOpen={open}
>
     <div slot="content">
          <div class="animate-slide-in-up">
               <img
                    src={imageUrl}
                    alt="Prototipo de imagen"
                    class="transition-all duration-300 hover:scale-105 w-full rounded-lg mb-4 ml-4 max-w-[800px]"
               />
          </div>

          <h1>{courseTitle}</h1>
          <p>
               <strong>Inicio de Clases:</strong>
               {startDate} | <strong>Modalidad:</strong>
               {modality}
          </p>

          <h2>Docente a cargo</h2>
          <p>{teacher}</p>

          <h2>Objetivo General</h2>
          <p>{generalObjective}</p>

          <h2>Objetivos Específicos</h2>
          <ul>
               {#each specificObjectives as objective}
                    <li>{objective}</li>
               {/each}
          </ul>

          <h2>Programación de Actividades</h2>
          <table>
               <thead>
                    <tr>
                         <th>Clase</th>
                         <th>Fecha</th>
                         <th>Hora</th>
                    </tr>
                    <tr>
                         <td rowspan="2" class="text-center">
                              <strong>Unidad</strong><br />
                              <strong>(Clases sincrónicas)</strong>
                         </td>
                         <td colspan="6" class="text-center">
                              <strong>Semanas</strong>
                         </td>
                    </tr>
                    <tr>
                         <td class="text-center"><strong>1</strong></td>
                         <td class="text-center"><strong>2</strong></td>
                         <td class="text-center"><strong>3</strong></td>
                         <td class="text-center"><strong>4</strong></td>
                         <td class="text-center"><strong>5</strong></td>
                         <td class="text-center"><strong>6</strong></td>
                    </tr>

                    <tr>
                         <td class="text-center"><strong>1</strong></td>
                         <td class="text-center">X</td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                    </tr>
                    <tr>
                         <td class="text-center"><strong>2</strong></td>
                         <td class="text-center"></td>
                         <td class="text-center">X</td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                    </tr>
                    <tr>
                         <td class="text-center"><strong>3</strong></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center">X</td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                    </tr>
                    <tr>
                         <td class="text-center"><strong>4</strong></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center">X</td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                    </tr>
                    <tr>
                         <td class="text-center"><strong>5</strong></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center">X</td>
                         <td class="text-center"></td>
                    </tr>
                    <tr>
                         <td class="text-center"><strong>6</strong></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center"></td>
                         <td class="text-center">X</td>
                    </tr>
               </thead>
          </table>

          <h3>
               <a
                    href="https://acortar.link/z3CQeE"
                    target="_blank"
                    style="color:red">► FORMULARIO DE INSCRIPCIÓN</a
               >
          </h3>
          <div class="animate-slide-in-up">
               <img src={qrCode} alt="Prototipo de imagen" />
          </div>

          <h2>Costos</h2>
          <p><strong>Costo:</strong> {cost}</p>
          <p><strong>Alias:</strong> {paymentDetails.alias}</p>
          <p>
               <strong>Número de cuenta:</strong>
               {paymentDetails.accountNumber}
          </p>
          <p><strong>CBU:</strong> {paymentDetails.cbu}</p>
          <p><strong>Nombre:</strong> {paymentDetails.name}</p>
          <p><strong>CUIT:</strong> {paymentDetails.cuit}</p>
          <p>
               Enviar comprobante de pago a: <strong
                    >{paymentDetails.email}</strong
               >
          </p>

          <h2>Contactos</h2>
          <p>{contactInfo.unit}</p>
          <p>{contactInfo.email}</p>
          <p>{contactInfo.address}</p>

          <h2>Inscripciones</h2>
          <p>
               Documentación a enviar: DNI, Título, Constancia de título en
               trámite.
          </p>
          <p>Enviar documentación a: <strong>{paymentDetails.email}</strong></p>
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

     h2 {
          font-family: "Merriweather", serif;
          font-weight: 600;

          font-size: 1.25rem;
          padding-top: 1rem;
          color: #7a1c0b;
     }

     ul {
          list-style-type: disc;
          margin-left: 20px;
     }
</style>
