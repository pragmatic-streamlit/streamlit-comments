import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base: './',
  optimizeDeps: {
    esbuildOptions: {
      // Node.js global to browser globalThis
      define: {
        global: 'globalThis',
        process: `${JSON.stringify({ env: {} })}`,
      },
    },
  },
  server: {
    port: 3001
  },
  plugins: [react()],
})
