$(document).ready(function() {

    $('.sorapic2,.rumpic,.kenpic,.sorapic,.morgpic,.heimpic,.backbutton,.summtab,.morgicon,.dianaicon,.fizzicon,.ruminfo,.keninfo,.sorainfo,.morginfo,.heiminfo').hide()

    $('.rumble').click(function() {
    $('div.default h5').hide();
    $('.rumpic,.backbutton,.ruminfo').fadeIn('slow');
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').hide();});
    
    $('.kennen').click(function() {
    $('div.default h5').hide();
    $('.kenpic,.backbutton,.keninfo').fadeIn('slow');
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').hide();});
    
    $('.soraka').click(function() {
    $('div.default h5').hide();
    $('.sorapic,.backbutton,.sorainfo,.sorapic2').fadeIn('slow');
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').hide();});
    
    $('.morgana').click(function() {
    $('div.default h5').hide();
    $('.morgpic,.backbutton,.morginfo').fadeIn('slow');
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').hide();});
    
    $('.heimerdinger').click(function() {
    $('div.default h5').hide();
    $('.heimpic,.backbutton,.heiminfo').fadeIn('slow');
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.dianaicon,.morgicon,.fizzicon').fadeIn('slow');
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.rumpic,.kenpic,.sorapic,.morgpic,.heimpic,.backbutton,.summtab,.morgicon,.dianaicon,.fizzicon,.ruminfo,.keninfo,.sorainfo,.morginfo,.heiminfo').hide()
    $('.rumble,.kennen,.morgana,.soraka,.heimerdinger,.summary').fadeIn('slow');});})