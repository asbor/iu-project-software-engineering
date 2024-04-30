export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', 'shadcn-nuxt', 'nuxt-icon', 'nuxt-highcharts'],
  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  },
  runtimeConfig: {
    API_URL: process.env.API_BASE_URL || "http://localhost:8000/",
    public:{
      API_URL: process.env.API_BASE_URL || "http://localhost:8000/",
    }
  },
})