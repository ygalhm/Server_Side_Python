$(document).ready(function () {
    $('#getrss').bind('click', display);
    $('#getrss').bind('click', cookieOk);
    $('#refresh').bind('click', refreshPage);
});

cookieOk = function () {
    $('#cookies').empty()
    $.ajax({
        type: "GET",
        url: "http://localhost:7001/cookie",
        success: function (cookie) {
                var new_div = $('<div>');
                new_div.text(cookie)
                $('#cookies').append(new_div);
        },
        error: function (new_list) {
            console.log("error");
        },
    });
}

refreshPage = function () {
    $('#cookies').empty()
    $('#feed').empty()
    display()
}

display = function () {
    $('#feed').empty()
    $.ajax({
        type: "GET",
        dataType: "JSON",
        url: "http://localhost:7001/rss",
        success: function (new_list) {
            for (var i = 0; i < new_list.length; i++) {
                var new_pre = $('<pre/>')
                var new_element = $('<a>');
                new_element.text(new_list[i].title)
                new_element.attr('href', new_list[i].link)
                new_pre.append(new_element)
                $('#feed').append(new_pre);
            }
        },
        error: function (new_list) {
            console.log("error");
        },
    });
}