function Tracker(){

}
Tracker.prototype.click_links = function(selector, data){
    $('body').on('click', selector, function(e){
        e.preventDefault();
        data.location = window.location;
        var href = $(this).attr("href");
        $.ajax({
            url: "http://localhost:8000/track-links/",
            type: 'POST',
            data: data,
            success: function(response) {
            },
            complete: function(response){
                window.location.href = href;
            }
        });
    })
}
Tracker.prototype.click_elements = function(selector, data){
    $('body').on('click', selector, function(e){
        data.location = window.location.href;
        $.ajax({
            url: "http://localhost:8000/track-click/",
            type: 'POST',
            data: data
        });
    })
}