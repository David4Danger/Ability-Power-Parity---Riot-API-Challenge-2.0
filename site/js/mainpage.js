$(document).ready(function() {
    $(".ind2").delay(1000).each(function(index) {
        $(this).delay(400*index).fadeTo(200, 1);});})