$(window).load(function(){
       $("[data-toggle]").click(function() {
         var toggle_el = $(this).data("toggle");
         $(toggle_el).toggleClass("open-sidebar");
       });
        $(".swipe-area").swipe({
             swipeStatus:function(event, phase, direction, distance, duration, fingers)
                 {
                     if (phase=="move" && direction =="right") {
                          $(".container").addClass("open-sidebar");
                          return false;
                     }
                     if (phase=="move" && direction =="left") {
                          $(".container").removeClass("open-sidebar");
                          return false;
                     }
                 }
         });
         // Mostramos y ocultamos submenus
     	   $('.submenu').click(function(){
     		    $(this).children('.children').slideToggle();
     	    })

          //inicio de secion
          $(document).ready(function(){
       $('.log-btn').click(function(){
           $('.log-status').addClass('wrong-entry');
          $('.alert').fadeIn(500);
          setTimeout( "$('.alert').fadeOut(1500);",3000 );
       });
       $('.form-control').keypress(function(){
           $('.log-status').removeClass('wrong-entry');
       });

   });
     });
