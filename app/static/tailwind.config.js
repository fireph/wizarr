/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
    content: ["../templates/**/*.html",
        "../templates/*.html",
        "./node_modules/flowbite/**/*.js",
        "../../wizard_steps/**/*.md",],
    theme: {
        extend: {
            colors: {
                primary: '#fe4155',
                primary_hover: '#982633',
                secondary: '#533c5b',
                secondary_hover: '#332538'
                // ...
            }
        },

    },
    plugins: [
        require("flowbite/plugin"),
        require("@tailwindcss/typography"),
    ]
}
