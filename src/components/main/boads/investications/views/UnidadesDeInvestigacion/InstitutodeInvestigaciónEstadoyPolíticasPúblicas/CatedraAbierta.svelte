<script>
  export let title = "";
  export let imageUrl = "";
  import BoardLayout from "$BoardLayout";
</script>

<BoardLayout>
  <div>
    <img
      src={imageUrl}
      alt="Prototipo de imagen"
      class="w-10 h-10 lg:w-10 lg:h-10 rounded-lg mb-4 float-left mr-4"
    />
    <h2 class="text-2xl font-semibold text-[#6d0205]">{title}</h2>

    <h3 class="text-xl mt-6 font-semibold text-[#6d0205]">Cátedra Abierta</h3>

    <p class="mb-4">
      La Cátedra Abierta es un espacio académico creado para promover la
      formación, la reflexión crítica y el debate en torno a problemáticas
      actuales y temáticas de relevancia en el ámbito educativo y social. Este
      espacio facilita la discusión y la investigación interdisciplinaria,
      brindando un entorno propicio para la generación de conocimientos y el
      intercambio de experiencias entre estudiantes, docentes, investigadores y
      la comunidad en general.
    </p>
    <p class="mb-4">
      A través de la Cátedra Abierta, se busca no solo la transmisión de
      conocimientos, sino también la apertura de diálogos que contribuyan a la
      comprensión y solución de desafíos contemporáneos. El objetivo es
      democratizar el acceso a saberes especializados, ofreciendo oportunidades
      para la divulgación y participación activa de todas las personas
      interesadas, sin importar su área de formación.
    </p>
  </div>
</BoardLayout>
