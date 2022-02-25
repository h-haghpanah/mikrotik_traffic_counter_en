

$(document).ready(function(){

        // Persian Date Picker
        // $(".pdate").pDatepicker({
        //     observer: true,
        //     format: 'YYYY/MM/DD',
        //     altField: '.observer-example-alt'
        // });
        // $('.datepicker').datepicker({
        //     dateFormat: 'yy-mm-dd'
        // })
    
        var show = $('.show');
        $('#toggle').on('click', function() {
            $('#toggle').toggleClass("btn-dark btn-secondary")
            var temp = $('#toggle').html()
            if (temp == "Hide"){
                $('#toggle').html("Change Date Range");
            }else{
            $('#toggle').html("Hide")
            }
            show.fadeToggle();  
        });
    
 
    $('#report').on('click','button',read_users_traffic)
    // var repeat_report = 0
    read_users_traffic("no_event")
    function read_users_traffic(event) {
        var allData2 = $("#report").serializeArray()
        var allData =  $("#report").serialize()
        if(event != "no_event"){
            event.preventDefault()
        allData = allData + "&event=event"
         if(allData2[0].value == "" || allData2[1].value == ""){
            alert("Not valid date.")
        }
            else if(allData2[0].value  ==  allData2[1].value){
                $("#title1").html("").append("Traffic usage in&nbsp;" + allData2[0].value + ' &nbsp; <span class="small">(Gigabyte)</span>')
            }else{
                $("#title1").html("").append("Traffic usage from&nbsp; " + allData2[0].value + ' to '+ allData2[1].value +' &nbsp; <span class="small">(Gigabyte)</span>')
            }
        }
        else{
            allData = allData + "&event=no_event"
            $("#title1").html("").append("  Traffic usage in current month&nbsp;  <span class='small'>(Gigabyte)</span>")

        }
        $.ajax({
            url:"/read_users_traffic",
            method: "POST",
            data:allData,
            success: function(response){
                var content = '';
                if( response[0].length > 0 )
                {
                for (var i in response[0]){
                    content += "<tr>\n"+
                    "<td class='col-md-1 col-sm-1'>"+response[0][i].name+" </td>\n"+
                    "<td class='col-md-1 col-sm-1'>"+response[0][i].download+"</td>\n"+
                    "<td class='col-md-1 col-sm-1'>"+response[0][i].upload+"</td>\n"+
                    "<td class='col-md-1 col-sm-1'>"+response[0][i].total+"</td>\n"+
                "</tr>\n"

                }
                $(".top_ten_users").html("").append(content)
                $("#destination_pie_chart").html("")
                $("#top_ten_chart").html("")
                destination_pie_chart(response[1])
                top_ten_chart(response[2])

            }
            }
        })
    }

    
        function destination_pie_chart (response){
            
                var usage = []
                var destinations = []
                var colors = []
                for (var i in response){
                    usage.push(response[i]["total"])
                    destinations.push(response[i]["destination"])
                    colors.push(response[i]["color_id"])
                
                }
                
            
                var options = {
                    series: usage,
                    chart: {
                    type: 'pie',
                    height: 350,
                },
                fill: {
                    colors: colors
                },
                legend: {
                    markers: {
                        fillColors: colors,

                    }
                },
                labels: destinations,
                responsive: [{
                    breakpoint: 480,
                    options: {
                    chart: {
                        width: 200
                    },
                    
                    legend: {
                        position: 'bottom'
                    }
                    }
                }]
                };
        
                var chart = new ApexCharts(document.querySelector("#destination_pie_chart"), options);
                chart.render();
        }
        function top_ten_chart (response){
            
            var usage = []
            var names = []
            for (var i in response){
                usage.push(response[i]["total"])
                names.push(response[i]["name"])

            }

        
                  
        var options = {
            series: [{
            name:"Usage (Gigabyte)",
            data: usage
          }],
            chart: {
            type: 'bar',
            height: 350,

          },
          plotOptions: {
            bar: {
              borderRadius: 4,
              horizontal: true,
            }
          },
          dataLabels: {
            enabled: true
          },
          xaxis: {
            categories: names
        
          }
          };
  
          var chart = new ApexCharts(document.querySelector("#top_ten_chart"), options);
          chart.render();
    }


  
});