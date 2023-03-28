$(document).ready(function() {
    $("#extra-select").select2();

    var select_url = $("#ajax-select-wrapper").data("select-url");
    var szamol_url = $("#calculate").data("calculate-url");

    $("#sorszam").keyup(function(){
        var sorszam = $("#sorszam").val();
         $.ajax({
            url: select_url,
            data: {"sorszam": sorszam},
            success: function(data) {
                $("#extra-select").html(data)
            }
          });

    });

    $("#calculate").click(function(){
        var sorszam = $("#sorszam").val();
        var select = $("#extra-select").val();

        $.ajax({
            url: szamol_url,
            data: {"sorszam": sorszam, "select": select},
            success: function(data) {
                $("#result").html(data)
            }
          });
    });


});