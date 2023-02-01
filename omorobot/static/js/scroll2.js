$(window).scroll((e) => {
  console.log($(window).scrollTop())

  if($(window).scrollTop() < 200) {
    $(".explain_a_1").hide()
  } else if($(window).scrollTop() > 3100) {
    $(".explain_a_1").fadeIn(1500)
  } 
});
