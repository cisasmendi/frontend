<script>
    export let title = "";
    export let imageUrl = "";
  </script>
  
  <div class="w-full lg:w-3/4 p-4">
    <img
      src={imageUrl}
      alt="Prototipo de imagen"
      class="w-full lg:w-1/2 rounded-lg mb-4 float-right ml-4"
    />
    <div>
      <h2 class="text-2xl font-semibold text-[#6d0205]">{title}</h2>
      <h2 class="text-2xl font-semibold text-[#6d0205]">
        Dr. Ricardo Pahlen Acuña
      </h2>
      <p class="mb-4">
        Tiene la misión de coordinar, ejecutar y transferir conocimientos teóricos
        o empíricos vinculados con la realidad disciplinar contable a nivel
        internacional, nacional, regional y local, realizando aportes a la teoría
        contable y fortaleciendo los sistemas de información contable de las
        organizaciones de carácter público o privado.
      </p>
  
      <h3 class="text-xl font-semibold text-[#6d0205]">Autoridades:</h3>
  
      <p class="mb-4">
        <strong>Directora:</strong><br />
        Mgter. CPN María Beatriz Maza
      </p>
  
      <h3 class="text-xl font-semibold text-[#6d0205]">Contacto:</h3>
  
      <p class="mb-4">
        <strong>Email:</strong>
        <a href="mailto:" class="text-blue-500 hover:underline"
          >[correo no especificado]</a
        ><br />
        <strong
          >Edificio de Profesores, Facultad de Ciencias Económicas y de
          Administración. UNCA</strong
        ><br />
        Av. José Figueroa 275. San Fernando del Valle de Catamarca (4700). Catamarca,
        Argentina.
      </p>
    </div>
  </div>