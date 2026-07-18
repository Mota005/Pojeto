<template>
  <section class="hero-section">
    <!-- EFEITO 1: Esferas mágicas de luz desfocadas no fundo (Orbs) -->
    <div class="magic-orb orb-1"></div>
    <div class="magic-orb orb-2"></div>
    <div class="magic-orb orb-3"></div>

  
    <!-- EFEITO 3: Formas geométricas abstratas flutuantes (Textura) -->
    <div class="floating-shape shape-plus-1">+</div>
    <div class="floating-shape shape-plus-2">+</div>
    <div class="floating-shape shape-ring-1"></div>

    <div class="hero-container">
      <!-- Lado Esquerdo: Textos e Botão com Shimmer -->
      <div class="hero-content">
        <h1 class="hero-title">
          Onde as <span class="title-highlight">histórias</span> ganham vida
        </h1>
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

      <!-- Lado Direito: Foto com Moldura Líquida + Anel Traseiro Rotativo -->
      <div class="hero-image-wrapper">
        <div class="photo-bg-ring"></div>
        <div class="blob-frame">
          <img src="https://images.unsplash.com/photo-1485546246426-74dc88dec4d9?w=600" alt="Crianças a divertirem-se na Pó de Fada" class="hero-main-img">
        </div>
      </div>
    </div>

    <!-- ─── NOVO DIVISOR: ONDA QUE COBRE 100% DA LARGURA DA PÁGINA ─── -->
    <div class="wave-splitter">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,32L60,42.7C120,53,240,75,360,74.7C480,75,600,53,720,48C840,43,960,53,1080,64C1200,75,1320,85,1380,90.7L1440,96L1440,120L1380,120C1320,120,1200,120,1080,120C960,120,840,120,720,120C600,120,480,120,360,120C240,120,120,120,60,120L0,120Z" fill="#ffffff"/>
      </svg>
    </div>
  </section>
</template>

<style scoped>
.hero-section {
  position: relative;
  min-height: 100vh; 
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 120px; 
  padding-bottom: 140px; /* Espaço para a onda não tapar o botão ou textos */
  background: linear-gradient(180deg, #faf6ff 0%, #f7f3ff 100%);
  overflow: hidden;
}

.hero-container {
  position: relative;
  z-index: 5;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 60px;
}

/* ─── ONDA 100% LARGURA DA PÁGINA ─── */
.wave-splitter {
  position: absolute;
  bottom: -1px; /* Cola perfeitamente à secção seguinte para não deixar linhas vazias */
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 10;
}

.wave-splitter svg {
  width: 100%;
  height: 100px; /* Altura ideal para a onda ser suave e visível */
  display: block;
}

/* ─── ORBS DE LUZ (FUNDO) ─── */
.magic-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(90px);
  opacity: 0.5;
  z-index: 1;
  pointer-events: none;
}
.orb-1 { top: -10%; left: -5%; width: 500px; height: 500px; background: radial-gradient(circle, rgba(232,219,255,1) 0%, rgba(214,228,255,0.2) 100%); }
.orb-2 { bottom: 20%; right: -5%; width: 550px; height: 550px; background: radial-gradient(circle, rgba(255,224,230,1) 0%, rgba(253,246,255,0.1) 100%); }
.orb-3 { top: 40%; left: 35%; width: 350px; height: 350px; background: radial-gradient(circle, rgba(214,228,255,0.8) 0%, rgba(232,219,255,0) 100%); }

/* ─── BRILHOS SUTIS ─── */
.magic-sparkle {
  position: absolute;
  background: #ffd700; 
  border-radius: 50%;
  z-index: 3;
  pointer-events: none;
  box-shadow: 0 0 10px 3px rgba(255, 215, 0, 0.7), 0 0 20px rgba(255, 255, 255, 0.9);
  animation: twinkle 3s ease-in-out infinite;
}
.sparkle-1 { top: 25%; left: 8%; width: 6px; height: 6px; animation-delay: 0s; }
.sparkle-2 { top: 15%; right: 12%; width: 8px; height: 8px; animation-delay: 1s; }
.sparkle-3 { bottom: 35%; left: 15%; width: 7px; height: 7px; animation-delay: 1.8s; }
.sparkle-4 { bottom: 45%; right: 8%; width: 5px; height: 5px; animation-delay: 0.5s; }

@keyframes twinkle {
  0%, 100% { transform: scale(0.6); opacity: 0.2; }
  50% { transform: scale(1.5); opacity: 0.8; }
}

/* ─── FORMAS FLUTUANTES ─── */
.floating-shape {
  position: absolute;
  color: rgba(168, 127, 255, 0.25);
  font-weight: 300;
  pointer-events: none;
  z-index: 2;
}
.shape-plus-1 { top: 35%; left: 6%; font-size: 2.5rem; animation: float-slow 6s ease-in-out infinite; }
.shape-plus-2 { bottom: 35%; right: 45%; font-size: 2rem; animation: float-slow 8s ease-in-out infinite 1.5s; }
.shape-ring-1 { top: 20%; right: 48%; width: 24px; height: 24px; border: 3px solid rgba(193, 217, 255, 0.4); border-radius: 50%; animation: float-slow 7s ease-in-out infinite 0.5s; }

@keyframes float-slow {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(45deg); }
}

/* ─── TEXTOS E GRADIENTE ─── */
.hero-content {
  flex: 1.1;
  text-align: left;
}
.hero-title {
  font-size: 4rem;
  color: #2c3e50;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 24px;
  letter-spacing: -1.5px;
}
.title-highlight {
  background: linear-gradient(135deg, #a87fff 0%, #c1d9ff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}
.hero-subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  font-weight: 500;
  margin-bottom: 40px;
}
.hero-subtitle span { margin-right: 8px; }

/* ─── FOTO E FAIXA ROTATIVA ─── */
.hero-image-wrapper {
  flex: 0.9;
  display: flex;
  justify-content: center;
  position: relative;
}
.photo-bg-ring {
  position: absolute;
  top: -20px;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  width: 480px;
  height: 480px;
  border: 2px dashed rgba(168, 127, 255, 0.25);
  border-radius: 50%;
  z-index: 1;
  animation: spin-slow 25s linear infinite;
}
@keyframes spin-slow { 100% { transform: rotate(360deg); } }

.blob-frame {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 440px;
  height: 440px;
  overflow: hidden;
  box-shadow: 0 25px 50px rgba(153, 126, 189, 0.25);
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: morphing-blob 10s ease-in-out infinite;
}
.hero-main-img { width: 100%; height: 100%; object-fit: cover; }

@keyframes morphing-blob {
  0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
  50% { border-radius: 45% 55% 50% 50% / 50% 55% 45% 50%; }
}

/* ─── BOTÃO MÁGICO ─── */
.btn-hero-magico {
  position: relative;
  display: inline-block;
  background: linear-gradient(135deg, #e8dbff 0%, #c1d9ff 100%);
  color: #2c3e50;
  text-decoration: none;
  padding: 18px 44px;
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
  top: 0; left: -150%; width: 50%; height: 100%;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.8) 50%, rgba(255, 255, 255, 0) 100%);
  transform: skewX(-20deg);
}
.btn-hero-magico:hover { transform: translateY(-4px); box-shadow: 0 15px 30px rgba(193, 217, 255, 0.6); }
.btn-hero-magico:hover::after { animation: shine-effect 1.2s ease-in-out infinite; }
@keyframes shine-effect { 100% { left: 150%; } }

/* ─── RESPONSIVIDADE ─── */
@media (max-width: 992px) {
  .hero-container { flex-direction: column-reverse; text-align: center; gap: 40px; }
  .hero-content { text-align: center; }
  .hero-title { font-size: 3rem; }
  .photo-bg-ring { width: 340px; height: 340px; }
  .blob-frame { max-width: 300px; height: 300px; }
  .wave-splitter svg { height: 60px; } /* Onda mais discreta no mobile */
}
</style>