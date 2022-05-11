# Home Control

** This is a WIP, it's usable but it might have some flaws**

Control your appliances with your Raspberry PI via Telegram.

This application allow you to interact with your Raspberry PI GPIOs via a telegram bot.

## Available features
 - Telegram bot
 - Receive events via HTTP and notify via Telegram
 - Toggle switches using RPi GPIO via Telegram
 - Restrict who can send commands to the bot

## How to set up

First you need a working Raspberry PI, this software was tested in the following operating systems and boards:

 - Raspberry PI 1B (Raspberry PI OS Lite Bullseye 32-bit)
 - Raspberry PI Zero 2W (Raspberry PI OS Lite Bullseye 32-bit)
 - Raspberry PI 400 (Raspberry PI OS Bullseye 64-bit)

### 1 - Clone and install dependencies

Then `clone` this repository:

```sh
sudo apt install git
git clone https://github.com/brunofjesus/home_control.git
```

Enter the `home_control` directory and install the required dependencies:

```sh
cd home_control
sudo apt install python3-pip
pip install -r requirements.txt
```

### 2 - Environment configuration

 - Copy the `.env.example` file as `.env`:

```sh
cp .env.example .env
```

 - In the `.env` file change the value of `TOKEN` to your bot's token
 - In the `.env` file change the value of `ALLOWED_USERS` to your bot's token
 - Create the Telegram bot (https://core.telegram.org/bots)
 - Create a Telegram group and add your bot there
 - Get the `chat_id` for the Telegram group you just created
   - Send a message to the group using your account
   - Open the following link in the browser `https://api.telegram.org/bot**YOUR_BOT_TOKEN**/getUpdates`
   - In the response you should see a `.."chat":{"id":-XXXXXXXX,..`, copy the number (including the -) and put it in the `.env` file, like this:

     ```sh
	...
	CHAT_ID=-302000453
	...
     ```

### 3 - Actions configuration

 - Copy the `actions.toml.example` as `actions.toml`
 - Configure the desired actions

** The example action is something like this: **
```toml
[toggles]
[toggles.door]
type = "press_release"
duration = 1
pin = 11

[toggles.lamp]
type = "press"
pin = 15
```

** press_release **
The `press_release` type puts the specified `pin` on `HIGH` during the specified `duration` in seconds.
To trigger it call the command `/tg door` on the chat.

** press **
Makes the specified `pin` `HIGH` or `LOW` depending on input.

 - Turn on: `/tg lamp on`
 - Turn off: `/tg lamp off`

# 4 - Event notifications

To send notifications make a `POST` request to `http://<HOST>:<PORT>/event/<item>/<value>`

