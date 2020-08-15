## Network Programming (in `python`)

Networking scripts that gives a good introduction to network programming in python. Open a pull request to contribute other similar scripts :)

*in development:* Add command line input for scripts

### Descriptions

1. **Mailing Client** <br>
Simple mailing client in python to send emails over smtp server with file/photos attachments.

2. **TCP Chat** <br>
A very basic local tcp chat. Use `server.py` to setup monitoring server for the chat, and `client.py` for different users to connect to the chat.<br>
    
    **Server thread**
    ```
    > server.py
      Server is listining...
      Connected with ('127.0.0.1', 64303)
      Nickname of client is vader!
      Connected with ('127.0.0.1', 64335)
      Nickname of client is johndoe!
    ```
    **New Client thread(s)**
    ```
    > client.py
      Choose a nickname: johndoe
      johndoe joined the chat!
      Connected to the server!
      vader: hey john 
    ```
   **Already Client thread(s)**
    ```
    > client.py
      Choose a nickname: vader
      vader joined the chat!
      Connected to the server!
      .
      .
      johndoe joined the chat!
      hey john
      vader: hey john
    ```

3. **DDOS** <br>
A very inefficient ddos script (for educational purposes only!)

4. **Port Scanner** <br>
A general purpose port scanner (use authorized ip for port scanning, port-scanning is considered ill-legal)