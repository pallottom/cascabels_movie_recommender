<!DOCTYPE html>

<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>{{title1}}</title>

    </head>
    <body>
        <ul>
            {%for f in films_var%}
              <li>{{f}}</li>
            {%endfor%}
    
        </ul>

    </body>

</html>