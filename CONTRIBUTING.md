
# Contributing

Thanks for your interest in contributing! Please read carefully through our guidelines below to ensure that your contribution adheres to our project's standards.

## Code of Conduct

To hold a safe space for all contributors, we expect all project participants to adhere to our Code of Conduct. Please read the [full text](CODE_OF_CONDUCT.md) so that you can understand what actions will and will not be tolerated.

## Issue Tracking

We use [GitHub Issues](https://github.com/iitg-foss/beginners-tutorial/issues) to track all tasks related to this project.

To help you get your feet wet and get you familiar with our contribution process, we have [a list of friendly issues](https://github.com/iitg-foss/beginners-tutorial/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that contain tasks which are fairly easy to fix. This is a great place to get started.

## Build the project locally

In order to contribute to a project on GitHub, you must first get a copy of the project running locally on your computer. This process is sometimes called a "build process", and every project's process will have different requirements. Some requirements are due to the project being hosted on GitHub, some are due to the programming language used, some are due to the project's dependencies.

There are five steps to building this project:

1. [Set up Git and install Python](#set-up-git-and-install-nodejs)
2. [Fork the repository](#fork-the-repository)
3. [Clone your fork](#clone-your-fork)
4. [Run the project](#run-the-project)

Once you get the project built, see if you can fix some [issues](https://github.com/iitg-foss/beginners-tutorial/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

### Set up Git and Install Python

> **If you've never written Python before, don't sweat!** This exercise only requires fundamental language skills, you should be able to adapt from your favorite language.

All GitHub projects are backed by a version control software called *Git*. You'll need to [set up Git](https://help.github.com/articles/set-up-git/) in order to contribute to *any* project on GitHub.

This specific project is written in Python. You'll need to [install Python](https://www.python.org/downloads/) in order to run the project.

### Fork the repository

A *fork* is a copy of a repository. Forking a repository lets you to make changes to your copy without affecting any of the original code.

Click **Fork** (in the top-right corner of the page) to copy this repository to your GitHub account.

### Clone your fork

A *clone* is a downloaded version of a repository. Cloning our fork lets you download a copy of the repository to your computer.

Use `git` to clone your fork

```
$ git clone https://github.com/YOUR-USERNAME/beginners-tutorial
```

### Install dependencies

Did you know that the author usually does not write all of the code in a project?

The beauty of open source is that you can install and use code that other people have written, allowing you to focus on the unique requirements of your project. Third-party code that your project installs is called a *dependency* because it is required to work.

But since our institute has a proxy based internet system, it becomes quite hard for beginners to install these dependencies or packages. Therefore, in our project we won't be adding any dependencies.

### Run the project

Run the project by entering following in main repo folder.
```
python3 main.py
```

Run an automated test suite
```
python3 main.py test
```

## Submit a Pull Request

Remember how making changes on a *fork* doesn't affect the original code? Well, in order to fix an issue the in the main project, you *want* to change to the original code. A *pull request* is a GitHub feature that lets you do just that!

There are three steps to submitting a pull request:
1. [Save your changes locally](#save-your-changes-locally)
2. [Send your changes to your fork](#send-your-changes-to-your-fork)
3. [Open a Pull Request](#open-a-pull-request)

These instructions are designed to explain the bare minimum steps in a beginner-friendly way. If you find yourself hungry for more details (or get stuck), I applaud and encourage you to continue research on your own. You'll find no lack of amazing articles on this topic.

### Save your changes locally

First, get a list of all the files you have changed.
```
$ git status
```

Next, *stage* the file you want to save. This will add the file to a new list that is ready to be saved.
```
$ git add src/utils.py
```

Next, verify that the file has been staged correctly. Notice that the text color has changed, and your file is now in a list that says "Changes to be committed" instead of "Changes not staged for commit"
```
$ git status
```

Finally, save your staged files.
```
$ git commit -m "Fix issue#1"
```

You'll often hear this process called *committing* changes. It's the exact same thing.

### Send your changes to your fork

With one simple `git` command, you can send the changes you just committed locally to your *fork* on GitHub.

```
$ git push origin master
```

### Open a Pull Request

1. Find the [New Pull Request](https://github.com/iitg-foss/beginners-tutorial/compare/) button
2. Select the option to **compare across forks**
3. Select **your username** in the `head fork` option
4. Select **your username** in the `base` option
5. Click **Create Pull Request**

## License
By contributing, you agree that your contributions will be licensed under its MIT license.
