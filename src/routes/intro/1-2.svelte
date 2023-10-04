<script lang="ts">
  import { Code, Notes, RevealJsContext, Slide } from '$lib';
  
  import Galery from "$lib/Gallery.svelte";
  const imageModules = import.meta.glob("$lib/assets/1-2/*.jpg"); 
  const imagePath = Object.keys(imageModules).map((key) => key.substring("/src/lib/assets".length))


  export let interval = 1500;
</script>
  

<Galery {interval} imagePath={imagePath} />

