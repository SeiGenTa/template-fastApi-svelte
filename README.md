# template-fastApi-svelte

## Instructions
You need to create a file called `.env`.  
This version does not have a database yet, so you can use the following example:

```txt
# .env
PORT=8080       # General port (used by nginx in dev mode and by the backend in prod mode)
PORT_FRONT=8081 # Port for the front-end app (used by "npm run dev" in dev mode only)
PORT_BACK=8082  # Port for the back-end app (used by Uvicorn in dev mode only)
```

Now, to initialize the template, you must execute the following command:
```bash
make init
```
This command initializes the template and installs all dependencies.

To launch the development mode, you must run the following command:
```bash
make run
```
This command starts the development mode, and everything will work on a single port (8080 if you use the example `.env`).

## Production
When you want to launch your app in production mode, you must run the following commands:

```bash
make init # Only if you haven't executed this command before.
make build
make run-production
```

The `make build` command packages the front-end application and places it in the correct location so it can be served by the back-end app.

