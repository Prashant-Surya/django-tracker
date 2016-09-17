function Tracker(){

}
Tracker.prototype.click_links = function(selector, data){
    $('body').on('click', selector, function(e){
        var href = $(this).attr("href")
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
    $('body').on('click', selector, function(e){
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json'
        });
    })
}