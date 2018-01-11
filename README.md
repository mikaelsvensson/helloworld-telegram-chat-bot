# Telegram bot

## Preparation

You will need this:

* Application for editing Python code. Basically any text editor will do but [PyCharm](https://www.jetbrains.com/pycharm/) 
  is a really good one (the community edition is also free).
* Telegram account. Sign up for free on [telegram.org](https://telegram.org/).
* Heroku account. Sign up for free on [heroku.com](https://signup.heroku.com/dc). We use Heroku to deploy our bot so 
  that Telegram can find it.
* The Heroku CLI (a tool for deploying applications to Heroku)
* The Heroku Builds plugin for the Heroku CLI

**How to install Heroku CLI and Heroku Builds:**

First, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

Second, install the Heroku Builds plugin for the Heroku CLI (we use this to upload our applications to Heroku):

```
heroku plugins:install heroku-builds
```

## Step By Step

### Tell Telegram you want to create a bot

Sign in to Telegram and do this:
- Find the bot BotFather in Telegram by searching for it.
- Click on BotFather and start chatting with "him" by clicking the Start button at the bottom of the chat window (or 
  by sending him the message `/newbot`).
- Answer BotFather's questions.
- After a couple of questions you will get a message starting with "Done! Congratulations...". This message will contain 
  your API key (shown in red). The API key is the password of your bot. 
- Save the API key in a text file on your computer, for later use.

### Get the source code

[Download the Hello World bot source code](https://github.com/mikaelsvensson/helloworld-telegram-chat-bot/archive/master.zip) 
and extract it to a new folder.

### Create the app in Heroku

Open a terminal window.

Go to the folder when you extracted the source code. On a Mac, you _probably_ can do this by entering this command into
the terminal: `cd Downloads/helloworld-telegram-chat-bot-master`

You must now create an "application" in Heroku. This application must have a name. The name of your 
application in Heroku does not have to match the name of your bot in Telegram, but it is convenient. In the commands 
below, replace _NAME_OF_YOUR_HEROKU_APPLICATION_ with the name you want. Think of this as Heroku's name for your bot. 

Run this command (the command may ask you for your Heroku username and password):
```
heroku apps:create NAME_OF_YOUR_HEROKU_APPLICATION
```

The `heroku apps:create` command shows an error about "tar" not being installed on some computers. You can safely ignore that error.
 
Make your API key, sent to you by BotFather, available to your Heroku application by entering this command in your terminal:

```
heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key --app NAME_OF_YOUR_HEROKU_APPLICATION
```

### Get it working

Open `init_webhook.py`, in the folder `app`, and set the `HOST_NAME` constant to the app's address. Skip the `/` at the end. 
It should look something like this: `HOST_NAME = 'https://NAME_OF_YOUR_HEROKU_APPLICATION.herokuapp.com'`

Deploy to Heroku using these commands:

```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku ps:scale web=1 --app NAME_OF_YOUR_HEROKU_APPLICATION
```

Within a minute or so, you should now be able to find your bot in Telegram by searching for it using the name you 
sent to BotFather earlier. 

Start chatting with your new bot. Does it send back everything you send it? Good.

**You now have a fully functional bot! Congratulations!**

## Next steps

In `app/views.py` there is a function called `process_text`. Use that to change the text and make the bot smarter.

If you want something to get you started you can try these [ideas on chat bots](./bot-ideas.md).

Run this command after you change something, otherwise the bot will not see your changes: 

```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
```

## A Closer Look

Want to know more about Telegram bots? Check out <https://core.telegram.org/bots>.

More reading about Heroku:

- Heroku Architecture: <https://devcenter.heroku.com/categories/heroku-architecture>
- Python on Heroku: <https://devcenter.heroku.com/articles/getting-started-with-python>
- Heroku CLI cheat sheet: <http://ricostacruz.com/cheatsheets/heroku.html>
- Heroku CLI usage: <https://devcenter.heroku.com/articles/using-the-cli>

We're using Flask, a web service library for Python, and a lot of information about it can be 
found on <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>.

## Troubleshooting

Ask yourself this if you have problems:

* Have you saved your changes?
* Have you uploaded your saved changes to Heroku using `heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION`?
* Have you written the correct URL or hostname?
* Have you confused your Heroku application name with your Telegram bot name?
* Are you working in the correct folder?
* Have you accidentally mixed up small and big letters? "Heroku" and "heroku" is not the same thing when typing 
  a command in the terminal.  
