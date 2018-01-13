# Telegram-bot

## Förberedelser

Du behöver det här:

* Program för att redigera Python-kod. I princip vilket textredigerare som helst duger men 
  [PyCharm](https://www.jetbrains.com/pycharm/) är en väldigt bra (Community Edition är dessutom gratis).
* Telegram-konto. Skapa ett gratis på [telegram.org](https://telegram.org/).
* Heroku-konto. Skapa ett gratis på [heroku.com](https://signup.heroku.com/dc). Vi använder Heroku för att göra vår bot 
  tillgänglig för Telegram i form av en Heroku-applikation.
* Verktyget "Heroku CLI" (det är ett verktyg för att ladda upp Heroku-applikationer)
* Tillägget "Heroku Builds" för "Heroku CLI".

**Så här installerar du Heroku CLI och Heroku Builds:**

Först, [installera Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

Därefter, installera tillägget Heroku Builds för Heroku CLI (används för att ladda upp applikationer till Heroku):

```
heroku plugins:install heroku-builds
```

## Steg för steg

### Berätta för Telegram att du vill göra en bot

Logga in i Telegram och gör så här:
- Hitta boten BotFather i Telegram genom att söka efter "honom".
- Klicka på BotFather och börja chatta genom att klicka på Start-knappen i nederkanten av chattfönstret (eller skicka 
  meddelandet `/newbot` till honom).
- Svara på frågorna från BotFather. Svårt att komma på ett bra namn till din bot? Chatta med boten 
  [hellobotnamebot](t.me/hellobotnamebot) för att få förslag.
- Efter ett par frågor får du ett meddelande som börjar med "Done! Congratulations...". Det meddelandet kommer innehålla 
  en "API key" (i rött). En "API key" är lösenordet som din bot måste ha för att kunna svara på meddelanden. 
- Spara API-nyckeln i en textfil på datorn, så att du kan använda den lite senare.

### Hämta källkoden

[Ladda ner källkoden till vår Hello World-bot](https://github.com/mikaelsvensson/helloworld-telegram-chat-bot/archive/master.zip) 
och packa upp till en mapp på din dator.

### Skapa en applikation i Heroku

Öppna ett terminal-fönster (även kallat Kommandoprompt).

Gå till mappen där du packade upp källkoden. På en Mac så kan du _troligtvis_ göra detta genom att köra det här kommandot 
i terminalen: `cd Downloads/helloworld-telegram-chat-bot-master`

Du måste nu skapa en "applikation" i Herou. Den måste ha ett namn. Namnet måste inte vara samma som du valt för din 
Telegram-bot, men det är praktiskt om det är samma. I kommandona härefter så ska du ersätta 
_NAME_OF_YOUR_HEROKU_APPLICATION_ med namnet du vill ha. Det här är lite som Herokus egna namn på din bot. 

Kör det här kommandot (kommandet kommer eventuellt fråga efter ditt Heroku-användarnamn och lösenord):
```
heroku apps:create NAME_OF_YOUR_HEROKU_APPLICATION
```

Kommandot `heroku apps:create` visar ibland en varning om att "tar" inte är installerat. Du kan lugnt strunta i den varningen.
 
Gör nu din API-nyckel, den du fick från BotFather, tillgänglig för din Heroku-applikation genom att göra det här 
kommandot i din terminal:

```
heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key --app NAME_OF_YOUR_HEROKU_APPLICATION
```

### Få det att fungera

Öppna `init_webhook.py`, i mappen `app`, och sätt konstanten `HOST_NAME` till din Heroku-applikations adress. 
Hoppa över `/` på slutet. Det borde se ut ungefär så här: `HOST_NAME = 'https://NAME_OF_YOUR_HEROKU_APPLICATION.herokuapp.com'`

Ladda nu upp din bot till Heroku genom att köra de här kommandona:

```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku ps:scale web=1 --app NAME_OF_YOUR_HEROKU_APPLICATION
```
Snart, inom en minut eller så, kommer du kunna hitta din bot i Telegram genom att sök efter den i Telegram.

Börja chatta med din bot. Skickar den tillbaka vad du sänder till den? Bra.

**Du har nu en fullt fungerade bot! Grattis!**

## Nästa steg

I `app/views.py` finns en funktion som heter `process_text`. Använd den för att ändra vad din bot svarar på meddelanden.

Om du vill ha förslag på hur du kan göra din bot bättre så har vi ett par [chatbot-idéer](./bot-ideas.md).

Kör det här kommandot efter att du ändrat något, annars kommer din bot inte att se dina ändringar:

```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
```

## En närmare titt

Vill du veta mer om Telegram-bottar? Kolla in <https://core.telegram.org/bots>.

Mer om Heroku:

- Heroku Architecture: <https://devcenter.heroku.com/categories/heroku-architecture>
- Python on Heroku: <https://devcenter.heroku.com/articles/getting-started-with-python>
- Heroku CLI cheat sheet: <http://ricostacruz.com/cheatsheets/heroku.html>
- Heroku CLI usage: <https://devcenter.heroku.com/articles/using-the-cli>

Vi använder Flask, ett Python-bibliotek för att göra webbtjänster, och mycket information om detta 
hittar du på <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>.

## Felsökning

Fråga dig själv detta om du har problem:

* Har du sparat dina ändringar?
* Har du laddat upp dina ändringar till Heroku med `heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION`?
* Har du skrivit rätt URL eller servernamn?
* Har du blandat ihop Heroku-namnet med Telegram-namnet på din bot?
* Är du rätt mapp på datorn?
* Har du av misstag blandat ihop stora och små bokstäver? "Heroku" och "heroku" är inte samma sak när det knappas in i ett terminalfönster.
