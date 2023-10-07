<script lang="ts">
	import { onMount } from 'svelte';
	import {  RevealJsContext } from '$lib';
	import type Reveal from 'reveal.js';

	// The highlight plugin requires a stylesheet

	
	let plugins: Reveal.PluginFunction[];

	onMount(async () => {
		plugins = [
			await import('reveal.js/plugin/highlight/highlight').then(res => res.default),
			await import('reveal.js/plugin/markdown/markdown').then(res => res.default),
			await import('reveal.js/plugin/notes/notes').then(res => res.default),
		]
	})
</script>
<div style:width="100%" style:height="100vh">
	{#if plugins}
	<RevealJsContext
		options={{
			disableLayout: true,
			controls: true,
			progress: true,
			center: false,
			hash: true,
			plugins
		}}
	>
        <slot/>
    </RevealJsContext>
    {/if}
</div>

