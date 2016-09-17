function Tracker(){

}
Tracker.prototype.click_links = function(selector, data){
    $('body').on('click', selector, function(e){
        e.preventDefault();
        data.url = window.location;
        var href = $(this).attr("href");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function(response) {
                window.location.href = href;
            }
        });
    })
}
Tracker.prototype.click_elements = function(selector, data){
    data.url = window.location;
    $('body').on('click', selector, function(e){
        $.ajax({
            url: 'track-click/',
            type: 'POST',
            data: data,
            dataType: 'json'
        });
    })
}