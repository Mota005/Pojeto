<script setup>
import { onMounted } from 'vue'
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import Sobre from './components/Sobre.vue'
import Servicos from './components/Servicos.vue'
import Duvidas from './components/Duvidas.vue'
import Testemunhos from './components/Testemunhos.vue'
import Contacto from './components/Contacto.vue'
import Footer from './components/Footer.vue'
import BotaoWhatsapp from './components/BotaoWhatsapp.vue'
import BrilhosMagicos from './components/BrilhosMagicos.vue'
import CookieBanner from './components/CookieBanner.vue'

// Efeito de animação ao fazer scroll para TODOS os títulos
onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
        }
      })
    },
    { threshold: 0.15 } // Ativa quando 15% do título entra no ecrã
  )

  // Seleciona automaticamente todos os h1, h2 e títulos de secção
  const titles = document.querySelectorAll('h1, h2, .reveal-title')
  titles.forEach((el) => observer.observe(el))
})
</script>

<template>
  <div class="main-layout">
    <Navbar />
    <Hero />
    <Sobre />
    <Servicos />
    <Duvidas />
    <Testemunhos />
    <Contacto />
    <Footer />

    <BotaoWhatsapp />
    <BrilhosMagicos />
    <CookieBanner/>
  </div>
</template>

<style>
/* SCROLL SUAVE EM TODA A PÁGINA */
html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Nunito', sans-serif;
  overflow-x: hidden;
}

.main-layout {
  position: relative;
  width: 100%;
  overflow-x: hidden;
  background-color: #faf6ff;
}

/* ─── ANIMAÇÃO GLOBAL DE SCROLL PARA TÍTULOS (H1, H2, etc.) ─── */
h1, h2, .reveal-title {
  opacity: 0;
  transform: translateY(35px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

/* Quando o título entra na vista do ecrã */
h1.is-visible, h2.is-visible, .reveal-title.is-visible {
  opacity: 1;
  transform: translateY(0);
}
</style>