# Usage
    Warnup usage:
      warnup [action] [arguments]

    Actions:
      push [file] - Deploys file into production path
      diff [file] - Shows a diff between the local/production versions

# Why?
At my current job we can't always do things the easy way. I'd love to be able to type `git push origin master` and have my code be deployed instantly, but unfortunately the world can't always work that way!

That's why I've created Warnup. It's an incredibly simple utility that allows us to compare and move code between our development and production environment. This could probably be done with simple shell commands but I like taking any excuse for writing python that I can get. 

I hope you find it useful!
