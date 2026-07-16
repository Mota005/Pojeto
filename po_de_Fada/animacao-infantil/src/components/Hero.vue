<template>
  <section class="hero-section">
    <div class="magic-orb orb-1"></div>
    <div class="magic-orb orb-2"></div>
    <div class="magic-orb orb-3"></div>

    <div class="magic-sparkle sparkle-1"></div>
    <div class="magic-sparkle sparkle-2"></div>
    <div class="magic-sparkle sparkle-3"></div>
    <div class="magic-sparkle sparkle-4"></div>

    <div class="hero-container">
      
      <div class="hero-content">
        <h1 class="hero-title">Onde as histórias ganham vida</h1>
        <p class="hero-subtitle">
          <span>Animação Infantil</span> • 
          <span>Eventos</span> • 
          <span>Oficinas Criativas</span>
        </p>
        <div class="hero-actions">
          <a href="#servicos" class="btn-hero-magico">
            Descobrir a Magia <span class="brilho-emoji">✨</span>
          </a>
        </div>
      </div>

      <div class="hero-image-wrapper">
        <div class="blob-frame">
          <img src="https://images.unsplash.com/photo-1485546246426-74dc88dec4d9?w=600" alt="Crianças a divertirem-se na Pó de Fada" class="hero-main-img">
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.hero-section {
  position: relative;
  min-height: 90vh; 
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 100px; 
  background-color: #faf6ff;
  overflow: hidden;
}

.hero-container {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 48px;
}

/* ─── EFEITO 1: ORBS DE LUZ (FUNDO) ─── */
.magic-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.55;
  z-index: 1;
  pointer-events: none;
}

.orb-1 {
  top: -10%;
  left: -10%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(232,219,255,1) 0%, rgba(214,228,255,0.2) 100%);
}

.orb-2 {
  bottom: -10%;
  right: 5%;
  width: 450px;
  height: 450px;
  background: radial-gradient(circle, rgba(255,224,230,1) 0%, rgba(253,246,255,0.1) 100%);
}

.orb-3 {
  top: 30%;
  left: 45%;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(214,228,255,0.8) 0%, rgba(232,219,255,0) 100%);
}

/* ─── EFEITO 2: BRILHOS SUTIS EM CSS ─── */
.magic-sparkle {
  position: absolute;
  background: #ffd700; 
  border-radius: 50%;
  z-index: 3; /* Fica à frente do fundo para garantir visibilidade */
  pointer-events: none;
  box-shadow: 0 0 10px 3px rgba(255, 215, 0, 0.7), 0 0 20px rgba(255, 255, 255, 0.9);
  animation: twinkle 3s ease-in-out infinite;
}

/* Posições bem distribuídas */
.sparkle-1 {
  top: 25%;
  left: 8%;
  width: 6px;
  height: 6px;
  animation-delay: 0s;
}

.sparkle-2 {
  top: 15%;
  right: 12%;
  width: 8px;
  height: 8px;
  animation-delay: 1s;
}

.sparkle-3 {
  bottom: 25%;
  left: 15%;
  width: 7px;
  height: 7px;
  animation-delay: 1.8s;
}

.sparkle-4 {
  bottom: 35%;
  right: 8%;
  width: 5px;
  height: 5px;
  animation-delay: 0.5s;
}

@keyframes twinkle {
  0%, 100% {
    transform: scale(0.6);
    opacity: 0.2;
  }
  50% {
    transform: scale(1.5);
    opacity: 0.8; /* Brilho bem definido no ponto alto da animação */
  }
}

/* ─── LADO ESQUERDO: TEXTOS ─── */
.hero-content {
  flex: 1;
  text-align: left;
}

.hero-title {
  font-size: 3.8rem;
  color: var(--cor-texto-escuro, #2c3e50);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 20px;
  letter-spacing: -1.5px;
}

.hero-subtitle {
  font-size: 1.15rem;
  color: var(--cor-texto-suave, #7f8c8d);
  font-weight: 500;
  margin-bottom: 40px;
}

.hero-subtitle span {
  margin-right: 8px;
}

/* ─── EFEITO 3: MOLDURA LÍQUIDA (BLOB) ─── */
.hero-image-wrapper {
  flex: 1;
  display: flex;
  justify-content: center;
}

.blob-frame {
  width: 100%;
  max-width: 460px;
  height: 460px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(193, 217, 255, 0.4);
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: morphing-blob 8s ease-in-out infinite;
}

.hero-main-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@keyframes morphing-blob {
  0%, 100% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  }
  50% {
    border-radius: 45% 55% 50% 50% / 50% 55% 45% 50%;
  }
}

/* ─── EFEITO 4: BOTÃO COM SHIMMER (BRILHO) ─── */
.btn-hero-magico {
  position: relative;
  display: inline-block;
  background-color: var(--cor-lilas-principal, #e8dbff);
  color: var(--cor-texto-escuro, #2c3e50);
  text-decoration: none;
  padding: 18px 40px;
  border-radius: 50px; 
  font-weight: 700;
  font-size: 1.15rem;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(193, 217, 255, 0.4);
  overflow: hidden;
}

.btn-hero-magico::after {
  content: '';
  position: absolute;
  top: 0;
  left: -150%;
  width: 50%;
  height: 100%;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.8) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: skewX(-20deg);
}

.btn-hero-magico:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 30px rgba(193, 217, 255, 0.6);
}

.btn-hero-magico:hover::after {
  animation: shine-effect 1.2s ease-in-out infinite;
}

@keyframes shine-effect {
  100% {
    left: 150%;
  }
}

/* ─── RESPONSIVIDADE (TELEMÓVEL) ─── */
@media (max-width: 768px) {
  .hero-section {
    min-height: 100vh;
  }

  .hero-container {
    flex-direction: column-reverse;
    text-align: center;
    gap: 32px;
  }

  .hero-content {
    text-align: center;
  }

  .hero-title {
    font-size: 2.6rem;
  }

  .blob-frame {
    max-width: 300px;
    height: 300px;
  }
}
</style>