/** @type {import('tailwindcss').Config} */
export default {
	content: ['./index.html', './src/**/*.{html,js,jsx,ts,tsx}'],
	corePlugins: {
		preflight: true
	},
	mode: 'jit',
	plugins: [],
	safelist: [],
	theme: {
		colors: {
			'cable-green': '#19323d',
			'citrine-white': '#faf3d3',
			'desert-sand': '#E8DAB2',
			'mint-cream': '#C0D8C0',
			'orange-roughly': '#ce5317',
			'steel-blue': '#4F6D7A',
			casablanca: '#f6a945',
			java: '#22afc3',
			terracotta: '#DD6E42',
			white: '#FFFFFF'
		},
		extend: {
			backgroundColor: {
				'default-bg': '#FAF3d3'
			},
			// backgroundImage: {
			// 	'tan-gradient': 'linear-gradient(to bottom, #E8DAB2, #faf3d3)',
			//   }
		}
	}
};
