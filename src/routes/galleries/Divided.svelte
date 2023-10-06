<script lang="ts">
  import { Code, Notes, RevealJsContext, Slide } from '$lib';
  
  import Galery from "$lib/Gallery.svelte";
  const imageModules = import.meta.glob("$lib/assets/1-2/*.jpg"); 
  const imagePath = Object.keys(imageModules).map((key) => imageModules[key].name);	
  const interval = 1500;
  </script>
  <Slide>
    <Slide>
      <Galery {interval} imagePath={imagePath} />
    </Slide>
  </Slide>