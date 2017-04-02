$(document).ready(function(){  

 $("#diff-main").css("display", "none");
 $("#question-main").css("display", "none");

 $("#test").click(function(){
    console.log("test");
    $("#tester").html("success");
  }); 
  
  


$("#lang-main").click(function(){
 $("#diff-main").css("display", "block");
})

$("#diff-main").click(function(){
 $("#question-main").css("display", "block");
})




}); // end ready