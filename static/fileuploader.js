$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file-form')[0]);
        $.ajax({
            type: 'POST',
            url: '/food',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                console.log(data);
                $('#upload_img').attr('src', data);
            },
        });
    $('#welcome-header').hide();
    $('#upload-file-header').hide();
    $('#upload-file-form').hide();
    });;
});