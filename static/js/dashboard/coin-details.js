(function($) {
     "use strict" 

	const graphData = document.querySelector('#graph-data')
	const graphDataParsed = JSON.parse(graphData.textContent)

	const dates = [];
	const prices = [];
	
	for (const objeto of graphDataParsed) {
		const datesObject = Object.keys(objeto);
		const pricesValores = Object.values(objeto);
		dates.push(datesObject[0]);
		prices.push(pricesValores[0]);
	}

	var dzChartlist = function(){
	
	var screenWidth = $(window).width();
		var chartBarRunning = function(){
			 var options = {
          series: [{
          data: prices
        },],
          chart: {
          height: 350,
          type: 'area',
		  toolbar:{
			  show:false
		  },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth',
		  width:3
        },
		grid:{
			show:false
		},
        xaxis: {
          type: 'Day',
          categories: dates,
		   labels:{
			    show: true,
				style:{
					 colors:'#808080',
				},
		   },
        },
		 yaxis: {
			labels: {
				 formatter: function (value) {
				  return value + "k";
				},
				style: {
					colors: '#787878',
					fontSize: '13px',
					fontFamily: 'Poppins',
					fontWeight: 400
				},
			},
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          },
        },
		colors:['#ffab2d']
        };

        var chart = new ApexCharts(document.querySelector("#chartBarRunning"), options);
        chart.render();
		
		
	}

	
	/* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){			
				chartBarRunning();				
			},
			
			resize:function(){
			}
		}
	
	}();

	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzChartlist.load();
		}, 1000); 
		
	});

	jQuery(window).on('resize',function(){
		
		
	});     

})(jQuery);