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


/* get image */
$(function() {
    $('#upload-file-btn').click(function() {
        let form_data = new FormData($('#upload-file-form')[0]);
        console.log(form_data);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                console.log(data);
                $('#upload-img').attr('src', data);
            },
        });
    $('#welcome-header').hide();
    $('#upload-file-header').hide();
    $('#upload-file-form').hide();
    });;
});



// TODO: send info to googleAPI
