<div class="markdown prose w-full break-words dark:prose-invert light"><h1>Zoomrec Transcribe and Summarize</h1><p>This repository is a fork that enhances the functionality of the original repository by adding the ability to transcribe and use LeMUR. The code has been modified to run on a specific version of Zoom that the original repository does not support, as the version used in the original was causing the code to fail. Please note that this version is also not the newest version of Zoom, as the newest version also causes the code to fail.</p><p>Additionally, this code is designed to run on AMD64 architecture. If your computer is not compatible, consider running this on a virtual machine (VM). It will not run if your computer is using ARM64.</p><h2>Steps to Run this Repository</h2><p>Follow these steps to set up and run this repository:</p><ol><li><p><strong>Clone the Repository:</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git <span class="hljs-built_in">clone</span> https://github.com/your_username/zoomrec-transcribe-and-summarize.git
</code></div></div></pre></li><li><p><strong>Navigate to the Repository:</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash"><span class="hljs-built_in">cd</span> zoomrec-transcribe-and-summarize
</code></div></div></pre></li><li><p><strong>Build with Docker:</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker build -t zoomrec-transcribe-and-summarize:tag .
</code></div></div></pre></li><li><p><strong>Create a .env File:</strong>
Add your AssemblyAI key to a .env file:</p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash"><span class="hljs-built_in">echo</span> <span class="hljs-string">"AAI_KEY=your_actual_api_key"</span> &gt; .<span class="hljs-built_in">env</span>
</code></div></div></pre></li><li><p><strong>Set Up a Virtual Environment:</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python3 -m venv venv
<span class="hljs-built_in">source</span> venv/bin/activate
pip install -r res/requirements.txt
</code></div></div></pre></li><li><p><strong>Create Folders and Set Permissions (on Host):</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash"><span class="hljs-built_in">mkdir</span> -p recordings/screenshots
<span class="hljs-built_in">chown</span> -R 1000:1000 recordings

<span class="hljs-built_in">mkdir</span> -p audio
<span class="hljs-built_in">chown</span> -R 1000:1000 audio
</code></div></div></pre></li><li><p><strong>Modify the meetings.csv File:</strong>
Update the <code>example/meetings.csv</code> file with your meeting data. Refer to the original readme below for more information. Remember to restart the Docker container whenever you change the <code>meetings.csv</code> file.</p></li><li><p><strong>Run Docker:</strong>
Replace <code>your_tz</code> with your own timezone in the command below:</p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker run -d --restart unless-stopped -e DISPLAY_NAME=<span class="hljs-string">"zoomrec"</span> \
  -e TZ=your_tz \
  -v $(<span class="hljs-built_in">pwd</span>)/recordings:/home/zoomrec/recordings \
  -v $(<span class="hljs-built_in">pwd</span>)/example/audio:/home/zoomrec/audio \
  -v $(<span class="hljs-built_in">pwd</span>)/example/meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
  zoomrec-transcribe-and-summarize:tag
</code></div></div></pre></li><li><p><strong>Separate Steps for Post-Meeting Processing:</strong></p><p>a. <strong>Transcribe the Recorded File:</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python transcribe.py
</code></div></div></pre><p>b. <strong>Run LeMUR:</strong></p><pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python run_lemur.py
</code></div></div></pre></li></ol><p>Please read the original readme below for more information.</p><hr></div>

<h1 align="center">
    zoomrec	
</h1>

<h4 align="center">
	A all-in-one solution to automatically join and record Zoom meetings.
</h4>

<p align="center">
	<a href="https://github.com/kastldratza/zoomrec/actions/workflows/docker-publish.yml"><img src="https://github.com/kastldratza/zoomrec/actions/workflows/docker-publish.yml/badge.svg" alt="GitHub Workflow Status"></a>
	<a href="https://github.com/kastldratza/zoomrec/actions/workflows/codeql-analysis.yml"><img src="https://github.com/kastldratza/zoomrec/actions/workflows/codeql-analysis.yml/badge.svg" alt="GitHub Workflow Status"></a>
	<a href="https://github.com/kastldratza/zoomrec/actions/workflows/snyk.yml"><img src="https://github.com/kastldratza/zoomrec/actions/workflows/snyk.yml/badge.svg" alt="GitHub Workflow Status"></a>
	<a href="https://github.com/kastldratza/zoomrec/actions/workflows/snyk-container-analysis.yml"><img src="https://github.com/kastldratza/zoomrec/actions/workflows/snyk-container-analysis.yml/badge.svg" alt="GitHub Workflow Status"></a>
    <br>
    <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/kastldratza/zoomrec">
    <img alt="Docker Image Size (tag)" src="https://img.shields.io/docker/image-size/kastldratza/zoomrec/latest">
    <img alt="Github Stars" src="https://img.shields.io/github/stars/kastldratza/zoomrec.svg">
</p>

---

- **Python3** - _Script to automatically join Zoom meetings and control FFmpeg_
- **FFmpeg** - _Triggered by python script to start/stop screen recording_
- **Docker** - _Headless VNC Container based on Ubuntu 20.04 with Xfce window manager and TigerVNC_
- **Telegram** - _Get notified about your recordings_

---

Join with ID and Passcode           |  Join with URL
:-------------------------:|:-------------------------:
![](doc/demo/join-meeting-id.gif)  |  ![](doc/demo/join-meeting-url.gif)

---

## Installation

The entire mechanism runs in a Docker container. So all you need to do is install Docker and use the image from
Registry.

### Requirements

- Docker - [https://docs.docker.com/get-docker/]()

### Docker Registry

Docker images are build and pushed automatically to [**Docker
Hub**](https://hub.docker.com/repository/docker/kastldratza/zoomrec) and [**GitHub Container
Registry**](https://github.com/kastldratza/zoomrec/pkgs/container/zoomrec).

So you can choose and use one of them:

- ```ghcr.io/kastldratza/zoomrec:master```
- ```kastldratza/zoomrec:latest```

*For my examples in this README I used* ```kastldratza/zoomrec:latest```

---

## Usage

- Container saves recordings at **/home/zoomrec/recordings**
- The current directory is used to mount **recordings**-Folder, but can be changed if needed
    - Please check use of paths on different operating systems!
    - Please check permissions for used directory!
- Container stops when Python script is terminated
- Zoomrec uses a CSV file with entries of Zoom meetings to record them
    - The csv can be passed as seen below (mount as volume or add to docker image)
- To "say" something after joining a meeting:
    - ***paplay*** (*pulseaudio-utils*) is used to play a sound to a specified microphone output, which is mapped to a
      microphone input at startup.
    - ***paplay*** is triggered and plays a random file from **/home/zoomrec/audio**
    - Nothing will be played if directory:
        - does not contain **.wav** files
        - is not mounted properly

### CSV structure

CSV must be formatted as in example/meetings.csv

- Delimiter must be a semicolon "**;**"
- Only meetings with flag "**record = true**" are joined and recorded
- "**description**" is used for filename when recording
- "**duration**" in minutes (+5 minutes to the end)

weekday | time | duration | id | password | description | record
-------- | -------- | -------- | -------- | -------- | -------- | --------
monday | 09:55 | 60 | 111111111111 | 741699 | Important_Meeting | true
monday | 14:00 | 90 | 222222222222 | 321523 | Unimportant_Meeting | false
tuesday| 17:00 | 90 | https://zoom.us/j/123456789?pwd=abc || Meeting_with_URL | true

### VNC

You can connect to zoomrec via vnc and see what is happening.

#### Connect (default)

Hostname | Port | Password
-------- | -------- | --------
localhost   | 5901   | zoomrec

### Telegram
Zoomrec can notify you via Telegram about starting and ending a recording or if joining a meeting failed. All you need is a bot token and a chat id of a Telegram channel.

At first [create a new telegram bot](https://core.telegram.org/bots#6-botfather) to get the bot token. After that create a new channel and add the bot with sufficient permissions to write messages in that channel. Finally [get the chat id of your channel](https://gist.github.com/mraaroncruz/e76d19f7d61d59419002db54030ebe35) and look below how to pass your Telegram details to Zoomrec.

### Preparation

To have access to the recordings, a volume is mounted, so you need to create a folder that container users can access.

**[ IMPORTANT ]**

#### Create folders and set permissions (on Host)

```
mkdir -p recordings/screenshots
chown -R 1000:1000 recordings

mkdir -p audio
chown -R 1000:1000 audio
```

### Flags

#### Set timezone (default: Europe/Berlin)

```
docker run -d --restart unless-stopped \
  -e TZ=Europe/Berlin \
  -v $(pwd)/recordings:/home/zoomrec/recordings \
  -v $(pwd)/example/audio:/home/zoomrec/audio \
  -v $(pwd)/example/meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
kastldratza/zoomrec:latest
```

#### Set debugging flag (default: False)

- screenshot on error
- record joining
- do not exit container on error

```
docker run -d --restart unless-stopped \
  -e DEBUG=True \
  -v $(pwd)/recordings:/home/zoomrec/recordings \
  -v $(pwd)/example/audio:/home/zoomrec/audio \
  -v $(pwd)/example/meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
kastldratza/zoomrec:latest
```
#### Set Telegram details
```
docker run -d --restart unless-stopped \
  -e TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN" \
  -e TELEGRAM_CHAT_ID="-100_YOUR_CHAT_ID" \
  -v $(pwd)/recordings:/home/zoomrec/recordings \
  -v $(pwd)/example/audio:/home/zoomrec/audio \
  -v $(pwd)/example/meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
kastldratza/zoomrec:latest
```
#### Set Zoom display name 
```
docker run -d --restart unless-stopped \
  -e DISPLAY_NAME="zoomrec" \
  -v $(pwd)/recordings:/home/zoomrec/recordings \
  -v $(pwd)/example/audio:/home/zoomrec/audio \
  -v $(pwd)/example/meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
kastldratza/zoomrec:latest
```
### Windows / _cmd_

```cmd
docker run -d --restart unless-stopped \
  -v %cd%\recordings:/home/zoomrec/recordings \
  -v %cd%\example\audio:/home/zoomrec/audio \
  -v %cd%\example\meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
kastldratza/zoomrec:latest
```

### Windows / _PowerShell_

```powershell
docker run -d --restart unless-stopped `
  -v ${PWD}/recordings:/home/zoomrec/recordings `
  -v ${PWD}/example/audio:/home/zoomrec/audio `
  -v ${PWD}/example/meetings.csv:/home/zoomrec/meetings.csv:ro `
  -p 5901:5901 `
  --security-opt seccomp:unconfined `
kastldratza/zoomrec:latest
```

### Linux / macOS

```bash
docker run -d --restart unless-stopped \
  -v $(pwd)/recordings:/home/zoomrec/recordings \
  -v $(pwd)/example/audio:/home/zoomrec/audio \
  -v $(pwd)/example/meetings.csv:/home/zoomrec/meetings.csv:ro \
  -p 5901:5901 \
  --security-opt seccomp:unconfined \
kastldratza/zoomrec:latest
```

## Customization example

### Add meetings.csv to image

```bash
# Switch to example directory
cd example

# Build new image by customized Dockerfile
docker build -t kastldratza/zoomrec-custom:latest .

# Run image without mounting meetings.csv and audio directory
# Linux
docker run -d --restart unless-stopped -v $(pwd)/recordings:/home/zoomrec/recordings -p 5901:5901 --security-opt seccomp:unconfined kastldratza/zoomrec-custom:latest

# Windows / PowerShell
docker run -d --restart unless-stopped -v ${PWD}/recordings:/home/zoomrec/recordings -p 5901:5901 --security-opt seccomp:unconfined kastldratza/zoomrec-custom:latest

# Windows / cmd
docker run -d --restart unless-stopped -v %cd%\recordings:/home/zoomrec/recordings -p 5901:5901 --security-opt seccomp:unconfined kastldratza/zoomrec-custom:latest
```

---

## Supported actions

- [x] Show when the next meeting starts
- [x] _Join a Meeting_ from csv with id and password
- [x] Wrong error: _Invalid meeting ID_ / **Leave**
- [x] _Join with Computer Audio_
- [x] _Please wait for the host to start this meeting._
- [x] _Please wait, the meeting host will let you in soon._
- [x] _Enter Full Screen_
- [x] Switch to _Speaker View_
- [x] Continuously check: _This meeting is being recorded_ / **Continue**
- [x] Continuously check: _Hide Video Panel_
- [x] Continuously check: _This meeting has been ended by host_
- [x] Quit ffmpeg gracefully on abort
- [x] _Host is sharing poll results_
- [x] _This meeting is for authorized attendees only_ / **Leave meeting**
- [x] Play sound after joining a meeting
- [x] _Join a Meeting_ from csv with url

---

## Roadmap

- [ ] Refactoring
- [ ] Create terraform stack to deploy in AWS
- [ ] _Join a Meeting_ from calendar
- [ ] _Sign In_ to existing Zoom account
- [ ] _Join Breakout Room_
- [ ] Support to record Google Meet, MS Teams, Cisco WebEx calls too
- [ ] Ability to monitor recordings sessions in various containers

---

## Testing

Create unittests for different use cases:

- [ ] Join meeting
- [ ] Start / Stop ffmpeg and check if file was created
- [ ] ...

---

## Support

Feel free. However, if you want to support me and my work, I have some crypto addresses here.

name | address |
------------ | ------------- |
Bitcoin (BTC) | <details><summary>show</summary><p><img src="doc/support/bitcoin.png" width="150" /> <br> ```bc1qz2n26d4gq8qjdge9ueeluqut5p0rmv5wjmvnus``` </p></details>
Ethereum (ETH) | <details><summary>show</summary><p><img src="doc/support/ethereum.png" width="150" /> <br> ```0x984dBf7fb4ab489E33ca004552259484041AeF88``` </p></details>
Dogecoin (DOGE) | <details><summary>show</summary><p><img src="doc/support/dogecoin.png" width="150" /> <br> ```DHBCESbBPqER83h5E2j6cw6H1QZW8qHtYd``` </p></details>
Cardano (ADA) | <details><summary>show</summary><p><img src="doc/support/cardano.png" width="150" /> <br> ```addr1q90phcf0qzkx9da8vghtaa04a68gwpat37gvss963r9xfsj7r0sj7q9vv2m6wc3whm6ltm5wsur6hrusepqt4zx2vnpqz307az``` </p></details>

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
