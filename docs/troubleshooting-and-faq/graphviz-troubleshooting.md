# 📈 Graphviz Troubleshooting

## Common Errors

### failed to execute WindowsPath('dot') / AttributeError: 'NoneType' object has no attribute '\_start\_node'

This is because the Graphviz install hasn't completed correctly, or you haven't added the executables to your systems PATH.

The best way to get around this is to just re-install using windows package manager which will sort the installation out for you.

**Steps:**

1. Press Windows Key + x
2. Click on the tab that says Terminal (Admin) or PowerShell(Admin)
3. Type or copy the following:

```sh
winget install graphviz
```

4. Wait for the install to finish and the run the script again

If you're still encountering errors, you can follow the steps below to add Graphviz to your PATH, or open an issue on our GitHub page: [New Issue](https://github.com/Jordan-Prescott/odins\_spear/issues/new)

## Adding Graphviz to PATH

#### Steps:

1. In the Windows Search Bar, search for: Edit the system Environment Variables
2. Click on 'Environment Variables' !\[\[environmentvariables.png]]
3. Under the 'User Variables' tab, click on 'New'
4. Enter the following details: !\[\[uservariables.png]]

After this, restart your computer to apply the changes and try your script again.

If you're still encountering errors, open an issue on our GitHub page: [New Issue](https://github.com/Jordan-Prescott/odins\_spear/issues/new)

## Installing Graphviz on Linux/Mac

Most Linux Distros have Graphviz supported in their package manager.

Execute the commands below in terminal depending on your distro:

Arch

```sh
sudo pacman -S graphviz
```

Debian/Ubuntu:

```sh
sudo apt install graphviz
```

Fedora:

```sh
sudo dnf install graphviz
```

MacOS (Needs homebrew):

```sh
brew install graphviz
```

[RPM resource graphviz (rpmfind.net)](https://rpmfind.net/linux/rpm2html/search.php?query=graphviz)