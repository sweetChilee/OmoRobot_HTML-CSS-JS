$(window).scroll((e) => {
  console.log($(window).scrollTop())

  if($(window).scrollTop() < 200) {
    $(".omobox").hide()
  } else if($(window).scrollTop() > 5600) {
    $(".omobox").fadeIn(1000)
  } 
});
