export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', 'shadcn-nuxt', 'nuxt-icon', 'nuxt-highcharts'],
  shadcn: {
    prefix: '',
    componentDir: './components/ui',
  },
  runtimeConfig: {
    API_URL: process.env.API_BASE_URL || 'http://localhost:8000/',
    public: {
      API_URL: process.env.API_BASE_URL || 'http://localhost:8000/',
    },
  },
  icon: {
    size: '24px',
    class: 'icon',
    mode: 'svg',
  },
  css: ['~/assets/css/tailwind.css'],
  generate: {
    fallback: true,
  },
});
