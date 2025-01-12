# Git / GitHub
For ease of collaboration

1. Install [Git](https://git-scm.com/downloads)
    * Keep default settings during install process
2. Setup [SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    * Make sure to select the right platform (Mac or Windows or Linux)
    * Complete the *Generating a new SSH key* and *Adding your SSH key to the ssh-agent* sections
    * No need to add it to your account yet, as you will do this in the next step
3. Add [SSH Key to Your Account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui)
    * Make sure to select the right platform (Mac or Windows or Linux)
    * Complete the *Adding a new SSH key to your account* section
4. If you DON'T know how to use VIM in Terminal, run: `git config --global core.editor "nano"`

# Windows Users Only: Install WSL2
* For UNIX consistency across all OS
* Instructions can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install)
* Complete the *Get started*, *Set up your Linux username and password*, and *Update and upgrade packages* sections.

# Virtual Environment
To minimize interference with other Python dependencies

1. MacOS / Linux: Download [Conda](https://www.anaconda.com/download/success)
    * Keep default settings during install process
2. Windows: Go to [this website](https://www.anaconda.com/download/success) and follow the following instructions:
    * Right click the Linux installer and copy the link address
    * Open WSL in a Command Prompt
    * Run: `sudo apt install curl`
    * Run: `sudo curl -o conda-install.sh <the Linux installer link address you copied>`
    * Run: `bash conda-install.sh` and keep default settings during install process
3. Run: `conda create -n Demand-Forecast python=3.12`

# VsCode (Optional)
* Install [here](https://code.visualstudio.com/download)
* Windows users will also need the [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
