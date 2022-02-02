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
            $('#toggle').html("اضافه کردن کاربر");
        }else{
        $('#toggle').html("پنهان کردن")
        }
        show.fadeToggle();  
    });

    var show2 = $('.show2');
    $('#toggle2').on('click', function() {
        $('#toggle2').toggleClass("btn-dark btn-secondary")
        var temp = $('#toggle2').html()
        if (temp == "پنهان کردن"){
            $('#toggle2').html("اضافه کردن گروه");
        }else{
        $('#toggle2').html("پنهان کردن")
        }
        show2.fadeToggle();  
    });


    read_users()
    function read_users() {
        $.ajax({
            url:"/read_users_without_other",
            method: "get",
            success: function(response){
                var content = '';
                if( response.length > 0 )
                {
                for (var i in response){
                    content += "<tr class='shabnam'>\n"+
                    "<td class='editable col-md-1 col-sm-1 fname'>"+response[i].first_name+" </td>\n"+
                    "<td class='editable col-md-1 col-sm-1 lname'>"+response[i].last_name+"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 uname'>"+response[i].user_name+"</td>\n"+
                    "<td class='editable col-md-2 col-sm-2 email'>"+ response[i].email + "</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 password'>"+ "••••••••" +"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 gname' id='gname"+ response[i].user_id +"'>"+ response[i].group_name +"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 role' id='role"+ response[i].user_id +"'>"+ response[i].role_name +"</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].user_id+"' class='btn btn-dark modify'>ویرایش</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].user_id+"' class='btn btn-secondary delete'>حذف</td>\n"+

                "</tr>\n"
                }
                $("table .table-header").html("<th>نام</th>\n<th>نام خانوادگی</th>\n<th>نام کاربری</th>\n<th>ایمیل</th>\n<th>رمزعبور</th>\n<th>گروه</th>\n<th>دسترسی</th>\n<th>ویرایش</th>\n<th>حذف</th>")
                $(".users-table").html("").append(content)
            }else {
                content ="<div class='jumbotron' style='margin:0 auto;'><h1 class='shabnam mid-font'>هیچ کاربری یافت نشد</h1>"
                $(".table-header").html("").append(content)
                $(".users-table").html("").append(content)

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
                var groups = '<option style="font-family: shabnam;" value="" selected>انتخاب گروه</option>\n'
                if( response.length > 0 )
                {
                for (var i in response){
                    groups += '<option style="font-family: shabnam;" value="' + response[i].group_id +'">' + response[i].group_name + '</option>\n'
                }
                
                $("#gnames").html("").append(groups)
                // $(this).html(content)
            }else {
                groups ='<option style="font-family: shabnam;" id="" >گروهی یافت نشد</option>'
                $("#gnames").html("").append(groups)
                // $(this).html(content)
            }
            }
            
        })
    }

    read_groups_table()
    function read_groups_table() {
        $.ajax({
            url:"/read_groups_without_other",
            method: "get",
            success: function(response){
                var content = '';
                if( response.length > 0 )
                {
                for (var i in response){
                    content += "<tr class='shabnam'>\n"+
                    "<td class='editable col-md-1 col-sm-1 gname'>"+response[i].group_name+" </td>\n"+
                    "<td class='editable col-md-1 col-sm-1 description'>"+response[i].description+"</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].group_id+"' class='btn btn-dark modify'>ویرایش</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].group_id+"' class='btn btn-secondary delete_group'>حذف</td>\n"+

                "</tr>\n"
                }
                $("table .group-table-header").html("<th>نام گروه</th>\n<th>توضیحات</th>\n<th>ویرایش</th>\n<th>حذف</th>")
                $(".groups-table").html("").append(content)
            }else {
                content = "<div class='jumbotron' style='margin:0 auto;'><h1 class='shabnam mid-font'>هیچ گروهی یافت نشد</h1>"
                $(".group-table-header").html("")
                $(".groups-table").html("").append(content)

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
                var roles = '<option style="font-family: shabnam;" value="" selected>انتخاب دسترسی</option>\n'
                if( response.length > 0 )
                {
                for (var i in response){
                    roles += '<option style="font-family: shabnam;" value="' + response[i].role_id +'">' + response[i].role_name + '</option>\n'
                }
                
                $("#role").html("").append(roles)
                // $(this).html(content)
            }else {
                groups ='<option style="font-family: shabnam;" id="" >گروهی یافت نشد</option>'
                $("#role").html("").append(roles)
                // $(this).html(content)
            }
            }
            
        })
    }

    $("table .users-table").on("click",".modify",modify);
    function modify() {
        if(!$(this).hasClass("active")){
        $(this).parent().siblings(".editable").each(function(){
            if($(this).hasClass("gname")){
                var val = $(this).html();
                gname = $(this).attr("id");
                $.ajax({
                    url:"/read_groups",
                    method: "get",
                    success: function(response){
                        var content2 = "<select name='gname' class='form-control shabnam' required>\n";
                        if( response.length > 0 )
                        {
                        for (var i in response){
                            if (val != response[i].group_name){
                            content2 += '<option style="font-family: shabnam;" value="' + response[i].group_id +'" id="' + response[i].group_id +'" >' + response[i].group_name + '</option>\n'
                            }else{
                                content2 += '<option style="font-family: shabnam;" value="' + response[i].group_id +'" id="' + response[i].group_id +'" selected>' + response[i].group_name + '</option>\n'
                            }

                        }
                        content2 = content2 + "</select>"
                        
                        $("#"+gname).html("").append(content2)
                        // $(this).html(content)
                    }else {
                        content2 ='<select class="form-control shabnam" required><option style="font-family: shabnam;" id="" >گروهی یافت نشد</option></select>'
                        $("#gname" + response[i].user_id).html("").append(content2)
                        // $(this).html(content)
                    }
                    }
                    
                })
            
            }else{
            if($(this).hasClass("role")){
                var val = $(this).html();
                role = $(this).attr("id");
                $.ajax({
                    url:"/read_roles",
                    method: "get",
                    success: function(response){
                        var content = "<select name='roles' class='form-control shabnam' required>\n";
                        if( response.length > 0 )
                        {
                        for (var i in response){
                            if (val != response[i].role_name){
                            content += '<option style="font-family: shabnam;" value="' + response[i].role_id +'" id="' + response[i].role_id +'" >' + response[i].role_name + '</option>\n'
                            }else{
                                content += '<option style="font-family: shabnam;" value="' + response[i].role_id +'" id="' + response[i].role_id +'" selected>' + response[i].role_name + '</option>\n'
                            }

                        }
                        content = content + "</select>"
                        
                        $("#"+role).html("").append(content)
                        // $(this).html(content)
                    }else {
                        content ='<select class="form-control shabnam" required><option style="font-family: shabnam;" id="" >دسترسی یافت نشد</option></select>'
                        $("#role" + response[i].user_id).html("").append(content)
                        // $(this).html(content)
                    }
                    }
                    
                })
            
            }else{
                if($(this).hasClass("password")){
                    var val = $(this).html();
                    $(this).html("<input class='form-control' type='password' value='"+ val +"'>")
                }else{
            var val = $(this).html();
            $(this).html("<input class='form-control' type='text' value='"+ val +"'>")
            }}}

        });
        $(this).addClass("active");
        $(this).toggleClass("btn-info btn-warning")
        $(this).html("اعمال")
    }else {
        var id = $(this).attr("id");
        var fname = $(this).parent().siblings(".fname").children("input").val();
        var lname = $(this).parent().siblings(".lname").children("input").val();
        var uname = $(this).parent().siblings(".uname").children("input").val();
        var email = $(this).parent().siblings(".email").children("input").val();
        var password = $(this).parent().siblings(".password").children("input").val();
        var gname = $(this).parent().siblings(".gname").children("select").val();
        var role = $(this).parent().siblings(".role").children("select").val();
        $.ajax({
            url:"/update_user",
            method: "post",
            data: {
                id : id,
                fname : fname,
                lname : lname,
                uname : uname,
                email : email,
                password : password,
                gname : gname,
                role  : role
            },
            success: function(response){
                if(response == "1"){
                read_users();
                }
                else if(response == "not_valid"){
                    alert("نام ، نام کاربری ،گروه و ایمیل نمی تواند خالی باشد")
                }
                else if(response == "user_exist"){
                    alert("کاربری با این نام کاربری موجود است")
                }
                else if(response == "email_exist"){
                    alert("کاربری با این ایمیل موجود است")
                }else{
                    alert("خطایی رخ داده است")
                }

            }
        })
    }
    }



    $("table .groups-table").on("click",".modify",modify_groups);
    function modify_groups() {
        if(!$(this).hasClass("active")){
        $(this).parent().siblings(".editable").each(function(){
            var val = $(this).html();
            $(this).html("<input class='form-control' type='text' value='"+ val +"'>")
        });
        $(this).addClass("active");
        $(this).toggleClass("btn-dark btn-secondary")
        $(this).html("اعمال")
    }else {
        var id = $(this).attr("id");
        var gname = $(this).parent().siblings(".gname").children("input").val();
        var description = $(this).parent().siblings(".description").children("input").val();
        $.ajax({
            url:"/update_group",
            method: "post",
            data: {
                id : id,
                gname : gname,
                description : description,
            },
            success: function(response){
                if(response == "1"){
                read_groups();
                read_groups_table();
                }
                else if(response == "group_name_exist"){
                    alert("نام گروه تکراری است")
                }
                else if(response == "other_not_valid"){
                    alert("نام 'دیگر' مجاز نیست")
                }
                else{
                    alert("خطایی رخ داده است")
                }
  
            }
        })
    }
    }




    $("div").on("click",".delete",delete_alert);
    function delete_alert(event){
        event.preventDefault();
        Swal.fire({
            title: '<span class="shabnam rtl_class big-font">آیا مطمعن هستید؟</span>',
            html: '<span " class="shabnam rtl_class">این عمل غیر قابل بازگشت است</span>',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText: '<span class="shabnam rtl_class">بیخیال</span>',
            confirmButtonText: '<span class="shabnam rtl_class">بله ، پاکش کن</span>'
            }).then((result) => {
            if (result.isConfirmed) {
                var id = $(this).attr("id");
                deleteuser(id);
                Swal.fire(
                '<span class="shabnam rtl_class">کاربر شما با موفقیت پاک شد</span>',
                '',
                'success'
                )
            }
            })
    }

    function deleteuser(id){
        
        $.ajax({
            url:"/delete_user",
            method: "post",
            data: {id : id},
            success: function(response){
                if(response == "1"){
                    read_users();
                    }
                    else{
                        alert("خطایی رخ داده است")
                    }

            }
        })
    }


    $("div").on("click",".delete_group",delete_alert);
    function delete_alert(event){
        event.preventDefault();
        Swal.fire({
            title: '<span class="shabnam rtl_class big-font">آیا مطمعن هستید؟</span>',
            html: '<span " class="shabnam rtl_class">این عمل غیر قابل بازگشت و تمام کاربران زیر مجموعه آن هم پاک خواهد شد</span>',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText: '<span class="shabnam rtl_class">بیخیال</span>',
            confirmButtonText: '<span class="shabnam rtl_class">بله ، پاکش کن</span>'
            }).then((result) => {
            if (result.isConfirmed) {
                var id = $(this).attr("id");
                deletegroup(id);
                Swal.fire(
                '<span class="shabnam rtl_class">گروه شما با موفقیت پاک شد</span>',
                '',
                'success'
                )
            }
            })
    }

    function deletegroup(id){
        
        $.ajax({
            url:"/delete_group",
            method: "post",
            data: {id : id},
            success: function(response){
                if(response == "1"){
                    read_groups();
                    read_groups_table();
                    }
                    else{
                        alert("خطایی رخ داده است")
                    }

            }
        })
    }





    $('#add_user').on('click','button',add_user)
    
    function add_user(event){
        event.preventDefault();
        var allData = $("#add_user").serialize();
        $.ajax({
            url:"/add_user",
            method: "post",
            data: allData,
            success: function(response){
                if (response == 1){
                    $("input").val("");
                    read_users()
                }else if(response == "not_valid"){
                    alert("نام ، نام کاربری ،گروه ، دسترسی و ایمیل نمی تواند خالی باشد")
                }else if(response == "user_exist"){
                    alert("کاربری با این نام کاربری موجود است")
                    }
                    else if(response == "email_exist"){
                        alert("کاربری با این ایمیل موجود است")
                        }else{
                            alert("خطایی رخ داده است")
                        }
                }
            
        })
        
    }

    $('#add_group').on('click','button',add_group)
    
    function add_group(event){
        event.preventDefault();
        var allData = $("#add_group").serialize();
        $.ajax({
            url:"/add_group",
            method: "post",
            data: allData,
            success: function(response){
                if (response == 1){
                    $("input").val("");
                    read_groups()
                    read_groups_table()
                }else if(response == "not_valid"){
                    alert("نام نمی تواند خالی باشد")
                }else if(response == "group_exist"){
                    alert("گروهی با این نام موجود است")
                    }
                    else{
                            alert("خطایی رخ داده است")
                        }
                }
            
        })
        
    }


});