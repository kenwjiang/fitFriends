$(document).ready(function(){

  // click to hide login and register forms
  $('#reg-logo').click(function(){
    $('#register-form').show(500);
    $('#login-form').hide(500);
  });

  $('#login-logo').click(function(){
    $('#register-form').hide(500);
    $('#login-form').show(500);
  });
 //  // registration validator
 //  $('#reg-email').keyup(function(){
 //    $.ajax({
 //      async: true,
 //      type: 'POST',
 //      url: '/login/create',
 //      beforeSend: function (request)
 //                   {
 //                       request.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); //this adds the CSRF token in the ajax call
 //                    },
 //
 //      data: $('reg-email').val(),
 //      dataType: 'json',
 //      success: function(data) {
 //        if (data.status == 'ok') {
 //          $('#register-errors').html(data.html);
 //        }
 //      },
 //      complete: function(){
 //      },
 //      error: function(xMLHttpRequest, textStatus, errorThrown){
 //        alert('server error')
 //      }
 //    });
 //  });
 // })
 //  end of document ready
});
