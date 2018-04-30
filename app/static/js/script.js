$('#list-group').empty()

$('#form').submit(function (e) {
    e.preventDefault()

    var text = $('#input').val()

    $('#list-group').empty()

    $.ajax({
        url: '/get',
        method: 'POST',
        datatype: 'json',
        data: {
            text: text,
            csrfmiddlewaretoken : getCookie('csrftoken')
        },
        success: function (response) {
            list(response)

            console.log(response)
        }
    })
})

items = { articles: [
            {
                title: 'Hello',
                abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation',
                keywords: ['keyword', 'hello', 'i don\'t know'],
                relevance: 0.72
            },
            {
                title: 'Hello2',
                abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation2',
                keywords: ['keyword', 'hello', 'i don\'t know'],
                relevance: 0.47
            },
            {
                title: 'Hello',
                abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation',
                keywords: ['keyword2', 'hello3', 'i don\'t know'],
                relevance: 0.37
            },
            {
                title: 'Hello',
                abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation',
                keywords: ['keyword', 'hello4', 'i don\'t know'],
                relevance: 0.24
            }
    ] }

list(items)

function list(items) {
    items.articles.forEach(function (item) {
        var html = '<a href="#" class="list-group-item list-group-item-action flex-column align-items-start">'
             +   '<div class="d-flex w-100 justify-content-between">'
             +     '<div>'
             +       '<h5 class="mb-1">' + item.title + '</h5>'
             +       '<p class="mb-1">' + item.abstract + '</p>'
             +       '<div class="row w-100 ml-1">'


        for (var i=0; i<Math.min(5, item.keywords.length); i++) {
            html +=    '<div class="col-auto rounded my-1 mr-2 key tag">'
             +           '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" style="margin-right: 1px;" width="13" height="12" viewBox="0 4 8 7">'
             +             '<path fill-rule="evenodd" fill="purple" d="M4 4H3v3H0v1h3v3h1V8h3V7H4V4z"></path>'
             +           '</svg>'
             +           item.keywords[i].keyword
             +         '</div>'
        }

        html +=       '</div>'
             +      '</div>'
             +     '<div class="mt-2">'
             +       '<div class="c100 p' + item.relevance * 100 + ' small" style="margin-right: 0px;">'
             +         '<span>' + item.relevance * 100 + '%' + '</span>'
             +         '<div class="slice">'
             +           '<div class="bar"></div>'
             +           '<div class="fill"></div>'
             +         '</div>'
             +       '</div>'
             +     '</div>'
             +   '</div>'
             + '</a>'


        $('#list-group').append($(html))
    })
}