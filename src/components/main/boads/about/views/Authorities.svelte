<script>
     import BoardLayout from "$BoardLayout"
    import ProfileCard from "../util/ProfileCard.svelte";

    export let title = "";

    // Datos de los perfiles
    let profiles = [
        { name: "CPN Gustavo Alfredo Lazarte", position: "Decano" ,imageUrl : "https://picsum.photos/150?random=1"},
        { name: "Esp. Marcelo Beltran Delgado", position: "Vicedecano" , imageUrl: "https://picsum.photos/150?random=2"},
        { name: "CPN Ana Teresa Calvimonte", position: "Secretaria Académica" , imageUrl: "https://picsum.photos/150?random=3"},
        { name: "CPN Evelin Sotomayor", position: "Secretaria de Relaciones Institucionales" , imageUrl: "https://picsum.photos/150?random=4"},
        { name: "Lic. Raúl Mura", position: "Secretario de Posgrado" , imageUrl: "https://picsum.photos/150?random=5"},
        { name: "Mg. CPN Andrea Morales", position: "Secretaría de Investigación, Innovación y Transferencia" , imageUrl: "https://picsum.photos/150?random=6"},
        { name: "Sr. Víctor Hugo Robledo", position: "Dirección Operativa" , imageUrl: "https://picsum.photos/150?random=7"},     
    ];
</script>



<BoardLayout {title} >
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {#each profiles as profile}
            <ProfileCard name={profile.name} position={profile.position} imageUrl={profile.imageUrl} />
        {/each}
    </div>
</BoardLayout>
