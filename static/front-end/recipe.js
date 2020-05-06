// https://3dtransforms.desandro.com/card-flip
$(document).on("click",".recipe-card", function () {
    $(this)[0].classList.toggle('is-flipped');
});


$(document).on("click",".keyword-toolbar", function () {
    alert("Coming Soon!");
});


$(document).on("click","#load-more-container", function () {
    let hiddenCounts = $('.recipe-card:hidden').length;
    let maxCounts = hiddenCounts > 3 ? 3 : hiddenCounts;
    for (let i = 0; i < maxCounts; i++) {
        $($('.recipe-card:hidden')[0]).parent().show();
    }

    if (hiddenCounts-maxCounts === 0) {
        $("#load-more-container").hide();
    }
});



function hideUnnecessaryRecipes() {
    console.log("hello");
        let visibleCards = $('.recipe-card:visible');
        let recipeCount = visibleCards.length;
        if (recipeCount > 3) {
            for (let i = 3; i < recipeCount; i++) {
                console.log($(visibleCards[i]).parent());
                $(visibleCards[i]).parent().hide();
            }
        }
}


// window.addEventListener("load",function() {
// });
//
// $(function () {
//     const card = document.getElementsByClassName("recipe-card")[0];
//         alert("aloha");
//
//
//     let visibleCards = $('.recipe-card');
//     alert("1");
//         let recipeCount = visibleCards.length;
//         alert(" 2");
//         console.log(recipeCount);
//         document.addEventListener("DOMContentLoaded", function(event) {
//            console.log("DOM fully loaded and parsed");
//         });
//         if (recipeCount > 3) {
//             alert(" 3");
//             for (let i = 3; i < recipeCount; i++) {
//                 console.log($(visibleCards[i]).parent());
//                 $(visibleCards[i]).parent().hide();
//             }
//         }
// });