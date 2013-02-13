# What is it?
Warnup is a utility that allows you to compare/work with two directories (in my use case, development and production) easily. It makes it easy to generate diffs and push (and eventually pull) files in bulk between the two.

# Why?
Sometimes working with large systems doesn't allow you to do things the easiest way (for example: `git push origin master` and bam, instant deployment). I was faced with this issue at my current job, and I felt that deploying to production should be easy and painless.

That's why I've created Warnup. It's an incredibly simple utility that allows you to compare and move code between a development and production environment. This could probably be done with simple shell commands, but I'll taking any excuse for writing some python that I can get!

# Installation
If you have `pip`, installing warnup is as simple as:

    $ pip install warnup

Next you'll need to create a simple configuration file in your development environment:

```bash
$ cd /path/to/development
$ vim .warnup
```

The basic requirement for a configuration file is:

```ini
[paths]
development = /path/to/development
production  = /path/to/production
```

Example `.warnup`:

```ini
[paths]
development = /home/steve/mysite
production  = /var/www/mysite
[utils]
; Allows you to specify which diff utility to use (I like meld)
diff=meld
```

And that's it! Warnup should be good to go.

# Usage
    Warnup usage:
      warnup [action] [arguments]

    Actions:
      push [file]    - Deploys file into production path
      push           - Deploys the current stage
      diff [file]    - Shows a diff between the local/production versions
      stage [file]   - Stages a file for a bulk push
      unstage [file] - Removes a file from the current stage
      stage          - Displays a list of files currently staged

# Usage examples

## Pushing a file to production

```bash
$ warnup diff news/index.php
# Check diff to make sure it looks good
$ warnup push news/index.php
[notice] Creating backup at /Users/steve/test/prod/news/index.php.temp
[success] news/index.php successfully pushed

Would you like to save, delete, or restore the backup file? (s/d/r) d
[success] Backup file deleted
```

## Pushing multiple files to production

```bash
$ warnup diff news/index.php
$ warnup diff test.php
# Both diffs look good
$ warnup stage news/index.php
[success] news/index.php successfully staged
$ warnup stage test.php
[success] test.php successfully staged
$ warnup push
Staged files:  
   test
   hello
Are you sure you would like to push these changes? (y/N) y
[success] Stage successfully pushed!

test.php - Would you like to save, delete, or restore the backup file? (s/d/r) d
news/index.php - Would you like to save, delete, or restore the backup file? (s/d/r) d
# Both files are now in production!
```
