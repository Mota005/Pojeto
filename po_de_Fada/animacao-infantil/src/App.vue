<template>
  <div id="app">
    <Navbar />
    
    <Hero />

    <Sobre/>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import Sobre from './components/Sobre.vue' // 1. Importa a nova secção
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