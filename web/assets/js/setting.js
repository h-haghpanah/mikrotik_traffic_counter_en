$(document).ready(function(){

    mikrotik_info()
    function mikrotik_info(){
      $.ajax({
        url:"/read_mikrotik_info",
        method: "GET",
        success: function(response){
              $("#mikrotik_ip").val(response["mikrotik_address"])
              $("#mikrotik_port").val(response["mikrotik_port"])
              $("#mikrotik_id").attr("data",(response["mikrotik_id"]))
              }

        
    })
      
    }


$("#mikrotik").on("click",".modify_mikrotik",modify_mikrotik);
function modify_mikrotik(event) {
  event.preventDefault()
  if ($(this).html() == "Modify"){
    $(this).parent().siblings().children().children("input").removeAttr("disabled")
    $(this).toggleClass("btn-black btn-secondary")
    $(this).html("Apply")
  }else{
  var id = $(this).attr("data")
  var alldata = $("#mikrotik").serialize();
  $(this).parent().siblings().children().children("input").attr("disabled","disabled")
  $(this).html("Modify")
  alldata = alldata + "&id=" + id     
  $.ajax({
    url:"/update_mikrotik_info",
    method: "post",
    data: alldata,
    success: function(response){
        if (response == 1){
          mikrotik_info()
          
          }
        }
    
})
  }
}

    var show = $('.show');
    $('#toggle').on('click', function() {
        $('#toggle').toggleClass("btn-dark btn-secondary")
        var temp = $('#toggle').html()
        if (temp == "Hide"){
            $('#toggle').html("Add local network");
        }else{
        $('#toggle').html("Hide")
        }
        show.fadeToggle();  
    });

    local_lan()
    function local_lan(){
      $.ajax({
        url:"/read_local_lan",
        method: "get",
        success: function(response){
            var items = '';
            if( response.length > 0 )
            {
            for (var i in response){
                items += '<div class="form-row" style="margin-top: 20px;">\n'+
                '<div class="col-lg-3 col-xl-3 col-sm-4 col-6 col-md-4">\n'+
                    '<div class="input-group">\n'+
                      '<div class="input-group-prepend"></div>\n'+
                      '<input type="text" id="ip'+response[i][2]+'" name="ip" class="form-input form-control ip shabnam editable" data="'+response[i][2]+'" value="'+response[i][0]+'" placeholder="xxx.xxx.xxx.xxx" required disabled>\n'+
                      '<span style="font-size: 25px;">/</span>\n'+
                      '<input type="number" name="" class="form-input form-control mask shabnam editable" data="'+response[i][2]+'" value="'+response[i][1]+'" style="max-width: 100px;" id="mask'+response[i][2]+'" min="1" max="32" maxlength="2" placeholder="Netmask" disabled>\n'+
                    '</div>\n'+
                '</div>\n'+

                '<div id="edit" class="col">\n'+
                      '<button id="'+response[i][2]+'" type="submit"  class="btn btn-dark btn-xs shabnam modify" dir="rtl">Modify</button>\n'+
                      '<button id="'+response[i][2]+'" type="submit"  class="btn btn-secondary btn-xs shabnam delete" dir="rtl">Delete</button>\n'+
                '</div>\n'+
            '</div>\n'
            }
            $("form #local_lan").html("").append(items)
        }else {
            items ="<div class='jumbotron' style='text-align:center'><h1 class='shabnam mid-font'>No local network found</h1>"
            $("#local_lan").html("").append(items)
        }
        }
    })


    }

  $('#add_local_range').on('click','button',add_device)
  
  function add_device(event){
      event.preventDefault();
      var allData = $("#add_local_range").serialize();
      $.ajax({
          url:"/add_local_range",
          method: "post",
          data: allData,
          success: function(response){
              if (response == 1){
                local_lan()
                  $("input").val("");
                }
              }
          
      })
      
  }

  $("div").on("click",".delete",delete_alert);
  function delete_alert(event){
      event.preventDefault();
      Swal.fire({
          title: '<span class="shabnam rtl_class big-font">Are you sure ?</span>',
          html: '<span " class="shabnam rtl_class">This action cannot be reverted.</span>',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          cancelButtonText: '<span class="shabnam rtl_class">Cansel</span>',
          confirmButtonText: '<span class="shabnam rtl_class">Yes, deleted.</span>'
          }).then((result) => {
          if (result.isConfirmed) {
              var id = $(this).attr("id");
              deletelocal(id);
              Swal.fire(
              '<span class="shabnam rtl_class">Your local network deleted successfully.</span>',
              '',
              'success'
              )
          }
          })
  }

  function deletelocal(id){
      
      $.ajax({
          url:"/delete_local_range",
          method: "post",
          data: {id : id},
          success: function(response){
              local_lan();
          }
      })
  }

$("form #local_lan").on("click",".modify",modify);
function modify(event) {
  event.preventDefault()
    if(!$(this).hasClass("active")){
      $(this).parent().siblings().children().children(".editable").each(function(){
        $(this).removeAttr("disabled")
       
    });
    $(this).addClass("active");
    $(this).addClass("exec");
    $(this).toggleClass("btn-black btn-secondary")
    $(this).html("Apply")
}else if($(this).hasClass("exec")) {
    var ip = $(this).parent().siblings().children().children(".ip").val();
    var mask = $(this).parent().siblings().children().children(".mask").val();
    var id = $(this).parent().siblings().children().children(".mask").attr("data");
    $.ajax({
        url:"/update_local_range",
        method: "post",
        data: {
            id : id,
            ip : ip,
            mask : mask
        },
        success: function(response){
            if(response == "1"){
              local_lan()
            }
        }
    })
}
}


  
  var ipv4_address = $('.ip');
  ipv4_address.inputmask({
  alias: "ip",
  greedy: false 
  });
});


