<script>
  export let title = "";
  import BoardLayout from "$BoardLayout";

  import Data from "./view/Data.svelte";
  import cvyt from "./view/data/cvyt.json";
  import pidi from "./view/data/pidi.json";
  import pit from "./view/data/pit.json";  
  import pforcyt from "./view/data/pforcyt.json";

  import info from "./view2024-2025/data/info.json";
  import Data2024 from "./view2024-2025/Data.svelte";
</script>

<BoardLayout {title}>
  <br />
  <h1 class="text-2xl font-bold text-center mb-4 text-[#6d0205]">Proyectos 2024-2025</h1>
  <Data2024 data={info} />
<!--
  <Data data={pit} />
  <br />
  <Data data={pidi} />
  <br />
  <Data data={pforcyt} />
  <br />
  <Data data={cvyt} />
  <br />-->
</BoardLayout>
