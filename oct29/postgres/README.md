# PostgreSQL - Notes

## Architectue fundamentals

PostgreSl uses a client/server model and a session consistss of two cooperatin subprocessess(programs):

- A server process, which managess the db files, accepts connections to db from client apps, and performs db actions on behalf of the clients. The server program is called **postgres**

- The user's client application that wants to perform db ops. (Client) Client apps can be very diverse in nature: a client could be a text oriented tool, GUI app, or a web server that accesses the dbs to display web pagees, or a specialized db maintenance tool. Some client applications are supplied with the PostgreSQL distribution with some features. But most are developed by users.

- **postgres** server can handlee multiple concurrent connections from clients. To achieve this, it forks a new process for each connection. Fro that point on, the clieent and the new server proceess communicate without intervention by the original **posstgres** process. Thus, the master server process is always running, waiting for client connections, whereas client and associated server processess come and go. (All of this process is invisible to the user.)

## Creating Databases

To create database in PostGre we can simply use `createdb` command.


Example:

```bash
$createdb mydb
```

>> Note: Aceessing Command line tools
To use command line tools in the mac use this command:
`sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp`
It will add path to our postgress binaries.

To delete the database:

```bash
$dropdb mydb
```
## Accesssing the db

Once we have created db, we can acess it by:

- Running PSQL in terminal with `psql` command which allows us to interactively enter, edit and execute SQL commands.

- Use graphical frontend tools like pgAdmin, or ODBC or JDBC to create and manipulate the db. 

- Write a custom application with language bindings.

To access from the command line:

```bash
$psql mydb
Output:
mydb => ..
```

You can easily modify your db and perform ops on it once you have created your db.

### Test some commands

- `SELECT version();`

- `SELECT current_date;`

- `SELECT 2 + 2`

- ` \h ` => Will provide you details about commands. help

>>Note: For convience we will use asyncpg and use the Postgre from there with its protocols.

To install asyncpg use:

```bash
$pip3 install asyncpg
```
