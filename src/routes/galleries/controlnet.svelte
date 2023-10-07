<script lang="ts">
  import { Code, Notes, RevealJsContext, Slide } from '$lib';
  
  import GaleryFull from "$lib/GalleryFull.svelte";
  const imageModules = import.meta.glob("$lib/assets/sd/control-net/*.png"); 
  const imagePath = Object.keys(imageModules).map((key) => key.substring("/src/lib/assets".length))
  export let interval = 5000;
  </script>
  

  <GaleryFull {interval} imagePath={imagePath}/>

<style>
	:global(.img_cont > img) {
		justify-content: center;
  	align-items: center;
		/* text-align: center; */
		max-width: 1024px;
		grid-column: 1/2;
		grid-row: 1/2		
	}  
</style>