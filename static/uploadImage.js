/* update Preview Image; local */
$(function () {
    const imgFile = document.getElementsByName("img-upload")[0];
        const previewImage = document.getElementById("image-preview");

        imgFile.addEventListener("change", function () {
            const img = this.files[0];

            if (img) {
                const reader = new FileReader();
                $('#image-preview-text').hide();
                previewImage.style.display = "block";

                reader.addEventListener("load", function() {
                    previewImage.setAttribute("src", this.result);
                });

                reader.readAsDataURL(img);
            } else {
                previewImage.style.display = "null";
            }
        })
});


/* send info to googleAPI */
$(function() {
    $('#upload-file-btn').click(function() {
        let form_data = new FormData($('#upload-file-form')[0]);
        $.ajax({
            type: 'POST',
            url: '/search-label',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                let img_data = JSON.parse(data);
                $('#upload-img').attr('src', img_data["uri"]);
                $('#upload-img').attr('alt', img_data["label"]);

                callRecipeApi(img_data["label"]);
            },
        });
    $('#welcome-header').hide();
    $('#upload-file-header').hide();
    $('#upload-file-form').hide();
    });;
});


function callRecipeApi(label) {
    console.log('in callREcipeAPI');
    console.log('the label is ' + label);
    setInterval(function() {
        $.ajax({
            success: function() {
                window.location.href = '/choose-recipe/'+label;
            }
        })
    }, 2000); //5 seconds
}