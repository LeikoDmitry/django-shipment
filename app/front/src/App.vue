<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <router-link active-class="active" class="nav-link" :to="{name: 'Home'}">Home</router-link>
          <router-link active-class="active" class="nav-link" :to="{name: 'Create'}">Create</router-link>
        </ul>
      </div>
    </div>
  </nav>
  <router-view/>
</template>
