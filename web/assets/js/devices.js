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
            $('#toggle').html("Add device");
        }else{
        $('#toggle').html("Hide")
        }
        show.fadeToggle();  
    });

    var show2 = $('.show2');
    $('#toggle2').on('click', function() {
        $('#toggle2').toggleClass("btn-dark btn-secondary")
        var temp = $('#toggle2').html()
        if (temp == "Hide"){
            $('#toggle2').html("Show devices");
        }else{
        $('#toggle2').html("Hide")
        }
        show2.fadeToggle();  
    });
    
    read_users()
    function read_users() {
        $.ajax({
            url:"/read_users",
            method: "get",
            success: function(response){
                var items = '<option style="justfy" value="" disabled>Select User</option>\n<option style="justfy" value="all" selected> تمام کاربران</option>\n';
                if( response.length > 0 )
                {
                for (var i in response){
                    items += 
                    '<option style="font-family: shabnam;" value="' + response[i].user_id +'" >' + response[i].first_name + ' ' + response[i].last_name + '</option>\n'
                }
                $("#users_list").html("").append(items)
            }else {
                items +='<option style="font-family: shabnam;" value="" >No user found</option>\n'
                $("#users_list").html("").append(items)
            }
            }
        })
    }

    $('#show_devices').on('click','button',show_devices2)

    function show_devices2(event){
        event.preventDefault()
        var id = $("#show_devices").serialize()
        show_devices(id)
    }

    function show_devices(id) {
        $.ajax({
            url:"/read_devices_without_other",
            method: "post",
            data: id,
            success: function(response){
                var content = '';
                if( response.length > 0 )
                {
                for (var i in response){
                    var ip_value = response[i].ip_value;
                    if(ip_value == null || ip_value == ""){
                        ip_value = "Without IP"
                    }
                    content += "<tr class='shabnam'>\n"+
                    "<td class='editable col-md-1 col-sm-1 dname'>"+response[i].device_name+" </td>\n"+
                    "<td class='editable col-md-1 col-sm-1 model'>"+response[i].model+"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 ip' id='"+response[i].ip_id+"'>"+ip_value+"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 tname' id='tname"+ response[i].device_id +"'>"+ response[i].type_name +"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 uname' id='uname"+ response[i].device_id +"'>"+ response[i].user_name +"</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].device_id+"' class='btn btn-dark modify'>Modify</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].device_id+"' class='btn btn-secondary delete'>Delete</td>\n"+

                "</tr>\n"
                }
                $("table .table-header").html("<th style='text-align:center'>Name</th>\n<th style='text-align:center'>Model</th>\n<th style='text-align:center'>IP</th>\n<th style='text-align:center'>Type</th>\n<th style='text-align:center'>User</th>\n<th style='text-align:center'>Modify</th>\n<th style='text-align:center'>Delete</th>")
                $(".devices-table").html("").append(content)
            }else {
                content ="<div class='jumbotron' style='margin:0 auto;'><h1 class='shabnam mid-font'>No device found</h1>"
                $(".table-header").html("").append(content)
                $(".devices-table").html("")
            }

            }
        })
    }

    read_groups()
    function read_groups() {
        $.ajax({
            url:"/read_groups",
            method: "get",
            success: function(response){
                var groups = '<option style="font-family: shabnam;" value="" selected>Select Group</option>\n'
                if( response.length > 0 )
                {
                for (var i in response){
                    groups += '<option style="font-family: shabnam;" value="' + response[i].group_id +'">' + response[i].group_name + '</option>\n'
                }
                
                $("#gnames").html("").append(groups)
                // $(this).html(content)
            }else {
                groups ='<option style="font-family: shabnam;" id="" >No group found</option>'
                $("#gnames").html("").append(groups)
                // $(this).html(content)
            }
            }
            
        })
    }

    read_roles()
    function read_roles() {
        $.ajax({
            url:"/read_roles",
            method: "get",
            success: function(response){
                var roles = '<option style="font-family: shabnam;" value="" selected>Select role</option>\n'
                if( response.length > 0 )
                {
                for (var i in response){
                    roles += '<option style="font-family: shabnam;" value="' + response[i].role_id +'">' + response[i].role_name_en + '</option>\n'
                }
                
                $("#role").html("").append(roles)
                // $(this).html(content)
            }else {
                groups ='<option style="font-family: shabnam;" id="" >No group found</option>'
                $("#role").html("").append(roles)
                // $(this).html(content)
            }
            }
            
        })
    }

    $("table .devices-table").on("click",".modify",modify);
    function modify() {
        if(!$(this).hasClass("active")){
        $(this).parent().siblings(".editable").each(function(){
            if($(this).hasClass("tname")){
                var val = $(this).html();
                tname = $(this).attr("id");
                $.ajax({
                    url:"/read_device_types",
                    method: "get",
                    success: function(response){
                        var content2 = "<select name='gname' class='form-control shabnam' required>\n";
                        if( response.length > 0 )
                        {
                        for (var i in response){
                            if (val != response[i].type_name){
                            content2 += '<option style="font-family: shabnam;" value="' + response[i].type_id +'" id="' + response[i].type_id +'" >' + response[i].type_name + '</option>\n'
                            }else{
                                content2 += '<option style="font-family: shabnam;" value="' + response[i].type_id +'" id="' + response[i].type_id +'" selected>' + response[i].type_name + '</option>\n'
                            }

                        }
                        content2 = content2 + "</select>"
                        
                        $("#"+tname).html("").append(content2)
                        // $(this).html(content)
                    }else {
                        content2 ='<select class="form-control shabnam" required><option style="font-family: shabnam;" id="" >گروهی یافت نشد</option></select>'
                        $("#tname" + response[i].device_id).html("").append(content2)
                        // $(this).html(content)
                    }
                    }
                    
                })
            
            }else{
            if($(this).hasClass("uname")){
                var val = $(this).html();
                uname = $(this).attr("id");
                $.ajax({
                    url:"/read_users_without_other",
                    method: "get",
                    success: function(response){
                        var content = "<select name='unames' class='form-control shabnam' required>\n";
                        if( response.length > 0 )
                        {
                        for (var i in response){
                            if (val != response[i].user_name){
                            content += '<option style="font-family: shabnam;" value="' + response[i].user_id +'" id="' + response[i].user_id +'" >' + response[i].user_name + '</option>\n'
                            }else{
                                content += '<option style="font-family: shabnam;" value="' + response[i].user_id +'" id="' + response[i].user_id +'" selected>' + response[i].user_name + '</option>\n'
                            }

                        }
                        content = content + "</select>"
                        
                        $("#"+uname).html("").append(content)
                        // $(this).html(content)
                    }else {
                        content ='<select class="form-control shabnam" required><option style="font-family: shabnam;" id="" >No role found</option></select>'
                        $("#uname" + response[i].device_id).html("").append(content)
                        // $(this).html(content)
                    }
                    }
                    
                })
            
            }else{
            var val = $(this).html();
            if(val == " Without IP"){
                $(this).html("<input class='form-control' type='text' value=''>")
            }else{
            $(this).html("<input class='form-control' type='text' value='"+ val +"'>")
            }
            }}

        });
        $(this).addClass("active");
        $(this).toggleClass("btn-info btn-warning")
        $(this).html("Apply")
    }else {
        var id = $(this).attr("id");
        var dname = $(this).parent().siblings(".dname").children("input").val();
        var model = $(this).parent().siblings(".model").children("input").val();
        var ip = $(this).parent().siblings(".ip").children("input").val();
        var ip_id = $(this).parent().siblings(".ip").attr("id")
        var tname = $(this).parent().siblings(".tname").children("select").val();
        var uname = $(this).parent().siblings(".uname").children("select").val();
        $.ajax({
            url:"/update_device",
            method: "post",
            data: {
                id : id,
                dname : dname,
                model : model,
                ip : ip,
                tname : tname,
                uname : uname,
                ip_id : ip_id
            },
            success: function(response){
                if(response == "1"){
                show_devices("user="+uname);
                }
                else if(response == "not_valid"){
                    alert("Name,username,group and email connot be empty.")
                }
                else if(response == "user_exist"){
                    alert("This username exist.")
                }
                else if(response == "email_exist"){
                    alert("This email exist")
                }else{
                    alert("Something happend")
                }

            }
        })
    }
    }

    $("div").on("click",".delete",delete_alert);
    function delete_alert(event){
        event.preventDefault();
        Swal.fire({
            title: '<span class="shabnam rtl_class big-font">Are you sure ?</span>',
            html: '<span " class="shabnam rtl_class">This action connot be reverted.</span>',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText: '<span class="shabnam rtl_class">Cansel</span>',
            confirmButtonText: '<span class="shabnam rtl_class">Yes,delete it</span>'
            }).then((result) => {
            if (result.isConfirmed) {
                var id = $(this).attr("id");
                deletedevice(id);
                Swal.fire(
                '<span class="shabnam rtl_class">Your device deleted successfully</span>',
                '',
                'success'
                )
            }
            })
    }

    function deletedevice(id){
        
        $.ajax({
            url:"/delete_device",
            method: "post",
            data: {id : id},
            success: function(response){
                show_devices("user="+response);
            }
        })
    }


    $('#add_device').on('click','button',add_device)
    
    function add_device(event){
        event.preventDefault();
        var allData = $("#add_device").serialize();
        var allData2 = $("#add_device").serializeArray();
        $.ajax({
            url:"/add_device",
            method: "post",
            data: allData,
            success: function(response){
                if (response == 1){
                    $("input").val("");
                    show_devices("user="+allData2[3]["value"])
                }else if(response == "not_valid"){
                    alert("All fields are required.")
                }else if(response == "device_exist"){
                    alert("Device this name is exist for current user.")
                    }
                    else if(response == "wrong_ip"){
                        alert("IP address is wrong or not in local nerwork ranges.")
                        }else{
                            alert(response)
                        }
                }
            
        })
        
    }
    read_users()
    function read_users(){
        $.ajax({
            url:"/read_users_without_other",
            method: "get",
            success: function(response){
                var content = "";
                if( response.length > 0 )
                {
                for (var i in response){
                    content += '<option style="font-family: shabnam;" value="' + response[i].user_id +'" id="' + response[i].user_id +'" >' + response[i].user_name + '</option>\n'
                }
                $("#user").html("").append(content)
                $("#users_list").html("").append(content)
            }else {
                content ='<option style="font-family: shabnam;" id="" >No user found</option>'
                $("#user").html("").append(content)
                $("#users_list").html("").append(content)
            }
            }
            
        })

    }

    read_types()
    function read_types(){
        $.ajax({
            url:"/read_device_types",
            method: "get",
            success: function(response){
                var content = "";
                if( response.length > 0 )
                {
                for (var i in response){
                    content += '<option style="font-family: shabnam;" value="' + response[i].type_id +'" id="' + response[i].type_id +'" >' + response[i].type_name + '</option>\n'
                }
                $("#type").html("").append(content)
            }else {
                content ='<option style="font-family: shabnam;" id="" >No type found</option>'
                $("#type").html("").append(content)
            }
            }
            
        })

    }

    var ipv4_address = $('#ipv4');
    ipv4_address.inputmask({
    alias: "ip",
    greedy: false 
    });

  
});