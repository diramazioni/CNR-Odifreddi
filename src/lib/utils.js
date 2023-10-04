import { onDestroy } from 'svelte';


/**
 * @param {(...args: any[]) => void} callback
 * @param {number} milliseconds
 */
export function onInterval(callback, milliseconds) {
	const timeout = setInterval(callback, milliseconds);

	onDestroy(() => {
		clearInterval(timeout)
	});
	return timeout;
}
