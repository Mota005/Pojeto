<script setup>
import { ref, onMounted } from 'vue'

const visivel = ref(false)

onMounted(() => {
  // Verifica se o utilizador já respondeu ao aviso anteriormente
  const consentimento = localStorage.getItem('podefada_cookies')
  if (!consentimento) {
    // Dá um pequeno atraso de 1.5s antes de aparecer para não ser intrusivo
    setTimeout(() => {
      visivel.value = true
    }, 1500)
  }
})

const aceitarCookies = () => {
  localStorage.setItem('podefada_cookies', 'aceite')
  visivel.value = false
}

const recusarCookies = () => {
  localStorage.setItem('podefada_cookies', 'recusado')
  visivel.value = false
}
</script>

<template>
  <transition name="slide-up">
    <div v-if="visivel" class="cookie-banner">
      <div class="cookie-content">
        <span class="cookie-icon">🍪</span>
        <p class="cookie-text">
          Utilizamos cookies para garantir que tens a melhor experiência mágica no nosso site. 
          Ao continuar a navegar, concordas com a nossa utilização de cookies.
        </p>
      </div>
      
      <div class="cookie-actions">
        <button @click="recusarCookies" class="btn-cookie btn-refuse">
          Recusar
        </button>
        <button @click="aceitarCookies" class="btn-cookie btn-accept">
          Aceitar
        </button>
      </div>
    </div>
  </transition>
</template>

<style scoped>
.cookie-banner {
  position: fixed;
  bottom: 24px;
  left: 24px;
  max-width: 480px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(168, 127, 255, 0.25);
  border-radius: 20px;
  padding: 18px 22px;
  box-shadow: 0 15px 35px rgba(44, 62, 80, 0.15);
  display: flex;
  flex-direction: column;
  gap: 14px;
  z-index: 10000; /* Fica acima de tudo, mas abaixo do WhatsApp */
}

.cookie-content {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.cookie-icon {
  font-size: 1.5rem;
  line-height: 1;
}

.cookie-text {
  font-size: 0.88rem;
  color: #2c3e50;
  line-height: 1.5;
  margin: 0;
}

.cookie-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.btn-cookie {
  padding: 8px 18px;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.25s ease;
  border: none;
}

.btn-refuse {
  background: transparent;
  color: #7f8c8d;
  border: 1px solid #e2e8f0;
}

.btn-refuse:hover {
  background: #f8fafc;
  color: #2c3e50;
}

.btn-accept {
  background: linear-gradient(135deg, #a87fff 0%, #8a53ff 100%);
  color: #ffffff;
  box-shadow: 0 4px 12px rgba(168, 127, 255, 0.3);
}

.btn-accept:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(168, 127, 255, 0.4);
}

/* ANIMAÇÃO SLIDE-UP */
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(40px);
}

@media (max-width: 600px) {
  .cookie-banner {
    left: 16px;
    right: 16px;
    max-width: none;
    bottom: 16px;
  }
}
</style>