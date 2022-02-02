$(document).ready(function(){

 
    var show = $('.show');
    $('#toggle').on('click', function() {
        $('#toggle').toggleClass("btn-dark btn-secondary")
        var temp = $('#toggle').html()
        if (temp == "پنهان کردن"){
            $('#toggle').html("اضافه کردن مقصد");
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
            $('#toggle2').html("اضافه کردن آدرس");
        }else{
        $('#toggle2').html("پنهان کردن")
        }
        show2.fadeToggle();  
    });



    read_destinations()
    function read_destinations() {
        $.ajax({
            url:"/read_destinations",
            method: "get",
            success: function(response){
                var content = '';
                if( response.length > 0 )
                {
                for (var i in response){
                    content += "<tr class='shabnam'>\n"+
                    "<td class='editable col-md-1 col-sm-1 dname'>"+response[i].destination_name+" </td>\n"+
                    "<td class='editable col-md-1 col-sm-1 description'>"+response[i].descriptions+"</td>\n"+
                    "<td class='editable col-md-1 col-sm-1 color'><input style='height: 35px; max-width: 40px; padding:0; display:inline-block;' type='color' class='form-control form-control-color' value='"+response[i].color_id+"' title='Choose your color' disabled></input></td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].destination_id+"' class='btn btn-dark modify'>ویرایش</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].destination_id+"' class='btn btn-secondary delete_dst'>حذف</td>\n"+
                "</tr>\n"
                }
                $("table .table-header-destination").html("<th>نام</th>\n<th>توضیحات</th>\n<th>رنگ</th>\n<th>ویرایش</th>\n<th>حذف</th>")
                $(".destination-table").html("").append(content)
            }else {
                content = "<div class='jumbotron' style='margin:0 auto;'><h1 class='shabnam mid-font'>مقصدی یافت نشد</h1>"
                $(".table-header").html("").append(Content)
            }

            }
        })
    }

    read_destinations_dropdown()
    function read_destinations_dropdown() {
        $.ajax({
            url:"/read_destinations",
            method: "get",
            success: function(response){
                var content = '<option style="font-family: shabnam;" value="" selected disabled>انتخاب مقصد</option>\n';
                if( response.length > 0 )
                {
                for (var i in response){
                    content += '<option style="font-family: shabnam;" value="'+ response[i].destination_id +'">'+ response[i].destination_name +'</option>\n'
                }
                $("#destination").html("").append(content)
            }else {
                content = '<option style="font-family: shabnam;" value="" selected disabled>مقصدی یافت نشد</option>\n'
                $("#destination").html("").append(Content)
            }

            }
        })
    }


    read_addresses()
    function read_addresses() {
        $.ajax({
            url:"/read_addresses",
            method: "get",
            success: function(response){
                var content = '';
                if( response.length > 0 )
                {
                for (var i in response){
                    content += "<tr class='shabnam'>\n"+
                    "<td class='editable col-md-1 col-sm-1 dname'>"+response[i].destination_address+" </td>\n"+
                    "<td class='editable col-md-1 col-sm-1 description'>"+response[i].destination_name+"</td>\n"+
                    // "<td class='col-md-1 col-sm-1'><button id='"+response[i].destination_id+"' class='btn btn-dark modify'>ویرایش</td>\n"+
                    "<td class='col-md-1 col-sm-1'><button id='"+response[i].destination_address_id+"' class='btn btn-secondary delete'>حذف</td>\n"+
                "</tr>\n"
                }
                $("table .table-header-address").html("<th>آدرس</th>\n<th>مقصد</th>\n<th>حذف</th>")
                $(".address-table").html("").append(content)
            }else {
                content = "<div class='jumbotron' style='margin:0 auto;'><h1 class='shabnam mid-font'>آدرسی یافت نشد</h1>"
                $(".table-header").html("").append(Content)
            }

            }
        })
    }


  $('#add_destination').on('click','button',add_destination)
  
  function add_destination(event){
      event.preventDefault();
      var allData = $("#add_destination").serialize();
      $.ajax({
          url:"/add_destination",
          method: "post",
          data: allData,
          success: function(response){
              if (response == 1){
                read_destinations()
                read_destinations_dropdown()
                $("input").val("");
                }else if(response == "destination_exist"){
                  alert("مقصدی با این نام موجود است")
                }
              }
          
      })
      
  }

  $('#add_address').on('click','button',add_address)
  
  function add_address(event){
      event.preventDefault();
      var allData = $("#add_address").serialize();
      $.ajax({
          url:"/add_address",
          method: "post",
          data: allData,
          success: function(response){
              if (response == 1){
                read_addresses()
                $("input").val("");
                }else if(response == "address_exist"){
                  alert("این آدرس موجود است")
                }
              }
          
      })
      
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
              delete_address(id);
              Swal.fire(
              '<span class="shabnam rtl_class">آدرس شما با موفقیت پاک شد</span>',
              '',
              'success'
              )
          }
          })
  }

  function delete_address(id){
      
      $.ajax({
          url:"/delete_address",
          method: "post",
          data: {id : id},
          success: function(response){
              read_addresses();
          }
      })
  }


  $("div").on("click",".delete_dst",delete_alert_dst);
  function delete_alert_dst(event){
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
              delete_destination(id);
              Swal.fire(
              '<span class="shabnam rtl_class">مقصد شما با موفقیت پاک شد</span>',
              '',
              'success'
              )
          }
          })
  }

  function delete_destination(id){
      
      $.ajax({
          url:"/delete_destination",
          method: "post",
          data: {id : id},
          success: function(response){
              read_destinations()
              read_destinations_dropdown
          }
      })
  }



  $("table .destination-table").on("click",".modify",modify);
  function modify() {
      if(!$(this).hasClass("active")){
      $(this).parent().siblings(".editable").each(function(){
          if ($(this).hasClass("color")){
              val = $(this).children().val()
              $(this).children().removeAttr("disabled")
          }else{
          var val = $(this).html();
          $(this).html("<input class='form-control' type='text' value='"+ val +"'>")
          }

      });
      $(this).addClass("active");
      $(this).toggleClass("btn-dark btn-secondary")
      $(this).html("اعمال")
  }else {
      var id = $(this).attr("id");
      var dname = $(this).parent().siblings(".dname").children("input").val();
      var description = $(this).parent().siblings(".description").children("input").val();
      var color = $(this).parent().siblings(".color").children("input").val();
      $.ajax({
          url:"/update_destination",
          method: "post",
          data: {
              id : id,
              dname : dname,
              description : description,
              color : color
          },
          success: function(response){
              if(response == "1"){
              read_destinations();
              read_destinations_dropdown();
              read_addresses();
              }
              else if(response == "dstination_name_exist"){
                  alert("نام مقصد تکراری است")
              }
              else{
                  alert("خطایی رخ داده است")
              }

          }
      })
  }
  }

  
});


