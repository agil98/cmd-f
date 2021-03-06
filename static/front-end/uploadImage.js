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
            if (JSON.parse(data)["label"] === "not food") {
                alert("This is not Food :(, please re-upload!");
                $('#img_url')[0].disabled = false;
                $('#img_url')[0].value = "";
                setTimeout(function(){
                    // window.location.reload();
                },1250);
            } else {
                callRecipeApi(data);
            }
        },
    });
}

function callRecipeApi(data) {
    document.body.style.cursor = "wait"; //"progress";
    setTimeout(function(){
        $.ajax({
            type: 'POST',
            url: '/choose-recipe',
            data: data,
            contentType: 'application/json',
            dataType:'json',
            cache: false,
            processData: false,
            success: function (response) {
                document.write(response);
            },
        });
    }, 2);
}