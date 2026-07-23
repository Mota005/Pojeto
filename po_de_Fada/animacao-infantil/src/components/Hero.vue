<template>
  <section id="hero" class="hero-full-section">
    
    <div class="hero-bg-image"></div>
    <div class="hero-overlay"></div>

    <div class="hero-container">
      <div class="hero-content">
        <span class="hero-badge animate-fade-down"> Animação Infantil & Eventos</span>
        
        <h1 class="hero-title animate-fade-up">
          Onde as <span class="highlight-text">histórias</span> ganham vida
        </h1>
        
        <p class="hero-subtitle animate-fade-up-delay">
          Animação Infantil • Eventos • Oficinas Criativas
        </p>

        <div class="hero-buttons animate-fade-up-more-delay">
          <a href="#contacto" class="btn-primary">
            Descobrir a Magia 
          </a>
          <a href="#servicos" class="btn-secondary">
            Ver Serviços
          </a>
        </div>
      </div>
    </div>

    <!-- ONDA BOTTOM REBAIXADA -->
    <div class="wave-bottom-hero">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,64L60,69.3C120,75,240,85,360,80C480,75,600,53,720,48C840,43,960,53,1080,64C1200,75,1320,85,1380,90.7L1440,96L1440,120L1380,120C1320,120,1200,120,1080,120C960,120,840,120,720,120C600,120,480,120,360,120C240,120,120,120,60,120L0,120Z" fill="#ffffff"/>
      </svg>
    </div>

  </section>
</template>

<style scoped>
.hero-full-section {
  position: relative;
  min-height: 85vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 140px 24px 100px 24px;
  overflow: hidden;
}

.hero-bg-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=1600');
  background-size: cover;
  background-position: center;
  z-index: 1;
  filter: saturate(1.2);
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg, 
    rgba(44, 62, 80, 0.82) 0%, 
    rgba(168, 127, 255, 0.75) 60%, 
    rgba(243, 232, 255, 0.85) 100%
  );
  z-index: 2;
}

.hero-container {
  position: relative;
  z-index: 3;
  max-width: 850px;
  margin: 0 auto;
  text-align: center;
}

.hero-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(10px);
  color: #ffffff;
  padding: 8px 22px;
  border-radius: 30px;
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.hero-title {
  font-size: 3.8rem;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.15;
  margin-bottom: 20px;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.highlight-text {
  color: #ffd700;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #f3e8ff;
  margin-bottom: 36px;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.hero-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  align-items: center;
}

.btn-primary {
  background: linear-gradient(135deg, #a87fff 0%, #8a53ff 100%);
  color: #ffffff;
  padding: 16px 36px;
  border-radius: 50px;
  font-weight: 800;
  text-decoration: none;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
  transition: all 0.3s ease;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 30px rgba(168, 127, 255, 0.5);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  color: #ffffff;
  padding: 16px 32px;
  border-radius: 50px;
  font-weight: 700;
  text-decoration: none;
  border: 1.5px solid rgba(255, 255, 255, 0.4);
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-3px);
}

.wave-bottom-hero {
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 4;
}

.wave-bottom-hero svg {
  width: 100%;
  height: 50px;
  display: block;
}

@media (max-width: 768px) {
  .hero-title { font-size: 2.6rem; }
  .hero-subtitle { font-size: 1.05rem; }
  .hero-buttons { flex-direction: column; }
  .btn-primary, .btn-secondary { width: 100%; box-sizing: border-box; }
}
</style>