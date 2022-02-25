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
        if (temp == "Hide"){
            $('#toggle').html("Change Date Range");
        }else{
        $('#toggle').html("Hide")
        }
        show.fadeToggle();  
    });
    read_users()
    function read_users() {
        $.ajax({
            url:"/read_users",
            method: "get",
            success: function(response){
                var items = '<option style="justfy" value="" disabled> انتخاب کاربر</option>\n<option style="justfy" value="all" selected> تمام کاربران</option>\n';
                if( response.length > 0 )
                {
                for (var i in response){
                    items += 
                    '<option style="font-family: shabnam;" value="' + response[i].user_id +'" >' + response[i].first_name + ' ' + response[i].last_name + '</option>\n'
                }
                $("#company").html("").append(items)
            }else {
                items +='<option style="font-family: shabnam;" value="" >کاربری یافت نشد</option>\n'
                $(".content-overview").html("").append(items)
            }
            }
        })
    }
    $('#report').on('click','button',read_report)

    read_report("no_event")
    function read_report(event) {
        if(event != "no_event"){
            event.preventDefault()
        }
        var allData = $("#report").serialize()
        var allData2 = $("#report").serializeArray()
        if (event == "no_event"){
            date1="this_month"
            date2="this_month"
            allData = "date1="+date1+"&date2="+date2+"&id=all"


        }
        read_report_table(event,allData,allData2)
    }

    function read_report_table(event,allData,allData2) {
        if(event != "no_event"){
            event.preventDefault()
        }
        if(event == "no_event"){
            $("#title1").html("").append("  Traffic usage in current month&nbsp;  <span class='small'>(Gigabyte)</span>")
        }
        else if(allData2[0].value == "" || allData2[1].value == ""){
            alert("Not valid date.")
        }
        else if(allData2[0].value  ==  allData2[1].value){
            $("#title1").html("").append("Traffic usage in&nbsp;" + allData2[0].value + ' &nbsp; <span class="small">(Gigabyte)</span>')
        }else{
            $("#title1").html("").append("Traffic usage from&nbsp; " + allData2[0].value + ' to '+ allData2[1].value +' &nbsp; <span class="small">(Gigabyte)</span>')
        }
        $.ajax({
            url:"/read_users_full_report",
            method: "post",
            data : allData,
            success: function(response){
                var content1 = '';
                var content2 = '';
                var content3 = '';
                var content4 = '';
                var total_traffic = 0.00 ;
                if( response.length > 0 )
                {
                for(var i in response[0]){ //users
                    for(var j in response[0][i]){
                        for(var k in response[0][i][j]){
                            if(j == response[0][i].length-1 && k == response[0][i][j].length -1 ){
                            var sum_of_download_upload = (parseFloat(response[0][i][j][k].download) + parseFloat(response[0][i][j][k].upload)).toFixed(2)
                            total_traffic = (parseFloat(total_traffic) + parseFloat(sum_of_download_upload)).toFixed(2)
                            rows = response[0][i].length * response[0][i][j].length
                            content1 += "<tr class='shabnam'>\n"+
                            "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].first_name+ " " + response[0][i][j][k].last_name+" </td>\n"+
                            "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].device_name+"</td>\n"+
                            "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].destination_name+"</td>\n"+
                            "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].download+ " / " + response[0][i][j][k].upload + "</td>\n"+
                            "<td class='col-md-1 col-sm-1'>"+ sum_of_download_upload +"</td>\n"+
                            "<td class='col-md-1 col-sm-1' rowspan='"+ rows + "'>"+ total_traffic +"</td>\n"+
                        "</tr>\n"
                        total_traffic = 0.00
                            }
                            else{
                                var sum_of_download_upload = (parseFloat(response[0][i][j][k].download) + parseFloat(response[0][i][j][k].upload)).toFixed(2)
                                total_traffic = parseFloat(total_traffic) + parseFloat(sum_of_download_upload)
                                content2 += "<tr class='shabnam'>\n"+
                                "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].first_name+ " " + response[0][i][j][k].last_name+" </td>\n"+
                                "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].device_name+"</td>\n"+
                                "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].destination_name+"</td>\n"+
                                "<td class='col-md-1 col-sm-1'>"+response[0][i][j][k].download+ " / " + response[0][i][j][k].upload + "</td>\n"+
                                "<td class='col-md-1 col-sm-1'>"+ sum_of_download_upload +"</td>\n"+
                            "</tr>\n"
                            }
        
                        }
                        content3 = content1+content2
                        }
                        content4 = content4 + content3
                        content1 = ""
                        content2 = ""
                        content3 = ""
                    }
                    $("#destination_pie_chart").html("")
                    $("#devices_pie_chart").html("")
                    destination_pie_chart(response[1])
                    devices_pie_chart(response[2])
                    $(".report_table").html("").append(content4)
                    
                }
                $("table .table-header").html("<th>Name</th>\n<th>Device</th>\n<th>Destination</th>\n<th>Traffic (Download/Upload)</th>\n<th>Sum</th>\n<th>Total Traffic</th>")//.append(no_content)
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

        function devices_pie_chart (response){
            
            var usage = []
            var names = []

            for (var i in response){
                usage.push(response[i]["total"])
                names.push(response[i]["name"])
            
            }
            
        
            var options = {
                series: usage,
                chart: {
                type: 'pie',
                height: 350,
                fontFamily: 'shabnam'
            },
            labels: names,
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
    
            var chart = new ApexCharts(document.querySelector("#devices_pie_chart"), options);
            chart.render();
    }


   
});