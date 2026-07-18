<template>
  <div class="sparkles-global-wrapper">
    <!-- As nossas novas estrelas mágicas de 4 pontas -->
    <div class="sparkle sp-global-1"></div>
    <div class="sparkle sp-global-2"></div>
    <div class="sparkle sp-global-3"></div>
    <div class="sparkle sp-global-4"></div>
    <div class="sparkle sp-global-5"></div>
    <div class="sparkle sp-global-6"></div>
  </div>
</template>

<style scoped>
.sparkles-global-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 3;
}

/* ─── BASE DA ESTRELA VIVA DE 4 PONTAS ─── */
.sparkle {
  position: absolute;
  background: #ffcc00; /* Um dourado muito mais vivo e saturado */
  
  /* TRUQUE MÁGICO: Recorta a div em formato de estrela de 4 pontas perfeita */
  clip-path: polygon(50% 0%, 61% 35%, 100% 50%, 61% 65%, 50% 100%, 39% 65%, 0% 50%, 39% 35%);
  
  /* Sombra proeminente para criar contraste nos fundos claros */
  filter: drop-shadow(0 0 6px rgba(255, 204, 0, 0.9)) drop-shadow(0 0 12px rgba(168, 127, 255, 0.4));
  
  animation: pulse-twinkle 3.5s ease-in-out infinite;
}

/* Roteiro de animação corrigido: agora ela nunca fica quase invisível (mínimo de 0.4) */
@keyframes pulse-twinkle {
  0%, 100% {
    transform: scale(0.6) rotate(0deg);
    opacity: 0.4; /* Visível mesmo no ponto mais baixo */
  }
  50% {
    transform: scale(1.3) rotate(90deg); /* Roda ligeiramente enquanto brilha! */
    opacity: 1; /* Brilho máximo e opacidade total */
  }
}

/* ─── COORDENADAS E TAMANHOS (Aumentámos os tamanhos para se destacarem) ─── */
.sp-global-1 { top: 6%; left: 7%; width: 14px; height: 14px; animation-delay: 0s; }
.sp-global-2 { top: 24%; right: 8%; width: 18px; height: 18px; animation-delay: 1.2s; }
.sp-global-3 { top: 44%; left: 6%; width: 16px; height: 16px; animation-delay: 0.5s; }
.sp-global-4 { top: 62%; right: 10%; width: 12px; height: 12px; animation-delay: 2s; }
.sp-global-5 { top: 79%; left: 9%; width: 18px; height: 18px; animation-delay: 0.9s; }
.sp-global-6 { top: 93%; right: 6%; width: 15px; height: 15px; animation-delay: 2.5s; }
</style>