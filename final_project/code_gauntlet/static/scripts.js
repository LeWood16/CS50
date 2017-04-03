$(document).ready(function(){  
    
   // initialize object used to get the game settings
   var userGame = {};

   // hide certain divs until they're needed
   $("#diff-main").css("display", "none");
   $("#question-main").css("display", "none");

   // shows difficulty div
   // pushes language selection to userGame object
   $(".lang-btn").click(function(){
      $("#diff-main").css("display", "block");
      userGame["language"] = this.id;
      console.log(userGame);
   });

   // shows questions div
   // pushes difficulty selection to userGame object
   $(".d").click(function(){
      $("#question-main").css("display", "block");
      userGame["difficulty"] = this.id;
      console.log(userGame);

   });

   // pushes difficulty selection to userGame object
   // TODO: start the countdown for the game :D
   $("#questions > button").click(function(){
      $("#question-main").css("display", "block");
      userGame["questions"] = this.id;
      console.log(userGame);
   });

/*

-user clicks a language button
   -function takes the div of the button user clicked
   -
*/



}); // end ready