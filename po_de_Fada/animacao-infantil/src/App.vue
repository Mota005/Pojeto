<template>
  <div id="app">
    <Navbar />
    
    <Hero />
  </div>
</template>

<script setup>
// Importamos os dois componentes que já criaste
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
</script>

<style>
/* Estilos globais (podes manter os que já tens) */
:root {
  --cor-lilas-principal: #d6e4ff;
  --cor-texto-escuro: #2c3e50;
  --cor-texto-suave: #7f8c8d;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Inter', sans-serif; /* Ou a fonte que escolheste */
}
</style>