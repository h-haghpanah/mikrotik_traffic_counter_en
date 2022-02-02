$(document).ready(function(){

        // Persian Date Picker
        $(".pdate").pDatepicker({
            observer: true,
            format: 'YYYY/MM/DD',
            altField: '.observer-example-alt'
        });
        
    
        var show = $('.show');
        $('#toggle').on('click', function() {
            $('#toggle').toggleClass("btn-dark btn-secondary")
            var temp = $('#toggle').html()
            if (temp == "پنهان کردن"){
                $('#toggle').html("تغییر بازه زمانی");
            }else{
            $('#toggle').html("پنهان کردن")
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
            if(allData2[0].value  ==  allData2[1].value){
                $("#title1").html("").append("  مصرف اینترنت  در تاریخ&nbsp;" + allData2[0].value + ' &nbsp; <span class="small">(دانلود  /  آپلود) گیگابایت</span>')
            }else{
                $("#title1").html("").append("مصرف اینترنت  از تاریخ&nbsp; " + allData2[0].value + ' تا تاریخ '+ allData2[1].value +' &nbsp; <span class="small">(دانلود  /  آپلود) گیگابایت</span>')
            }
        }
        else{
            allData = allData + "&event=no_event"
            $("#title1").html("").append("  مصرف اینترنت  در ماه جاری&nbsp;  <span class='small'>(دانلود  /  آپلود) گیگابایت</span>")

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
                    content += "<tr class='shabnam'>\n"+
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

                // if(event == "no_event"){
                //     repeat_report = repeat_report + 1
                // }
                // if(event != "no_event" && repeat_report%2 == 0){
                //     repeat_report = repeat_report + 1
                //     document.getElementById("report_btn").click();
                // }
                // else{
                //     repeat_report = repeat_report + 1
                // }
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
                    fontFamily: 'shabnam'
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
            name:"مصرف (گیگابایت)",
            data: usage
          }],
            chart: {
            type: 'bar',
            height: 350,
            fontFamily: 'shabnam'
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