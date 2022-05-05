module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
    screens: {
      xxs: {'max': '362px'},
      xs: {'max': '386px'},
      md: {'max': '858px'},
      lg: '858px',
      xl: '1440px',
      smd: '640px',
      mdd: '768px',
      lgd: '1024px',
      xld: '1280px',
      xl2d: '1536px',
    },
    fontFamily: {
      'poppins': ['Poppins', 'sans-serif'],
      'lato': ['Lato', 'sans-serif'],
    },
    extend: {
      lineHeight: {
        '20': '5rem',
      },
      colors: {
        brightRed: 'hsl(12, 88%, 59%)',
        brightRedLight: 'hsl(12, 88%, 69%)',
        brightRedSupLight: 'hsl(12, 88%, 95%)',
        darkBlue: 'hsl(228, 39%, 23%)',
        darkGrayishBlue: 'hsl(227, 12%, 61%)',
        veryDarkBlue: 'hsl(223, 12%, 13%)',
        veryPaleRed: 'hsl(13, 100%, 96%)',
        veryLightGray: 'hsl(0, 0%, 98%)',
      }
    },
  },
  variants: [],
  plugins: [],
}
