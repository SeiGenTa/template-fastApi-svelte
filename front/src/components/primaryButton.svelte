<script>
  export let onClick = () => {};
</script>

<button on:click={onClick}>
  <slot />
</button>

<style>
  button {
    background-color: #56baec;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.25rem;
    cursor: pointer;
    transition: background 0.1s ease-in-out;
  }
  button:hover {
    background-color: rgb(68, 170, 153);
  }
</style>
