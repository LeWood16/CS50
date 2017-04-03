$(document).ready(function(){  
    
   var userGame = {};


   $("#diff-main").css("display", "none");
   $("#question-main").css("display", "none");


$(".lang-btn").click(function(){
 $("#diff-main").css("display", "block");
});

$(".d").click(function(){
 $("#question-main").css("display", "block");
});


$("nav > ul > button").click(function(){
   var category = this.parent().parent().id;
   userGame[category] = this.id;
   console.log("category:" + category);
   console.log("button id for value:" + this.id)
});

function userChoices(language, difficulty, questions){
    return {
        "language": language,
        "difficulty": difficulty,
        "questions": questions
    }
}


/*

-user clicks a language button
   -function takes the div of the button user clicked
   -







*/



}); // end ready