import { defineConfig } from 'vite'
import autoprefixer from 'autoprefixer'
import react from '@vitejs/plugin-react-swc'
import tailwindcss from 'tailwindcss'

// https://vitejs.dev/config/
export default defineConfig({
  css: {
    postcss: {
      plugins: [
        autoprefixer,
        tailwindcss,
      ]
    }
  },
  esbuild: {
    // disable esbuild typescript handling because using SWC
    // jsxInject: `import React from 'react'`,
    tsconfigRaw: require('./tsconfig.json'),
  },
  plugins: [react()],
})
