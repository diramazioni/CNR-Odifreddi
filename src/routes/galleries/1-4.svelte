<script lang="ts">
  import { Code, Notes, RevealJsContext, Slide } from '$lib';
  
  import Galery from "$lib/Gallery.svelte";
  const imageModules = import.meta.glob("$lib/assets/1-4/*.jpg"); 
  const imagePath = Object.keys(imageModules).map((key) => key.substring("/src/lib/assets".length))
  export let interval = 1500;
  </script>
  
  <p style="font-size: x-large; margin:0;">Poliedri</p>
  <Galery {interval} imagePath={imagePath} />

