<!DOCTYPE html>
<html>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <title>Flat Design ChatBox</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    
</head>


<body>

    <div class="chatbox">
        <div id = "chatlogs" class="chatlogs">

        </div>
            <div class="chat-form">
                <textarea id="texto" name="texto"></textarea>
                <button id="submit">Send</button>
            </div>
    </div>

    <script type="text/javascript">
        $("#submit").click(function() {
            var texto = document.getElementById("texto").value;
            $("<div class='chat user'><div class='user-photo'><img src='img/bot.png'></div><p class='chat-message'>" + texto + "</p></div>").appendTo('.chatlogs');
            document.getElementById("texto").value = "";
            var element = document.getElementById("chatlogs");
            element.scrollTop = element.scrollHeight;
        });
    </script>
</body>
</html>