![Build Status](https://drone-ext.mcos.nc/api/badges/scrippy/scrippy-core/status.svg) ![License](https://img.shields.io/static/v1?label=license&color=orange&message=MIT) ![Language](https://img.shields.io/static/v1?label=language&color=informational&message=Python)


![Scrippy, my scrangourou friend](./scrippy-core.png "Scrippy, my scrangourou friend")

# `scrippy_core`

`scrippy_core` is the main _Python3_ module of the [`Scrippy`](https://codeberg.org/scrippy) framework for the normalization of _Python_ scripts writing.

This module provides all the basic functionalities such as configuration file management, log and execution history management, script access control, concurrent execution management, etc.

## Prerequisites

### System

#### Debian and derivatives

- python3
- python3-pip
- python-dev
- build-essential

### Python modules

#### List of required modules

The modules listed below will be installed automatically.

- prettytable
- coloredlogs
- argcomplete
- filelock
- PyYAML

## Installation


### Complete **Scrippy** framework installation and configuration

The **Scrippy** framework and all its packages can be installed with the [**Scrippy** installer and configuration helper](https://codeberg.org/scrippy/scrippy).

```shell
pip install scrippy
scrippy install
```
The commands listed above will install the **Scrippy** scripting framework with default values in the user home directory.

### With `pip`

```bash
sudo pip install scrippy-core
```

### Manual installation from source

```bash
git clone https://codeberg.org/scrippy/scrippy-core.git
cd scrippy-core
python -m pip install -r requirements.txt
make install
```

### Environment configuration details

At the start of each script, _Scrippy_ looks for its global configuration file at the following locations in the following order:

1. `/etc/scrippy/scrippy.yml`, allows package mainteners to provide a default _Scrippy_ configuration (i.e: _vendor config_)
2. `~/.config/scrippy/scrippy.yml`, allows users to configure _Scrippy_ without requiring administrator permissions
3. `/usr/local/etc/scrippy/scrippy.yml`, allows the system administrator to configure _Scrippy_.

When multiple configuration files exist within the same system, the configuration files are merged so that a user can override a default configuration without being able to override a configuration set up by the system administrator.

The _Scrippy_ configuration file must define a number of directories that will be useful to scripts based on _Scrippy_.

| Key                   | Purpose                                                                 |
| --------------------- | ----------------------------------------------------------------------- |
| `env.logdir`         | Directory of execution logs of scripts based on _Scrippy_              |
| `env.histdir`        | Directory of execution history files                                   |
| `env.reportdir`      | Directory of report files                                              |
| `env.tmpdir`         | Temporary directory for scripts based on _Scrippy_                     |
| `env.templatedirdir` | Directory of template files                                            |
| `env.confdir`        | Directory of configuration files for scripts based on _Scrippy_        |
| `env.datadir`        | Directory of data used by scripts based on _Scrippy_                   |

Model of _Scrippy_ execution environment configuration file:

```yaml
env:
  logdir: /var/log/scrippy
  histdir: /var/scrippy/hist
  reportdir: /var/scrippy/reports
  tmpdir: /var/tmp/scrippy
  datadir: /var/scrippy/data
  templatedir: /var/scrippy/templates
  confdir: /usr/local/etc/scrippy/conf
```

2. Creation of the directories defined in the configuration file `/usr/local/etc/scrippy/scrippy.yml`

Python script to create the necessary directories:

```python
import os
import yaml

conf_file = "/usr/local/etc/scrippy/scrippy.yml"
with open(conf_file, "r") as conf:
  scrippy_conf = yaml.load(conf, Loader=yaml.FullLoader)
  for rep in scrippy_conf["env"]:
    os.makedirs(scrippy_conf["env"][rep], 0o0775)
```

### Enabling auto-completion (optional)

If your shell has the `whence` command (i.e _zsh_), the argument parser (argparse) can be used to supply auto-completion. See [`argcomplete`'s documentation](https://argcomplete.readthedocs.io/en/latest/).

To activate it, launch the following command (installed with the `argcomplete` Python module):

```bash
sudo activate-global-python-argcomplete
```

Refresh your _Bash_ environment.

```bash
source /etc/profile
```

---

## Formalism

Scripts using the `scrippy_core` module must follow a certain formalism in order to ensure standardization of their format while facilitating the implementation of certain advanced functionalities such as the control of the validity of the configuration or the management of optional parameters.

Thus each script must include in its [_doc string_](https://www.python.org/dev/peps/pep-0257/) a declarative header and a set of predefined _sections_.


### Basic model

The basic model below can be used as a code snippet:

```python
#!/bin/env python3
"""
--------------------------------------------------------------------------------
  @author         : <Author>
  @date           : <Date of current script version>
  @version        : <X.Y.Z>
  @description    : <Brief description (one line) of the utility of the script>

--------------------------------------------------------------------------------
  Update:
  <X.Y.Z>  <Date> - <Author> - <Reason>: <Description of update>

--------------------------------------------------------------------------------
  List of authorized users or group:
    @user:<username>
    @group:<group name>

--------------------------------------------------------------------------------
  Concurrent executions:
    @max_instance: <INT>
    @timeout: <INT>
    @exit_on_wait: <BOOL>
    @exit_on_timeout: <BOOL>

--------------------------------------------------------------------------------
  List of mandatory configuration parameters:
    @conf:<section>|<key>|<type>|<secret>

--------------------------------------------------------------------------------
  List of execution options and argument parameters:
    @args:<name>|<type>|<help>|<number of arguments>|<default value>|<conflicts>|<implies>|<required>|<secret>

--------------------------------------------------------------------------------
  Functioning:
  ---------------
    <Detailed description of the script>
...
"""
#-------------------------------------------------------------------------------
#  Initialization of the environment
#-------------------------------------------------------------------------------
import scrippy_core
from scrippy_core import logger


#-------------------------------------------------------------------------------
#  Definition of functions and classes
#-------------------------------------------------------------------------------
class <Class>(<object>):
  def __init__(self, [<param>, ...]):
  [...]

def <function>([<param>, ...]):
  [...]

#-------------------------------------------------------------------------------
#  Main processing
#-------------------------------------------------------------------------------

def main():
  with scrippy_core.ScriptContext() as _context:
    # Retrieve config if necessary
    config = _context.config
    args = _context.args

    [...]

#-------------------------------------------------------------------------------
#  Entry point
#-------------------------------------------------------------------------------

if __name__ == '__main__':
  main()
```

A `main()` function **must**:

- Be defined in the `Definition of functions and classes` section
- Be called in the `Entry point` section
- Directly enclose its contents by `with scrippy_core.ScriptContext() as _context:` which manages and activates all the functionalities of scripts written from the `scrippy_core` module.

```python
def main():
  with scrippy_core.ScriptContext() as _context:
    # Script environement is accessed through `_context.env`
    # Script arguments are accessed through `_context.args`
    # Script configuration are accessed through `_context.config`

if __name__ == '__main__':
  main()
```

### Header elements

The `author`, `date`, `version`, `description` elements are **mandatory** and will be automatically displayed by the `--help` option.

#### Version

A script's version number is in the format X.Y.Z with:

- `X`, the major version identifier
- `Y` is the minor version identifier
- `Z`, the correction version identifier

**Major version X**: It is worth "0" during development, the script is considered invalid and should not be called by other scripts or used in production.

Once the script is validated, the version should be 1.0.0 (first stable version).

`X` should be incremented if changes in the code no longer guarantee backward compatibility.

The minor version identifiers `Y` and the correction version identifiers `Z` must be reset to zero when the major version identifier `X` is incremented.

**Minor version Y**: Must be incremented when adding new functionalities or improving the code that has no impact on backward compatibility.

The correction version identifier `Z` must be reset to zero when the minor version identifier is incremented.

**Correction version Z**: Must be incremented if only retro-compatible corrections are introduced.

A correction is defined as an internal change that corrects incorrect behavior (Bug).

`Z` can be incremented for typographical or grammatical correction.


#### Update:

In addition to the version number, modification date, and modification author, each line of the script history must indicate the reason for the modification.

`<Reason>` can take one of the following values:

- `cre`: Script creation
- `evo`: Script evolution (adding functionality, improving code, etc.)
- `bugfix`: Correction of unexpected behavior (bug)
- `typo`: Typo correction, adding comments, and any action that does not modify the code.

## Authorized Users and Groups

The `scrippy_core` module adds a verification layer to the script execution to ensure that a script is executed by a specific user or a user belonging to a specific group.

Placed in the header, a line such as `@user:harry.fink` will prevent execution by any user other than `harry.fink`.

It is possible to define several authorized users by multiplying the declarations:

```
@user:harry.fink
@user:luiggi.vercotti
```

It is also possible to authorize groups of users with a line such as `@group:monty` which ensures that only a user from the `monty` group executes the script.

In the same way as for users, it is possible to multiply group declarations:

```
@group:monty
@group:python
```

In the absence of `@user` and `@group` declarative lines, file permissions take precedence, and in all cases, file permissions have priority.

**Attention:** If a group and a user are declared, **both conditions must be met** for the user to be authorized to execute the script.

## Management of Concurrent Executions

The optional declarations `@max_instance`, `@timeout`, `@exit_on_wait`, and `@exit_on_timeout` make it possible to define the number of concurrent executions of the same script as well as the behavior of the script if necessary:

| Declaration        | Type                        | Utility                                                                                                          | Default value |
| ------------------ | --------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------- |
| `@max_instance`    | Integer                     | Maximum number of parallel executions                                                                            | 0 (infinite)  |
| `@timeout`         | Integer                     | Maximum waiting time expressed in seconds if `@exit_on_timeout` is set to true                                   | 0 (infinite)  |
| `@exit_on_timeout` | Boolean (`true`, `1`, `on`) | Exits the script with an error when the waiting time is reached                                                  | False         |
| `@exit_on_wait`    | Boolean (`true`, `1`, `on`) | Immediately exits the script with an error in case of waiting, even if the waiting time is not reached           | False         |

The waiting occurrences are executed sequentially in the order in which they are recorded in the execution queue.

In the following example, two occurrences of the script are allowed. A third execution will be put on hold for 10 seconds, after which the script will exit with an error if it cannot obtain a execution slot.

```
  @max_instance: 2
  @timeout: 10
  @exit_on_wait: false
  @exit_on_timeout: true
```

## Management and Verification of Mandatory Configuration Parameters

Any script may have an optional configuration file.

This configuration file will be automatically loaded at script start if:
- located in the directory defined by the `env::confdir` variable set by the [**Scrippy** main configuration file](#environment-configuration-details)
- has the same name as the script that must load it, stripped of its extension and suffixed with the `.conf` extension.

This way the script `exp_test_logs.py` will automatically load the configuration file `exp_test_logs.conf`.

A script configuration file is a simple _ini_ file divided into as many sections as necessary:

```ini
[log]
  level = ERROR
[database]
  host = srv.flying.circus
  port = 5432
  user = arthur.pewtey
  base = ministry_of_silly_walks
  password = parrot
# The section name may hashave spaces
[my section]
  my variable = my value
```

In such a file:

- Indentation is possible but optional
- A line beginning with `#` or `;` is considered a comment, even if it is indented.
- All values are strings:
  - It is up to the developer to convert the variable value to the desired type during processing (see [**_Retrieving a Value of a Particular Type_**](#retrieving-a-value-of-a-particular-type)).
  - Spaces are accepted in the section name, key name, or value.


### Validating the configuration file

In order to validate the configuration file, the script must contain a set of lines starting with `@conf` and describing the configuration file in its [_docstring_](https://www.python.org/dev/peps/pep-0257/).

The declaration lines of the configuration format must respect the following format:

```
@conf:<section>|<key>|<value_type>[|<secret>]
```

`<value_type>` must be one of the following recognized types:

- `str` (string of characters)
- `int` (integer)
- `float` (floating point number)
- `bool` (boolean)

`secret` is **optional** and if defined, must have the value `true` or `false`.

If `secret` is defined and has the value `true`, the configuration parameter value will be considered a _secret_ and will be redacted in the logging files.

Example:

From the following declaration:

```
@conf:log|level|str
@conf:database|port|int
@conf:sql|verbose|boolean
@conf:sql|database|str|false
@conf:sql|password|str|true
```

The following configuration file will be checked:

```
[log]
  level = error
[database]
  port = 5432
[sql]
  verbose = True
  database = monty
  password = d34dp4rr0t
```

All occurrences of the password `d34dp4rr0t` will be replaced by `*******` in the logging files and on the standard output.

No control over the values of the parameters is performed, so there is no need to indicate them. Only the structure of the configuration and the type of the keys are checked.

During the configuration check and if the logging level is set to `debug`, the loaded configuration will be displayed on the standard output and in the log (beware of the presence of passwords in the configuration when using the `debug` logging level).

```python
"""
@conf:database|port|int
@conf:database|base|str
@conf:database|host|str
@conf:database|password|str
@conf:database|user|str
@conf:local|dir|str
@conf:src|port|int
@conf:src|host|str
@conf:src|dir|str
@conf:src|user|str
@conf:dst|port|int
@conf:dst|host|str
@conf:dst|dir|str
@conf:dst|user|str
"""
import scrippy_core
from scrippy_core import logger

with scrippy_core.ScriptContext() as _context:
  # retrieving the configuration
  config = _context.config
```

If one of the sections or keys described by `@conf` is absent from the configuration file or if the type described for a key does not match the type found in the configuration file for that key, a critical error is raised and the script immediately exits with an error.

Extra sections or keys found in the configuration file that are not declared will simply be ignored during validation but will remain available to the script.

Thus in the above example, the `[mail]` section not being defined in `@conf` neither its presence nor its validity will be checked.


### Retrieving a configuration parameter value

Retrieving a parameter value from the configuration file is done through the `_context.config.get()` method.

```python
"""
@conf:database|port|int
@conf:database|base|str
@conf:database|host|str
@conf:database|password|str
@conf:database|user|str
"""
import logging
import scrippy_core
from scrippy_core import logger

with scrippy_core.ScriptContext() as _context:
  config = _context.config
  logger.info(config.get('database', 'host'))
```

In the above example, the value of the `host` key in the `database` section will be displayed on the screen.

If the section or key does not exist, an error is raised and **the script will immediately raise a critical error**.


#### Retrieving a value of a particular type

Unless the 'param_type' parameter is set to one of the authorized values (`str` (default), `int`, `float` or `bool`), the returned type is always a string.

Calling the `Config.get()` method with the wrong type will raise an error and **the script will immediately raise a critical error**.

```python
"""
@conf:log|level|str
@conf:database|port|int
@conf:database|base|str
@conf:database|host|str
@conf:database|password|str
@conf:database|user|str
"""
import scrippy_core
from scrippy_core import logger

with scrippy_core.ScriptContext() as _context:
  config = _context.config
  logger.info(config.get('database', 'port', 'int'))
```


### Reserved Sections and Keys:

Some sections and keys are automatically read and interpreted during the import of the `scrippy_core` module.

These configuration keys are optional, just like the configuration file.

- Log level, read and applied automatically:

```ini
[log]
  level = <str>
```

- Activation of logging and history (True by default):

```ini
[log]
  file = <bool>
```

More details in the **Runtime Logging Management** section.

### Examples

All examples in this documentation are based on all or part of the following configuration file:

```ini
[log]
  level = info
  file = true
[database]
  host = srv.flying.circus
  port = 5432
  user = arthur.pewtey
  base = ministry_of_silly_walks
  password = dead parrot
[local]
  dir = /tmp/transfert
[src]
  host = srv.source.circus
  port = 22
  user = harry.fink
  dir = /home/harry.fink/data
[dst]
  host = srv.destination.circus
  port = 22
  user = luigi.vercotti
  dir = /home/luigi.vercotti/received
[mail]
  host = srv.mail.circus
  port = 25
  from = Luiggi Vercotti
  from_addr = luiggi.vercotti@circus.com
  to = Harry Fink
  to_addr = harry.fink@circus.com
  subject =  Execution Report
```

## Execution options management

Script options can be managed through declarations in the [_docstring_](https://www.python.org/dev/peps/pep-0257/).

The declaration of an option is composed of 8 fields, some of which are required:

```
@args:<name>|<type>|<help>|<number of arguments>|<default value>|<conflicts>|<implies>|<required>|<secret>
```

with:

- **name**: The name of the option (required)
- **type**: One of the following values: `str`, `int`, `float`, `choice`, `bool` (default: str). If the type is `choice`, the list of possible choices must be entered in the **default value** field as a list of words separated by commas.
- **help**: A string summarising the purpose of this option (required).
- **number of arguments**: The number of arguments taken by the option. This field is mandatory for all types except `bool`, where the declared number of arguments is ignored. Its value is usually an integer but can take the value `+` when the number of arguments is greater than 1 but is not known in advance, or `?` when the number of arguments can be equal to zero.
- **default value**: The default value of the option (optional). `true` is the default value for `bool` options.
- **conflictx**: The list of options that conflict with the current option (optional, list of options separated by commas).
- **implies**: The list of options induced by the current option (optional, list of options separated by commas).
- **required**: A Boolean (`true` or `false`) indicating whether the option is mandatory or not.
- **secret**: A Boolean (`true` or `false`) indicating whether the option value should be kept secret.

The value of an option whose _secret_ attribute is set to `true` will be automatically masked in log files as well as in standard output.

The declaration of the options will automatically generate the help of the script accessible with the `--help` option.

The following options will also be automatically generated:

- `--version`: Displays the script version number from the information contained in the header.
- `--source-code`: Displays the source code of the script.
- `--hist [NB_EXECUTION (default:10)]`: Displays the execution history of the script.
- `--log [SESSION]`: Displays the content of the log file corresponding to the session whose identifier is passed as an argument. By default, the latest session is displayed.
- `--debug`: Forces the logging level to DEBUG (Changes in log level during execution are then ignored).
- `--no-stdout`: Disable log output to standard output except for *error* and *critial* messages.
- `--no-log-file`: Prevents the creation of log and history files.

The `--help`, `--version`, `--hist`, `--log`, `--debug`, `--no-stdout` and `--no-log-file` options should not be declared.

### Examples

The following script can be called with the following options and arguments:

- `--env`: Mandatory. Accepts one of the following values: qualif, preprod or prod
- `--appname`: Optional. A free string with a default value of "aviva"
- `--now`: Boolean option. If used, its value will be _true_ (false by default) and the `--date` option cannot be used.
- `--date`: A sequence of 3 integers from which a date will be created (i.e. 24 02 2019). This option conflicts with the `--now` option.
- `--email`: A free string. This option is mandatory if the `--now` option is used.

```python
#!/bin/env python3
"""
--------------------------------------------------------------------------------
  @author         : Florent Chevalier
  @date           : 2019-07-27
  @version        : 1.0.0
  @description    : test arguments

--------------------------------------------------------------------------------
  Update :
  1.0.0  2019-07-27   - Florent Chevalier   - Cre : Production
--------------------------------------------------------------------------------
    @args:appname|str|Application name|1|aviva|||false
    @args:date|int|Planning date(day, month, year)|3||now|email|false
    @args:email|str|Notification email address|1||||false
    @args:now|bool|Apply immediately||false|date||false
--------------------------------------------------------------------------------
"""
import datetime
import scrippy_core
from scrippy_core import logger

def print_contact(email):
  logger.info(" - Contact: {}".format(email))

def print_appname(appname):
  logger.info(" - Application: {}".format(appname))

def print_date(date):
  logger.info(" - Date: {}".format(date))

def main():
  with scrippy_core.ScriptContext() as _context:
    args = _context.args
    if args.date:
      date = "{}/{}/{}".format(args.date[0], args.date[1], args.date[2])
    if args.now:
      date = datetime.datetime.now().strftime('%d/%m/%Y')
    logger.info("[+] Report:")
    print_date(date)
    print_appname(args.appname)
    print_contact(args.email)

if __name__ == '__main__':
  main()
```


## Execution log management

Execution logging is done using the `scrippy_core.logger` object.

Two types of logs are simultaneously available:

- **Standard output**: Colored display towards `sys.stdout`
- **Log file**: A file located in log directory defined by the `env::logdir` variable set by the [**Scrippy** main configuration file](#environment-configuration-details).

The name of the log file is extrapolated from the name of the script as follows: `<script_name>_<timestamp>_<pid>.log`.

If a configuration file exists for the script and it contains a `[log]` section indicating a log level with the `level` key, then the indicated log level is automatically applied.

If the configuration file contains a `[log]` section with a `file` key whose value is `false`, then no log file will be created and only standard output will receive the logs.


### Defining the log level through the configuration file:

```
[log]
  level = warning
```

The value of the log level in the configuration file is case-insensitive.

The available log levels, from least verbose to most verbose, are [the logging levels of the standard logging module](https://docs.python.org/3/library/logging.html#logging-levels)

- `critical`
- `error`
- `warning`
- `info`
- `debug`

Note that the `debug` log level displays the entire configuration file as well as other details that could prove to be a source of information leakage. It is not recommended to use it in production.

All scripts written using the `scrippy_core` module have the following logging options:

- `--no-log-file`: When this option is used, no execution log is recorded on disk. This option does not prevent output on the screen.
- `--debug`: When this option is used, the log level is forced to `DEBUG`. In this case, the script does not take into account a possible configuration parameter indicating the opposite.

These two options can be combined and will override their equivalent defined in the configuration file.


## Error management

The **Scrippy** framework is intended to be used in production environments where debug trace or even stack traces should be avoided.

For the above reason, if an exception is not handled and propagates up to the *script context*, a `sys.exit(1)` will be triggered with a brief error message **with no stack trace**.

To display the stack trace, the log level must be set to `debug`.

Please, debug your scripts in testing environment !


## Execution history

The execution history file is located in the history directory defined by the `env::histdir` variable set by the [**Scrippy** main configuration file](#environment-configuration-details)

The execution history file will be created and named `<script_name>.db` at the first script execution.

This file is an _sqlite3_ database that lists all executions of a script.

For each execution the following information are stored:
- session identifier
- Start date of the execution
- End date of the execution
- Duration of the execution
- User who initiated the execution
- User who actually ran the script (in case of _sudo_)
- Return code of the execution (0 if OK, other value if KO)
- Set of parameters passed as arguments to the script
- Name of the error if the execution did not end correctly (0 otherwise)

If the history file already exists at execution time, it will be updated with the parameters of the new execution.

History is automatically enabled by enclosing the call to the `main` function with the declaration `with scrippy_core.ScriptContext() as _context:`

```python
with scrippy_core.ScriptContext() as _context:
  main()
```

Each script execution is assigned a session allowing each execution to be uniquely identified.

This session is composed of:

- a _timestamp_ representing the execution time
- the process identifier (PID)


Exemple:
  ```txt
  1568975414.6954327_10580
  ```

This session identifier is reported in the `Session` column of the history and allows the corresponding log to be found (See the `--log` option in [**_Execution options management_**](#execution-log-management)).


### Retention

The number of executions kept in the history file is **90** by default.

It is possible to override this value by specifying the desired retention number using the declaration `with scrippy_core.ScriptContext(retention=100) as _context:`

```python
with scrippy_core.ScriptContext(retention=100) as _context:
  config = _context.config
  args = _context.args
  <...>
```

### Displaying execution history

All scripts based on the `scrippy_core` module have an `--hist` option that allows you to display the last executions.

```shell
exp_test_script.py --hist
```

The number of executions to display can be specified by passing an integer parameter to the `--hist` option.

```shell
exp_test_script.py --hist 2
```

For each script execution, the execution history records the following information:
- The execution date
- The original user
- The effective user (_sudo_)
- The unique session identifier
- The exit code (0 by default)
- The list of options and arguments passed to the script

## Temporary workspace

The declaration `with scrippy_core.ScriptContext() as _context:` automatically creates a temporary workspace that will **automatically be destroyed with its contents at the end of the script**.

The workspace is located in the temporary directory defined by the `env::tmpdir` variable set by the [**Scrippy** main configuration file].

The exact path to this workspace can be obtained using the `workspace_path` attribute of the execution context `_context`.

```python
with scrippy_core.ScriptContext() as _context:
  workspace_path = _context.workspace_path
  ...
```

In the previous example, the `workspace_path` variable will contain the path to the temporary working directory, whose name will be constructed as follows: `scrippy_core.SCRIPPY_TMPDIR/<SCRIPT NAME>_<SESSION ID>`

Exemple:

```bash
/var/tmp/scrippy/exp_transfert_ftp_1574391960.6696503_102257
```

This temporary workspace, which will be **automatically destroyed with its contents at the end of the script**, is a directory that can be used to create temporary files used by the script.

```python
#!/bin/env python3
import os
import scrippy_core
from scrippy_core import logger

def create_file(workspace_path):
  tmp_file = "fichier.tmp"
  logger.info("[+] Creating temporary file: {}".format(os.path.join(workspace_path, tmp_file)))
  with open(os.path.join(workspace_path, tmp_file), 'a') as tmpfile:
    logger.info("[+] Writing in temporary file")
    tmpfile.write("Nobody expects the Spanish inquisition !")

def main():
  with scrippy_core.ScriptContext() as _context:
    config = _context.config
    create_file(_context.workspace_path)

if __name__ == '__main__':
  main()
```

## Accessing the environment

The environement is accessible through the `_context.env` dictionnary.

It contains all the initial environement variables that may be useful to scripts.

```python
#!/bin/env python3
import os
import scrippy_core
from scrippy_core import logger

def create_report(reportdir, filename):
  report_filename = os.join(reportdir, filename)
  logger.info(f"[+] Creating report file: {report_filename}")
  with open(report_filename), 'a') as report:
    logger.info("[+] Writing report file")
    report.write("Nobody expects the Spanish inquisition !")

def main():
  with scrippy_core.ScriptContext() as _context:
    config = _context.config
    create_report(_context.env.get("reportdir"), "inquisition.txt")

if __name__ == '__main__':
  main()
```

## Tips and guidelines

- A log is **never too verbose**
- **Priority should be given to readability** and maintainability rather than compactness and technicality
- Break down the code into **small functions**
- **Each function should log its entry point** and where possible, the parameters it receives
- **Maximize variable naming** and transfer as many variables as possible to the configuration file or run-time options (no hard coded values)
- **Simplify the main algorithm** of the program to its simplest expression
- **Handle errors as finely as possible** and as close as possible
- **Avoid global variables at all cost**
- **Minimize information leaks** in log files by using the `secret` attributes of options and arguments whose values are sensitive information (login, password, connection server, etc.)
- **Create a `main()` function** containing the script's main algorithm
- Create the environment (objects and variables used at the global level) in the `Entry point` section.

## Additional modules

The _Scrippy_ framework, of which `scrippy-core` is the core, has modules that facilitate the writing of advanced _Python_ scripts in accordance with Scrippy's basic principles.

| Module             | Utility                                                       |
| ------------------ | ------------------------------------------------------------- |
| `scrippy-template` | Template file management (based on _Jinja2_)                  |
| `scrippy-remote`   | Implementation of _SSH/SFTP_ and _FTP_ protocols               |
| `scrippy-mail`     | Implementation of _SMTP_, _POP_ and _Spamassassin_ protocols   |
| `scrippy-git`      | Git repository management                                     |
| `scrippy-db`       | Database management (_PostgreSQL_ and _Oracle_)                |
| `scrippy-api`      | Using _REST API_ (based on _resquets_)                         |

All available modules are available at [**https://codeberg.org/scrippy**](https://codeberg.org/scrippy)
