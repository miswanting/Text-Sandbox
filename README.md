# Text-Sandbox
A Text Sandbox with Python &amp; Go.

## 目录结构

mods\

A [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd) instance has the following methods:

- `Cmd.``cmdloop`(*intro=None*)

  Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument.The optional argument is a banner or intro string to be issued before the first prompt (this overrides the [`intro`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.intro) class attribute).If the [`readline`](https://docs.python.org/3/library/readline.html#module-readline) module is loaded, input will automatically inherit **bash**-like history-list editing (e.g. `Control-P` scrolls back to the last command, `Control-N` forward to the next one, `Control-F` moves the cursor to the right non-destructively, `Control-B` moves the cursor to the left non-destructively, etc.).An end-of-file on input is passed back as the string `'EOF'`.An interpreter instance will recognize a command name `foo` if and only if it has a method `do_foo()`. As a special case, a line beginning with the character `'?'` is dispatched to the method `do_help()`. As another special case, a line beginning with the character `'!'` is dispatched to the method `do_shell()` (if such a method is defined).This method will return when the [`postcmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd) method returns a true value. The *stop* argument to [`postcmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd) is the return value from the command’s corresponding `do_*()` method.If completion is enabled, completing commands will be done automatically, and completing of commands args is done by calling `complete_foo()` with arguments *text*, *line*, *begidx*, and *endidx*. *text* is the string prefix we are attempting to match: all returned matches must begin with it. *line* is the current input line with leading whitespace removed, *begidx* and *endidx* are the beginning and ending indexes of the prefix text, which could be used to provide different completion depending upon which position the argument is in.All subclasses of [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd) inherit a predefined `do_help()`. This method, called with an argument `'bar'`, invokes the corresponding method `help_bar()`, and if that is not present, prints the docstring of `do_bar()`, if available. With no argument, `do_help()` lists all available help topics (that is, all commands with corresponding `help_*()` methods or commands that have docstrings), and also lists any undocumented commands.


- `Cmd.``onecmd`(*str*)

  Interpret the argument as though it had been typed in response to the prompt. This may be overridden, but should not normally need to be; see the [`precmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.precmd) and [`postcmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd) methods for useful execution hooks. The return value is a flag indicating whether interpretation of commands by the interpreter should stop. If there is a `do_*()` method for the command *str*, the return value of that method is returned, otherwise the return value from the [`default()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.default) method is returned.


- `Cmd.``emptyline`()

  Method called when an empty line is entered in response to the prompt. If this method is not overridden, it repeats the last nonempty command entered.


- `Cmd.``default`(*line*)

  Method called on an input line when the command prefix is not recognized. If this method is not overridden, it prints an error message and returns.


- `Cmd.``completedefault`(*text*, *line*, *begidx*, *endidx*)

  Method called to complete an input line when no command-specific `complete_*()` method is available. By default, it returns an empty list.


- `Cmd.``precmd`(*line*)

  Hook method executed just before the command line *line* is interpreted, but after the input prompt is generated and issued. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd); it exists to be overridden by subclasses. The return value is used as the command which will be executed by the [`onecmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.onecmd) method; the [`precmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.precmd) implementation may re-write the command or simply return *line*unchanged.


- `Cmd.``postcmd`(*stop*, *line*)

  Hook method executed just after a command dispatch is finished. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd); it exists to be overridden by subclasses. *line* is the command line which was executed, and *stop* is a flag which indicates whether execution will be terminated after the call to [`postcmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd); this will be the return value of the [`onecmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.onecmd) method. The return value of this method will be used as the new value for the internal flag which corresponds to *stop*; returning false will cause interpretation to continue.


- `Cmd.``preloop`()

  Hook method executed once when [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop) is called. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd); it exists to be overridden by subclasses.


- `Cmd.``postloop`()

  Hook method executed once when [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop) is about to return. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd); it exists to be overridden by subclasses.

Instances of [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd) subclasses have some public instance variables:

- `Cmd.``prompt`

  The prompt issued to solicit input.


- `Cmd.``identchars`

  The string of characters accepted for the command prefix.


- `Cmd.``lastcmd`

  The last nonempty command prefix seen.


- `Cmd.``cmdqueue`

  A list of queued input lines. The cmdqueue list is checked in [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop) when new input is needed; if it is nonempty, its elements will be processed in order, as if entered at the prompt.


- `Cmd.``intro`

  A string to issue as an intro or banner. May be overridden by giving the [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop) method an argument.


- `Cmd.``doc_header`

  The header to issue if the help output has a section for documented commands.


- `Cmd.``misc_header`

  The header to issue if the help output has a section for miscellaneous help topics (that is, there are `help_*()` methods without corresponding `do_*()` methods).


- `Cmd.``undoc_header`

  The header to issue if the help output has a section for undocumented commands (that is, there are `do_*()` methods without corresponding `help_*()` methods).


- `Cmd.``ruler`

  The character used to draw separator lines under the help-message headers. If empty, no ruler line is drawn. It defaults to `'='`.


- `Cmd.``use_rawinput`

  A flag, defaulting to true. If true, [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop) uses [`input()`](https://docs.python.org/3/library/functions.html#input) to display a prompt and read the next command; if false, `sys.stdout.write()` and `sys.stdin.readline()` are used. (This means that by importing [`readline`](https://docs.python.org/3/library/readline.html#module-readline), on systems that support it, the interpreter will automatically support **Emacs**-like line editing and command-history keystrokes.)