(function ($) {
    "use strict";
    
    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#nav').addClass('nav-sticky');
        } else {
            $('#nav').removeClass('nav-sticky');
        }
    });
    
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 768) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Skills section
    $('.skills').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});
    

    // jQuery counterUp
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 1000
    });
    

    // Clients carousel
    $(".clients-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        responsive: { 0: {items: 2}, 768: {items: 4}, 900: {items: 6} }
    });
    

    // Testimonials carousel
    $(".testimonials-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        responsive: { 0: {items: 1}, 576: {items: 2}, 768: {items: 3}, 992: {items: 4} }
    });
  
})(jQuery);

//$("#dropdowns").change(function () {
//   var pid = $("input[name='user_selected']").val();
//   var fid = $("input[name='merchant']").val();
////  var pid = document.getElementById("delete_code").value;
//   if(pid === '' || pid === undefined){
//    Swal.fire({
//            title: 'Error',
//            text: "Please select a record.",
//            type: 'warning',
//            confirmButtonColor: '#3085d6',
//            confirmButtonText: 'OK',
//        });
//}
//   else{
//       $("#client_drop").attr('href', '/home/'+pid);
//    }
//
//});
function totalCalc() {
    var buy = document.getElementById("buy").value;
    var mrp = document.getElementById("mrp").value;
    var margin = mrp - buy;
    document.getElementById("margin").value = margin;
    }

//function totalMrp() {
//    var buy = document.getElementById("buy").value;
//    var margin = document.getElementById("margin").value;
//    var mrp = buy + margin;
//    document.getElementById("mrp").value = mrp;
//    }


