import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react({swcOptions: {
    jsc: {
      parser: {
        // enable typescript parsing 
        syntax: 'typescript',
        // enable tsx
        tsx: true,
      },
      transform: {
        react: {
          // react jsx transfromations
          runtime: 'automatic',
        }
      }
    }
  }})],
  esbuild: {
    // disable esbuild typescript handling because using SWC
    // jsxInject: `import React from 'react'`,
    tsconfigRaw: require('./tsconfig.json'),
  }
})
