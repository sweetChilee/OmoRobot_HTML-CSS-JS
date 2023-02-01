$(window).scroll((e) => {
  console.log($(window).scrollTop())

  if($(window).scrollTop() < 200 ) {
    $(".explain_a").hide()
  } else if($(window).scrollTop() > 2000 ) {
    $(".explain_a").fadeIn(1500)
  } 
});
