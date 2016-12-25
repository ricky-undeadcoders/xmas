$(document).ready( function () {
    $('#profile_picture').change(function () {
        var filename = $('#profile_picture').val().match(/[-_\w]+[.][\w]+$/i)[0];
        $('#upload-text').text(filename);
    });
});