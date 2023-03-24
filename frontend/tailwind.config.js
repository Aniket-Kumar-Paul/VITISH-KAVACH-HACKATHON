/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "dark": "#0c0c16",
        "grayish": "#a3a2b8",
        "blue-dark": "#0473e9",
        "blue-light": "#018dee",
      },
    },
  },
  plugins: [],
};
