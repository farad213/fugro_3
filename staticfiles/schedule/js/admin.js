function addBubblesToIcons(){
    $('.icons > div').hover(function() {
  if (this.classList.contains('true')) {
    // Get the value of the data-bubble attribute and parse it into a JavaScript array
    const bubbleList = JSON.parse($(this).data('bubble').replace(/'/g, '"'));

    // Create an empty bubble element
    const bubble = $('<div>').addClass('bubble');
    // Loop through the array and create a new <div> element for each item
    for (let i = 0; i < bubbleList.length; i++) {
      const bubbleItem = $('<div>').text(bubbleList[i]);
      // Append the bubbleItem to the bubble
      bubble.append(bubbleItem);
    }
    // Append the bubble to the icon
    $(this).append(bubble);
  }
}, function() {
  // Remove the bubble when the mouse leaves the icon
  $(this).find('.bubble').remove();
});
}


$( document ).ready(function() {

function isMobile() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

 $('.icons > div').on('click', function(event) {
if (isMobile()) {
event.preventDefault();
}
});


 $('.ppl-image-green, .ppl-image').on('click', function(event) {
if (isMobile()) {
event.preventDefault();
}
});



addBubblesToIcons();

  var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!

today = mm + '/' + dd;

$('.day .date').each(function() {
    console.log(today, $(this).text())
    if ($(this).text() === today) {
        $(this).closest('.day').attr('id', 'today');
    }
});

 $(".toggle-days-displayed input[name='toggle-days-displayed']").click(function() {
        if ($(this).val() === "5 nap") {
            $(".weekend, .Szombat-display, .Vasárnap-display").css("display", "none");
            $(".day_wrap, .weekdays div").css("margin", "10px 20px 10px 20px");
        } else {
            $(".weekend, .Szombat-display, .Vasárnap-display").css("display", "block");
            $(".day_wrap, .weekdays div").css("margin", "10px");
        }
    });

});

$(document).ready(function() {
  function updateWarning() {
    var start = $("#id_start").val();
    var end = $("#id_end").val();
    var url = $("#export").data("check-sit-url");

    $.ajax({
      url: url,
      data: {
        'start': start,
        'end': end,
      },
      success: function(response) {
        if (response.length === 0) {
          $("#check").show();
          $("#warning").hide();
        } else {
          // Update the data-bubble attribute with the new response
          $("#warning").show().attr('data-bubble', JSON.stringify(response));
          $("#check").hide();
        }
      }
    });
  }

  // Initial call to update the warning on page load
  updateWarning();

  // Add event listeners to update the warning when the input fields change
  $("#id_start, #id_end").on("change", function() {
    updateWarning();
  });

$('#warning').mouseover(function(e) {
  var bubbleList = JSON.parse($(this).attr('data-bubble'));
  var bubble = $('<div>').addClass('bubble');

  for (let i = 0; i < bubbleList.length; i++) {
    var bubbleItem = $('<div>').text(bubbleList[i]);
    bubble.append(bubbleItem);
  }
    console.log(bubbleList)
  $('body').append(bubble);

  const bubbleWidth = bubble.outerWidth();
  const bubbleHeight = bubble.outerHeight();
  const windowWidth = $(window).width();
  const windowHeight = $(window).height();
  const posX = e.pageX + 10;
  const posY = e.pageY + 10;

  if (posX + bubbleWidth > windowWidth) {
    bubble.css('left', e.pageX - bubbleWidth - 10);
  } else {
    bubble.css('left', posX);
  }

  if (posY + bubbleHeight > windowHeight) {
    bubble.css('top', e.pageY - bubbleHeight - 10);
  } else {
    bubble.css('top', posY);
  }
});

$('#warning').mouseout(function() {
  $('.bubble').remove();
});

$('.upper-row').each(function() {
  var freeEmployees = $(this).data('free-employees');
  if (freeEmployees.length === 0) {
    $(this).find('.ppl-image-green').addClass('no-display');
  } else {
    $(this).find('.ppl-image').addClass('no-display');
  }
});


$('.ppl-image-green').hover(function() {
// Get the value of the data-bubble attribute and parse it into a JavaScript array
const freeEmployeesStr = $(this).closest('.upper-row').data('free-employees');
const bubbleList = JSON.parse(freeEmployeesStr.replace(/'/g, '"'));

// Create an empty bubble element
const bubble = $('<div>').addClass('bubble');
// Loop through the array and create a new <div> element for each item
for (let i = 0; i < bubbleList.length; i++) {
  const bubbleItem = $('<div>').text(bubbleList[i]);
  // Append the bubbleItem to the bubble
  bubble.append(bubbleItem);
}
// Append the bubble to the icon
$(this).append(bubble);

}, function() {
// Remove the bubble when the mouse leaves the icon
$(this).find('.bubble').remove();
});


$(".user-selection input").each(function(){
   $(this).change(function(){

        var url = $(".user-selection").data("user-selection-url");
        var id = $(this).val();
        $.ajax({
          url: url,
          data: {
            "id": id
          },
          success: function(response) {
               if (id !== "Admin") {
                  $(".calendar").html(response);
                  $('.icons [data-bubble]').each(function() {
                      var bubbleData = $(this).data('bubble');
                      if (bubbleData.length === 0) {
                        $(this).addClass('false');
                      } else {
                        $(this).addClass('true');
                      }
                    });
                    addBubblesToIcons();
               } else {
                  window.location.href = response;
               }
          }
        });

   });
});

$(document).on('click', '.nav_buttons button', function(){
   var url = $(".nav_buttons").data("month-change-url");
   var direction = $(this).val();
   var year = $(".nav_buttons").data("year");
   var month = $(".nav_buttons").data("month");
   var id = $("input[name=user-selection]:checked").val();
   console.log(url, direction);
    $.ajax({
      url: url,
      data: {
        "direction": direction,
        "year": year,
        "month": month,
        "id": id
      },
      success: function(response) {
        var $response = $(response);
        var month = $response.find('.nav_buttons').data('month');
        var year = $response.find('.nav_buttons').data('year');
        $(".date_title").text("Admin - " + year + "." + month);

        $(".calendar").html(response);
      }
    });
});



});

