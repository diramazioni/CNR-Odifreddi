import adapter from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/kit/vite';

const dev = process.env.NODE_ENV === 'development';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter(),
		files: {
			assets: dev ? './src/lib/assets' : './src/lib/assets' 
		},		
	},

	vitePlugin: {
		experimental: {
			inspector: {
				holdMode: true,
				showToggleButton: 'always', //always
				toggleButtonPos: 'bottom-right'
			}
		}
	}
};

export default config;
