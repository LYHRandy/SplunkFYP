require.config({
    paths: {
        "app": "../app"
    }
});
<div id="sunburst-chart"></div>
<script>
	require([
		"splunkjs/ready!",
		"jquery",
		"app/mysginfoV3/components/sunburst/sunburst",
	],
	function(mvc, $, Sunburst) {
		var sunburst = new Sunburst({
			'id' : 'example-sunburst'
			'managerid' : 'sunburst-search',
			'el' : $('#sunburst-chart')
		}).render()
	});
</script>