import { heroui } from "@heroui/react";

export default heroui({
  themes: {
    light: {
      colors: {
        primary: {
          "50": "#e0e5e8",
          "100": "#b4c1c9",
          "200": "#889ca9",
          "300": "#5d7889",
          "400": "#31536a",
          "500": "#052f4a",
          "600": "#04273d",
          "700": "#031f30",
          "800": "#021623",
          "900": "#020e16",
          foreground: "#fff",
          DEFAULT: "#052f4a",
        },
      },
    },
    dark: {
      colors: {
        primary: {
          "50": "#020e16",
          "100": "#021623",
          "200": "#031f30",
          "300": "#04273d",
          "400": "#052f4a",
          "500": "#31536a",
          "600": "#5d7889",
          "700": "#889ca9",
          "800": "#b4c1c9",
          "900": "#e0e5e8",
          foreground: "#fff",
          DEFAULT: "#052f4a",
        },
      },
    },
  },
});
