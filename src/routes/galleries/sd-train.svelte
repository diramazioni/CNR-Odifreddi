<script lang="ts">
  import { Code, Notes, RevealJsContext, Slide } from '$lib';
  
  import GaleryFull from "$lib/GalleryFull.svelte";
  const imageModules = import.meta.glob("$lib/assets/11/*.jpg"); 
  const imagePath = Object.keys(imageModules).map((key) => key.substring("/src/lib/assets".length))
  export let interval = 5000;
  </script>
  
<div style="margin-top: -50px;">
  <GaleryFull {interval} imagePath={imagePath}/>
</div>
