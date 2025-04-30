/**
 * Greenova Tailwind Configuration
 *
 * This configuration is designed to complement PicoCSS, not replace it.
 * We map Tailwind's color system to use Greenova design tokens and
 * ensure the two systems work together without conflicts.
 */

module.exports = {
  // Only process files that specifically use Tailwind
  content: [
    './greenova/templates/**/*.html',
    './greenova/static/js/**/*.js',
    './greenova/*/templates/**/*.html',
  ],

  theme: {
    extend: {},
  },

  // Define custom plugins for Greenova-specific needs
  plugins: [
    require('daisyui'),
    // Plugin to generate WCAG-compliant focus styles
    function ({ addUtilities }) {
      const accessibilityUtilities = {
        '.focus-accessible': {
          outline: '3px solid var(--greenova-green-primary)',
          'outline-offset': '2px',
        },
      };
      addUtilities(accessibilityUtilities);
    },

    // Plugin for responsive data visualization
    function ({ addComponents }) {
      const chartComponents = {
        '.responsive-chart': {
          width: '100%',
          height: 'auto',
          'min-height': '300px',
        },
      };
      addComponents(chartComponents, { respectImportant: true });
    },
    
  ],
  daisyui: {
    themes: ['light', 'dark'], // Use DaisyUI's light and dark themes
  },
};
