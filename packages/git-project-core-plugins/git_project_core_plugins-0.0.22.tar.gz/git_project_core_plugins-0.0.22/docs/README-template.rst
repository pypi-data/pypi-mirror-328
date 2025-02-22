************************
git-project-core-plugins
************************

Plugins for `git-project <http://www.github.com/greened/git-project>`_

This is a set of basic plugins to manage several aspects of projects kept within
git repositories.  These plugins include commands to:

#. Configure git-project and its various plugins
#. Clone repositories
#. Manage branches
#. Manage worktrees
#. Run commands (e.g configure/build/install)

Setup
=====

``pip install git-project-core-plugins``

Commands
========

These plugins add a number of commands to git-project.  Each command has an
associated ``--help`` option to describe its function and options.  There is
also a `help` command that accesses more extensive manpage-like descriptions of
commands.

* ``git <project> config``

  Configure git-project or any git config sections added by projects.  This will
  add ``config`` subcommands to plugin commands that manipulate git config
  sections (e.g. ``git project build config``).

* ``git <project> clone [--worktree]``

  Clone a repository.  Other plugins may hook into this command to provide
  additional functionality.  With ``--worktree``, set up a worktree environment.

* ``git <project> init [--worktree]``

  Initialize a ``git-project`` config in an existing cloed repository.  With
  ``--worktree``, setup a worktree environment.

* ``git <project> branch status``

  Report whether local branches are merged to a project branch and whether the
  local branch head is pushed to a remote.

* ``git <project> branch prune``

  Delete branches that are merged to a project branch and pushed to a remote.

* ``git <project> run <command> [<args>]``

  Run a pre-configured commandm, passing ``<args>`` to it.

* ``git <project> worktree``

  Create and manage worktrees for the project.  This plugin gives ``git
  <project> clone`` an option to create a special directory layout and a master
  worktree when performing a bare clone.

  Worktrees can be referenced to set up per-worktree build and install trees
  such that switching from worktree to worktree does not result in "rebuilding
  the world."

Worktree environment
====================

A number of commands can have knowledge of a "worktree environment" with a
specific layout:

  <path>
    .git
    worktree1
    worktree2
    worktree3

That is, either a bare clone is done, or an existing clone is converted to a
bare clone via ``git <project> init --worktree``.  Any conversion will abort if
the worktree is dirty.  Typically, an ordinary ``git clone`` is followed
immediately by ``git <project> init --worktree``.

Examples
========

Initial setup
-------------

  git clone <url>
  git <project> init --worktree

Add convenience substitution variables
--------------------------------------

Adding custom commands
----------------------

  git <project> run --make-alias configure
  git <project> run --make-alias build
  git <project> run --make-alias install

  git <project> add configure debug "cd {builddir} && "
