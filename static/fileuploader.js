$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        form_data.append('image', $('input[type=file]')[0].files[0]);
        $.ajax({
            type: 'POST',
            url: '/food',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
            },
        });
    $('#welcome').hide();
    $('#tag').hide();
    $('#upload-file').hide();
    });
});