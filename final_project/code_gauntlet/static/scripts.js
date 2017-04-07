$(document).ready(function(){  
    
   // initialize object used to get the game settings
   var userGame = {};

   // shows difficulty div
   // hide language div
   // pushes language selection to userGame object
   $(".lang-btn").click(function(){
      $("#diff-main").removeClass("hidden");
      $("#lang-main").addClass("hidden");
      userGame["language"] = this.id;
      console.log(userGame);
   });

   // shows questions div
   // hide difficulty div
   // pushes difficulty selection to userGame object
   $(".d").click(function(){
      $("#question-main").removeClass("hidden");
      $("#diff-main").addClass("hidden");
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

- index page logs which language the user chose;
- based on that, when the user clicks the number of questions, they are 
  redirected to the appropriate language test page
  
- four different pages made, each hiding and showing questions and answers, and 
  managing state by keeping track of the user's score;
  
- at the end of the questions, user will be shown their score, as well as a link
  back to the index page, so they can play again;
*/



}); // end ready