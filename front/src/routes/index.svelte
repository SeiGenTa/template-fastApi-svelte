<script>
  import { link } from "svelte-spa-router";
</script>

<h1>Navigation</h1>
<ul>
  <li>
    <a href="/user/login" use:link>Login</a>
  </li>
  <li>
    <a href="/user/register" use:link>Register</a>
  </li>
</ul>
