<!DOCTYPE html>
<html>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <title>UFMG Atendimento</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    
</head>

<body>
    <div class="chatbox">
        <div id = "chatlogs" class="chatlogs">


        <div class="chat bot">
            <div class="user-photo"><img src="img/user.png"></div>
            <p class="chat-message arrow_box_bot">Seja bem vindo ao Atendimento Virtual UFMG. Aqui você pode tirar dúvidas relacionadas ao NIPs, conexão com a Internet e inconsistências no Moodle. Com o que posso ajudar?</p>
        </div>
        </div>
        <div class="chat-form">
            <textarea id="texto"  placeholder="Escreva alguma coisa..."  onKeyUp="verificaEnter(this, event)" name="texto"></textarea>
            <button id="submit">Send</button>
        </div>
    </div>

<!-- Script que controla as mensagens do chat -->
    <script type="text/javascript">

    function verificaEnter(t,e){
        if (e.keyCode === 13)
            document.getElementById("submit").click();
    }
        $("#submit").click(function() {
            var texto = document.getElementById("texto").value;
            if (texto){
                $("<div class='chat user'><div class='user-photo'><img src='img/bot.png'></div><p class='chat-message arrow_box'>" + texto + "</p></div>").appendTo('.chatlogs');
                document.getElementById("texto").value = "";
                var element = document.getElementById("chatlogs");
                element.scrollTop = element.scrollHeight;

                 $("<div class='chat bot'><div class='user-photo'><img src='img/bot.png'></div><p class='chat-message arrow_box_bot'> Chat Message</p></div>").appendTo('.chatlogs');
            }
        });
    </script>
</body>
</html>