
# DEPLOYMENT CONCEPT

* deployment needs to be specified for
    * framework (dev edition)
    * finished game (player edition)

This file specifies the folder and file structures for both deployment
variants.

## IDEALIZED STRUCTURES (VISION)

### DEV VERSION (concept 1)

**IMPORTANT NOTE:**
**THIS CONCEPT IS OBSOLOTE. TAKE CONCEPT 2 INSTEAD**

Seperate framework code from project code, avoid redundancy of framework code and libraries / executables.

The path to the executable is stored in the `configuration.txt`.

**advantages**

* no redundant code
* hide complexity from user
* projects are more project-like

**disadvantages**

* framework can not easily be adjusted for a specific game
* more complex installation and initialization of new projects


    xylophone/
        ./bin/
        ./lib/
        ./pgw/


    $(workspace)/
        ./some-project/
            ./assets/
                ./images/
                ./sounds/
            ./rooms/
            ./objects/
            ./sprites/

            ./configuration.txt

        ./some-other-project/
            ...

### DEV VERSION (concept 2) (chosen concept)

The framework contains everything from the python executable to the actual project code.

**advantages**

* no setup or other form of installation necessary, the template will work immediately after being dropped somewhere on the disk.
* no complicated configuration of projects about where the executable lies or something

**disadvantages**

* heavy redundancy of thirdparty libraries and cpython
* user will see all the complexity and will maybe wonder what this is about.


    xylophone/
        ./bin/
        ./lib/
        ./pgw/

        ./some-project/
            ./assets/
                ./images/
                ./sounds/
            ./rooms/
            ./objects/
            ./sprites/

        ./configuration.txt

        ./LICENSE_PGW   #license info for pgw itself
        ./LICENSE_PRJ   #license information for the actual project


### GAME VERSION

The game version needs these files/folders:

* actual game content
* configuration files
* python executable
* pygame libraries
* framework code
* start script or executable

The actual game code files should be hidden from the player, so something like the following could be a good idea.

    ${game}/
        ./${game}_launcher.sh|.bat|...
        ./LICENSE
        ./bin/
            ./python/
            ./pgw/
            ./project/
            ./configfile
            ./secondary start scripts

## WAY OF DEPLOYMENT

possible options:
* zip file

### DEV VERSION

* the shipping of the dev version should be the final folder structure packed into a zip file.

### GAME VERSION

* a `create-release-package.sh` or a `.bat` would be cool
* the shipping should also be via some zip file
