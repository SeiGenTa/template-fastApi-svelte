<script lang="ts">
  import PrimaryButton from "../../components/primaryButton.svelte";
  import Alert from "../../components/alert.svelte";
  import { validateEmail, validateUsername, validatePassword } from "../../lib/validations.ts";

  interface errorInfo {
    text: string;
    type: string;
    id?: string;
  }

  let errors: errorInfo[] = [];

  const post = async (data: FormData) => {
    const response = await fetch("/api/v1/user/register", {
      method: "POST",
      body: data,
    });
    if (!response.ok) {
      const error = await response.json();
      addAlert(error.message, "error");
    } else {
      const result = await response.json();
      if (result.success) {
        addAlert("Registration successful", "success");
      } else {
        addAlert(result.message, "error");
      }
    }
  };

  const submit = (e: Event) => {
    clearAlerts();
    e.preventDefault();
    const form = document.getElementById("form-register") as HTMLFormElement;
    if (!form) {
      addAlert("Internal error", "error");
    }
    const formData = new FormData(form);

    const email = formData.get("email")!.valueOf() as string;
    const validationEmail = validateEmail(email);
    if (validationEmail) {
      addAlert(validationEmail, "error");
    }

    const username = formData.get("username")!.valueOf() as string;
    const validationUsername = validateUsername(username);
    if (validationUsername) {
      addAlert(validationUsername, "error");
    }

    const password = formData.get("password")!.valueOf() as string;
    const validationPassword = validatePassword(password);
    if (validationPassword) {
      addAlert(validationPassword, "error");
    }
    const confirmPassword = formData.get("confirm_password")!.valueOf() as string;
    if (password !== confirmPassword) {
      addAlert("Passwords do not match", "error");
    }

    const terms = formData.get("terms");
    if (!terms) {
      addAlert("You must accept the terms and conditions", "error");
    }

    if (errors.length > 0) {
      return;
    }

    post(formData);
  };

  const addAlert = (text: string, type: string) => {
    if (document.startViewTransition) {
      document.startViewTransition(() => {
        errors = [...errors, { text: text, type: type, id: text }];
      });
    } else {
      errors = [...errors, { text: text, type: type, id: text }];
    }
  };

  const clearAlerts = () => {
    if (document.startViewTransition) {
      document.startViewTransition(() => {
        errors = [];
      });
    } else errors = [];
  };
</script>

<main>
  <form method="POST" action="/api/user/register" id="form-register" on:submit={submit}>
    <h3>Register</h3>
    <div>
      <label for="email">Email</label>
      <input type="email" id="email" name="email" />
    </div>
    <div>
      <label for="username">Username</label>
      <input type="text" id="username" name="username" />
    </div>
    <div>
      <label for="password">Password</label>
      <input type="password" id="password" name="password" />
    </div>
    <div>
      <label for="confirm_password">confirm password</label>
      <input type="password" id="confirm_password" name="confirm_password" />
    </div>
    <div>
      <input type="checkbox" id="terms" name="terms" />
      <label for="terms">I agree to the terms and conditions</label>
    </div>

    <div>
      <div id="alerts">
        {#each errors as error}
          <Alert type={error.type} message={error.text} id={error.id}></Alert>
        {/each}
      </div>

      <PrimaryButton>Register</PrimaryButton>
    </div>
  </form>
</main>

<style>
  main {
    height: 100%;
    background-color: #56baec;
  }

  form div:has(input[type="checkbox"]) {
    flex-direction: row;
    align-items: center;
  }

  form div:has(input[type="checkbox"]) label {
    margin-left: 0.5rem;
  }

  main {
    display: flex;
    width: 100%;
    height: 100%;
    padding: 1rem;
  }

  h3 {
    text-align: center;
    font-size: 1.4rem;
    margin-bottom: 0.5rem;
  }

  form {
    width: 100%;
    max-width: 400px;
    padding: 1rem;
    border-radius: 0.5rem;
    background-color: #fefefe;
    margin: auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  form div {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  input {
    padding: 0.2rem;
    border-color: transparent;
    border-bottom-color: black;
    border-width: 0.1rem;
    transition: border-color 0.1s ease;
    outline: none;
  }

  input:focus {
    border-bottom-color: #56baec;
  }

  form div:has(input:hover) label {
    color: #408cb3;
  }

  form div:has(input:focus) label {
    color: #56baec;
  }

  #alerts {
    gap: 0.2rem;
  }
</style>
