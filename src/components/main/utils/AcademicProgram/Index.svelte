<script>
  import BoardLayout from "$BoardLayout";
  import Registration from "./components/Registration.svelte";
  import ManagementStructure from "./components/ManagementStructure.svelte";
  import Staff from "./components/Staff.svelte";
  import Requirements from "./components/Requirements.svelte";
  import Downloads from "./components/Downloads.svelte";
  import GraduateProfile from "./components/GraduateProfile.svelte";
  import Scope from "./components/Scope.svelte";
  import Objetives from "./components/Objetives.svelte";
  import Plan from "./components/StudyPlan.svelte";
  import Cost from "./components/Cost.svelte";

  export let programInfo = {
    title: "",
    modality: "",
    duration: "",
    finalTitle: "",
    resolution: "",
    observations: "",
    objectives: {
      general: [],
      specific: [],
    },
    scope: "",
    graduateProfile: "",
    requirements: [],
    studyPlan: [],
    contact: {
      email: "",
      phone: "",
      wp: "",
    },
    downloads: [],
    registrations: [],
    cost: "",
    managementstructure: "",
  };

</script>

<BoardLayout title={programInfo.title}>
  <div
    class="informacion-carrera"
    style="display: flex; flex-direction: column;"
  >
    <div>
      <h2>
        {#if programInfo?.modality}
          Modalidad: {programInfo.modality}<br />
        {/if}
        {#if programInfo?.duration}
          Duración: {programInfo.duration}<br />
        {/if}
        {#if programInfo?.finalTitle}
          Título Final: {programInfo.finalTitle}<br />
        {/if}
        {#if programInfo?.resolution}
          Resolución Ministerial: {programInfo.resolution}<br />
        {/if}
        {#if programInfo?.Link && programInfo?.labelLink}
          <a class="text-xl font-semibold pt-4 text-blue-600" href={programInfo.Link} target="_blank">{programInfo.labelLink} "Click aquí"</a>
        {/if}
      </h2>
    </div>

    {#if programInfo?.observations}
      <br />
      {@html programInfo.observations}
      <br />
    {/if}
    <br />
    {#if programInfo?.graduateProfile}
      <GraduateProfile graduateProfile={programInfo.graduateProfile} />
    {/if}
    {#if programInfo?.objectives?.general.length > 0 || programInfo?.objectives?.specific.length > 0}
      <Objetives objectives={programInfo.objectives} />
    {/if}
    {#if programInfo?.scope}
      <Scope scope={programInfo.scope} />
    {/if}
    {#if programInfo?.requirements?.length > 0}
      <Requirements requirements={programInfo.requirements} />
    {/if}
    {#if programInfo?.registrations?.length > 0 || programInfo?.contact?.email || programInfo?.contact?.phone }
      <Registration {programInfo} />
    {/if}

    {#if programInfo?.downloads?.length > 0}
      <Downloads programInfo={programInfo} />
    {/if}
    {#if programInfo?.managementstructure}
      <ManagementStructure
        managementStructure={programInfo.managementstructure}
      />
    {/if}
    {#if programInfo?.staff}
      <Staff staff={programInfo.staff} />
    {/if}
    {#if programInfo?.cost}
      <Cost cost={programInfo.cost} />
    {/if}
    <Plan>
      <slot name="plan"></slot>
      <br />
    </Plan>

  </div>
</BoardLayout>
