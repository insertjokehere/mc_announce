A really simple docker container to announce one or more Minecraft games on your LAN

The Linux version of the standalone Minecraft server doesn't do this by default for some reason.

## Usage

This container looks for environment variables that start with `MCSERVER_`. Everything after the underscore is assumed to be the port number the server is listening on, and the content of the variable is the server description. For example, to announce two servers called 'Test Server 1' and 'Test Server 2', running on ports 25565 and 25566 respectively:

`docker run -d --net=host -e MCSERVER_25565="Test Server 1" -e MCSERVER_25566="Test Server 2" mc_announce`

Note the `--net=host`, which is required for the broadcast packets can make it to the right place.

Based off the script provided in [this StackOverflow answer](http://gaming.stackexchange.com/a/238680)
