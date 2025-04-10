module.exports = {
  content: [
    './greenova/templates/**/*.html',
    './greenova/static/js/**/*.js',
    './greenova/*/templates/**/*.html',
  ],

  important: false,

  corePlugins: {
    preflight: false,
  },

  plugins: [require('daisyui')],
};
