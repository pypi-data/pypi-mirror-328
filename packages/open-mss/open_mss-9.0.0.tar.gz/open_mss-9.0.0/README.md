Mission Support System Usage Guidelines
=======================================

Welcome to the Mission Support System software for planning
atmospheric research flights. This document is intended to point you
into the right direction in order to get the software working on your
computer.


## Installing MSS

We distinguish between Developer and User installations.

### Developer Installation
Please read our [contributing](https://open-mss.github.io/contributing/) pages.
and [development](https://mss.readthedocs.io/en/stable/development.html) guidelines

### User Installation

Get **pixi** from https://pixi.sh/latest/ for your operation system.

You can now decide if you want to install **mss** as global or a project.

#### Global installation
You can install **mss** global without defining a project first.
This method is practical when you are interested in starting the client
and don't need server configurations.

    pixi global install mss

#### Usage

    msui
    mswms -h
    mscolab -h
    mssautoplot -h


##### Updating

    pixi global update mss

#### Project installation
Initialize a new project and navigate to the project directory.

    pixi init MSS
    cd MSS

Use the shell command to activate the environment and start a new shell in there.

    pixi shell

Add the **mss** dependencies from conda-forge.

    (MSS) pixi add mss

##### Usage
Always when you want to start **mss** programs you have after its installation
to activate the environment by pixi shell in the project dir.
On the very first start of **msui** it takes a bit longer because it setups fonts.

    cd MSS
    pixi shell

    (MSS) msui
    (MSS) mswms -h
    (MSS) mscolab -h
    (MSS) mssautoplot -h

##### Updating

    cd MSS
    pixi shell
    (MSS) pixi update mss
