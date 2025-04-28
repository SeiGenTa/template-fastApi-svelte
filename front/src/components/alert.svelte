<script lang="ts">
  export let message = "";
  export let type = "info"; // 'info', 'success', 'error'
  export let id = "";

  id = id || `alert-${Math.random().toString(36).substr(2, 9)}`;
</script>

<div class="alert {type}" id={id} style="view-transition-name: {id};">
  {message}
</div>

<style>
    .alert {
        padding: 1rem;
        border-radius: 0.25rem;
    }
    .info {
        background-color: #e7f3fe;
        color: #0c5460;
    }
    .success {
        background-color: #d4edda;
        color: #155724;
    }
    .error {
        background-color: #f8d7da;
        color: #721c24;
    }
</style>
