$(document).ready(function(){
    
    // Waiting JS
    $body = $("body");
    $(document).on({
        ajaxStart: function() {$body.addClass("loading");    },
         ajaxStop: function() { $body.removeClass("loading"); }    
    });
    var ipv4_address = $('.ip');
    ipv4_address.inputmask({
    alias: "ip",
    greedy: false //The initial mask shown will be "" instead of "-____".
    });


});