var t;
var d;

$(document).ready(function () {
    $('.t1d2Lx').hide();
    $('.t1d2Qz').hide();
    $('.t1d2Lz').hide();
    $('.t1d3Lz').hide();
    $('.t1d3Qy').hide();
    $('.t1d3Qz').hide();
    $('.t2point').hide();
})

$("#kinematicsType").change(function () {
    if ($(this).val() === "1") { // t is 1
        t = 1;
    } else {  // t is 2
        t = 2;
    }
});

$("#robotType").change(function () {
    if ($(this).val() === "1") { // t is 1
        d = 1;
    } else if ($(this).val() === "2") {  // t is 2
        d = 2;
    } else {
        d = 3;
    }
});

$("#kinematicsType").trigger("change");
$("#robotType").trigger("change");


$("#kinematicsType").bind("change", displayAptFields)
$("#robotType").bind("change", displayAptFields)

function displayAptFields() {
    if (t === 1 && d === 1) {
        $('.t1d1Lx').show();
        $('.t1d1Ly').show();
        $('.t1d1Lz').show();
        $('.t1d2Lx').hide();
        $('.t1d2Qz').hide();
        $('.t1d2Lz').hide();
        $('.t1d3Lz').hide();
        $('.t1d3Qy').hide();
        $('.t1d3Qz').hide();
        $('.t2point').hide();
    } else if (t === 1 && d === 2) {
        $('.t1d1Lx').hide();
        $('.t1d1Ly').hide();
        $('.t1d1Lz').hide();
        $('.t1d2Lx').show();
        $('.t1d2Qz').show();
        $('.t1d2Lz').show();
        $('.t1d3Lz').hide();
        $('.t1d3Qy').hide();
        $('.t1d3Qz').hide();
        $('.t2point').hide();
    } else if (t === 1 && d === 3) {
        $('.t1d1Lx').hide();
        $('.t1d1Ly').hide();
        $('.t1d1Lz').hide();
        $('.t1d2Lx').hide();
        $('.t1d2Qz').hide();
        $('.t1d2Lz').hide();
        $('.t1d3Lz').show();
        $('.t1d3Qy').show();
        $('.t1d3Qz').show();
        $('.t2point').hide();
    } else if (t === 2) {
        $('.t2point').show();
        $('.t1d1Lx').hide();
        $('.t1d1Ly').hide();
        $('.t1d1Lz').hide();
        $('.t1d2Lx').hide();
        $('.t1d2Qz').hide();
        $('.t1d2Lz').hide();
        $('.t1d3Lz').hide();
        $('.t1d3Qy').hide();
        $('.t1d3Qz').hide();
    }
}