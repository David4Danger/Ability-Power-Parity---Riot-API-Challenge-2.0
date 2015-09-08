$(document).ready(function() {
    $(".ind2").delay(600).each(function(index) {
        $(this).delay(400*index).fadeTo(600, 1);});})