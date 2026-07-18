<script setup>
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import Sobre from './components/Sobre.vue'
import Servicos from './components/Servicos.vue'
import Duvidas from './components/Duvidas.vue' // 1. Importa as Dúvidas
import BrilhosMagicos from './components/BrilhosMagicos.vue'
</script>

<template>
  <div class="main-layout">
    <Navbar />
    <Hero />
    <Sobre />
    <Servicos />
    <Duvidas /> <!-- 2. Insere aqui -->
    <BrilhosMagicos />
  </div>
</template>

<style>
/* Estilos globais essenciais para o efeito funcionar */
.main-layout {
  position: relative; /* Cria a base de altura total para o BrilhosMagicos se guiar */
  width: 100%;
  overflow-x: hidden; /* Evita barras de scroll horizontal indesejadas */
  background-color: #faf6ff;
}

/* Limpeza básica de margens */
body {
  margin: 0;
  padding: 0;
}
</style>