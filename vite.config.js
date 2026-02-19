import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from '@tailwindcss/vite';
import dsv from '@rollup/plugin-dsv';


import path from "path";
export default defineConfig({
  resolve: {
    alias: {

      '$EnConstruccion': path.join(__dirname, 'src/components/main/utils/ComponeteEnContruccion.svelte'),
      '$BoardLayout': path.join(__dirname, 'src/components/layout/BoardLayout.svelte'),
      '$utilsMain': path.join(__dirname, 'src/components/main/utils'),   
      '$utils': path.join(__dirname, 'src/components/utils'),
      '@globalStore': path.join(__dirname, 'src/stores/globalStore.js'),
    }
  },
    plugins: [
    svelte(),
    tailwindcss(),
    dsv() 
  ],
  optimizeDeps: {
    
  },
  build: {
    //outDir: path.join(__dirname, "../public"),
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('svelte-pdf')) {
            return 'svelte-pdf';
          }
        }
      }
    }
  }
});
