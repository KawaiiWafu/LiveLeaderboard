# LiveLeaderboard
Simple tool for creating live leaderboards during speedrun races

## Server installation

The application was only tested on [pythonanywhere servers](https://www.pythonanywhere.com/user/Wafu/). It should work locally as well (you'd have to do some changes, more at [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/), but due to Flask and this application being very lightweight, I recommend running it there (at least you don't have to leak your public IP address). By default, the application uses [Spectre.css](https://picturepan2.github.io/spectre/) and [anime.js](https://animejs.com), both of these are fully optional, you can use whatever you want. These are, however, simple enough for anyone to be able to modify it and both are lightweight.

## Client installation

I recommend you to build the client with pyinstaller and distribute it to your runners, or they can use any of the [Releases](https://github.com/KawaiiWafu/LiveLeaderboard/releases). For this to work, runners need to install [LiveSplit.Server](https://github.com/LiveSplit/LiveSplit.Server) into their LiveSplit or use the development build of LiveSplit. The server needs to be added in Layout and must be started via Control -> Start Server, then the client app can be started. The application sends a request to the server everytime the client reaches next split. This means all runners must use the same splits for this to be fair.

## How to improve accuracy?

* Autosplitters — Games with autosplitters allow more accuracy as every runner usually has the same amount of splits and human error is avoided
* More splits — If you can afford splitting more often (e.g. on every checkpoint (Outlast), every door (Devil May Cry 4: Special Edition)), the difference between runners will be updated more often, resulting in more accurate leaderboard

## The code is a mess

Yes. There's things that should be done differently and it needs more documentation. Feel free to contribute.

## License

All of my code in this repository is public domain. This doesn't apply to Spectre.css and anime.js, those use MIT license.
