<script>
  import Router from "svelte-spa-router";
  import index from "./routes/index.svelte";
  import login from "./routes/user/login.svelte";
  import register from "./routes/user/register.svelte";

  const routes = {
    "/": index,
    "/user/login": login,
    "/user/register": register,
  };
</script>

<Router {routes} />

<style>
</style>
