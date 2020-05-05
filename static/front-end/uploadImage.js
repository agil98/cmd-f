/* update Preview Image; local */
$(function () {
    const imgFile = document.getElementsByName("local-img-file")[0];
        const previewImage = document.getElementById("image-preview-img");

        imgFile.addEventListener("change", function () {
            const img = this.files[0];

            $('#img_url')[0].value = img.name.toString();
            $('#img_url')[0].disabled = true;

            if (img) {
                const reader = new FileReader();
                // $('.website-title').opacity = "0.2"; //animate?

                reader.addEventListener("load", function() {
                    previewImage.setAttribute("src", this.result);
                });

                reader.readAsDataURL(img);
                searchRecipe();
            } else {
                previewImage.style.display = "null";
            }
        })
});


/* if link is entered */
//     document.addEventListener('keydown', function (e) {
//         console.log("??");
//         if (e.keyCode == 13) {
//             e.preventDefault();
//             alert("success");
//             return searchRecipe();
//         }
//     })
document.onkeydown = function(event){
    event = event || window.event;
    let e = event.keyCode;
    if (e == 13){
        event.preventDefault();
        searchRecipe();
    }
};


/* send info to googleAPI */
function searchRecipe() {
    let form_data = new FormData($('.upload-file-form')[0]);
    $.ajax({
        type: 'POST',
        url: '/search-label',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            console.log(data);
            let img_data = JSON.parse(data);
            $('#image-preview-img').attr('src', img_data["uri"]);
            $('#image-preview-img').attr('alt', img_data["label"]);

            callRecipeApi(img_data["uri"],img_data["label"]);
            // callRecipeApi(img_data["label"]);
        },
    });
}

function callRecipeApi(uri, label) {
    document.body.style.cursor = "progress"; //"wait";
    setInterval(function() {
        $.ajax({
            success: function() {
                // window.location.href = '/choose-recipe/'+label+'/'+uri;
                //                 window.location.href = '/choose-recipe/?='+uri;
                window.location.href = '/choose-recipe/'+label;
            }
        })
    }, 1500);
}