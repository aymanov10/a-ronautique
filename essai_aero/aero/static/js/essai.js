
$('#map-example').vectorMap(
		{
			map: 'world_en',
			backgroundColor: 'transparent',
			borderColor: '#fff',
			borderWidth: 2,
			color: '#e4e4e4',
			enableZoom: true,
			hoverColor: '#35cd3a',
			hoverOpacity: null,
			normalizeFunction: 'linear',
			scaleColors: ['#b6d6ff', '#005ace'],
			selectedColor: '#35cd3a',
			selectedRegions: ['ID', 'RU', 'US', 'AU'],
			showTooltip: true,
			onRegionClick: function(element, code, region)
			{
				return false;
			},
			onResize: function (element, width, height) {
				console.log('Map Size: ' +  width + 'x' +  height);
			},
            onRegionOver: function(element, code, region)
			{
				return true;
			},
		});