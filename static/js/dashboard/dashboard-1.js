
(function($) {
    "use strict"

		const marketOverview = document.getElementById("market-overview")
		const marketOverviewParsed = JSON.parse(marketOverview.textContent)

 var dzChartlist = function(){
	
	var marketChart = function(){
		 var options = {
          series: marketOverviewParsed.data,
          chart: {
          height: 300,
          type: 'area',
		  toolbar:{
			  show:false
		  }
        },
		colors:["#FFAB2D","#00ADA3","#6418C3", "#0DDF5E"],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth',
		  width:3
        },
		legend:{
			show:false
		},
		grid:{
			show:false,
			strokeDashArray: 6,
			borderColor: '#dadada',
		},
		yaxis: {
		  labels: {
			style: {
				colors: '#B5B5C3',
				fontSize: '12px',
				fontFamily: 'Poppins',
				fontWeight: 400
				
			},
			formatter: function (value) {
			  return value;
			}
		  },
		},
        xaxis: {
          categories: marketOverviewParsed.dates,
		  labels:{
			  style: {
				colors: '#B5B5C3',
				fontSize: '12px',
				fontFamily: 'Poppins',
				fontWeight: 400
				
			},
		  }
        },
		fill:{
			type:'solid',
			opacity:0.05
		},
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          },
        },
        };


        var chart = new ApexCharts(document.querySelector("#marketChart"), options);
        chart.render();

	}
	var currentChart = function(){
		 var options = {
          series: [85, 60, 67, 50],
          chart: {
          height: 315,
          type: 'radialBar',
        },
        plotOptions: {
          radialBar: {
				startAngle:-90,
			   endAngle: 90,
            dataLabels: {
              name: {
                fontSize: '22px',
              },
              value: {
                fontSize: '16px',
              },
            }
          },
        },
		stroke:{
			 lineCap: 'round',
		},
        labels: ['Income', 'Income', 'Imcome', 'Income'],
		 colors:['#ec8153', '#70b944','#498bd9','#6647bf'],
        };

        var chart = new ApexCharts(document.querySelector("#currentChart"), options);
        chart.render();
	}
	
	var recentContact = function(){
		jQuery('.testimonial-one').owlCarousel({
			loop:true,
			autoplay:true,
			margin:20,
			nav:false,
			rtl:true,
			dots: false,
			navText: ['', ''],
			responsive:{
				0:{
					items:3
				},
				450:{
					items:4
				},
				600:{
					items:5
				},	
				991:{
					items:5
				},			
				
				1200:{
					items:7
				},
				1601:{
					items:5
				}
			}
		})
	}
	
	/* Function ============ */
		return {
			init:function(){
			},
			
			load:function(){
					marketChart();
					currentChart();
					recentContact();
					
			},
			
			resize:function(){
			},
			
		}
	
	}();


		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzChartlist.load();
		}, 500); 
		
	});

	jQuery(window).on('resize',function(){
		
		
	});     

})(jQuery);