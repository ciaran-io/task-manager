/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./taskmanager/templates/**/*.html",
    "./taskmanager/static/**/*.js",
  ],
  theme: {
    container: {
      padding: '1rem',
      center: true,
    },
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["dark", 'night'],
  },
}
