<script lang="ts">
  import PrimaryButton from "../../components/primaryButton.svelte";

  </script>
  
  <main>
    <form method="POST">
      <h3>Login</h3>
      <div>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" />
      </div>
      <div>
        <PrimaryButton
          onClick={() => {
            console.log("login");
          }}>login</PrimaryButton
        >
      </div>
    </form>
  </main>
  
  <style>
    main {
      display: flex;
      width: 100%;
      height: 100%;
      background-color: #56baec;
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
  
    form div:has(input:focus) label{
      color: #56baec;
    }
  </style>
  