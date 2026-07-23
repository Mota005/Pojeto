<template>
  <section id="hero" class="hero-section">
    <div class="hero-container">
      
      <!-- ─── LADO ESQUERDO: TEXTO & CTA ─── -->
      <div class="hero-content">
        <h1 class="hero-title">
          Onde as <span class="highlight-text">histórias</span> ganham vida
        </h1>
        
        <p class="hero-subtitle">
          Animação Infantil • Eventos • Oficinas Criativas
        </p>

        <div class="hero-buttons">
          <a href="#contacto" class="btn-primary">
            Descobrir a Magia
          </a>
        </div>
      </div>

      <!-- ─── LADO DIREITO: FOTO EM CIRCULO ─── -->
      <div class="hero-visual">
        <div class="circle-frame">
          <img 
            src="https://images.unsplash.com/photo-1544717305-2782549b5136?w=800" 
            alt="Menino encantado com um livro" 
            class="hero-img"
          />
        </div>
      </div>

    </div>

    <!-- ONDA NO FUNDO DA HERO -->
    <div class="wave-bottom-hero">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,32L60,42.7C120,53,240,75,360,80C480,85,600,75,720,64C840,53,960,43,1080,48C1200,53,1320,75,1380,85.3L1440,96L1440,120L1380,120C1320,120,1200,120,1080,120C960,120,480,120,360,120C240,120,120,120,60,120L0,120Z" fill="#ffffff"/>
      </svg>
    </div>
  </section>
</template>

<style scoped>
.hero-section {
  position: relative;
  background-color: #faf6ff;
  padding: 140px 24px 100px 24px;
  overflow: hidden;
}

.hero-container {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: 50px;
}

/* LADO ESQUERDO */
.hero-title {
  font-size: 3.2rem;
  font-weight: 800;
  color: #2c3e50;
  line-height: 1.15;
  margin-bottom: 16px;
}

.highlight-text {
  background: linear-gradient(135deg, #a87fff 0%, #d8b4fe 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.15rem;
  color: #7f8c8d;
  margin-bottom: 32px;
  font-weight: 600;
}

.btn-primary {
  display: inline-block;
  background: linear-gradient(135deg, #a87fff 0%, #8a53ff 100%);
  color: #ffffff;
  padding: 16px 36px;
  border-radius: 50px;
  font-weight: 800;
  text-decoration: none;
  box-shadow: 0 10px 25px rgba(168, 127, 255, 0.35);
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 30px rgba(168, 127, 255, 0.45);
}

/* LADO DIREITO */
.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.circle-frame {
  width: 380px;
  height: 380px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(153, 126, 189, 0.2);
  border: 4px solid #ffffff;
  outline: 2px dashed rgba(168, 127, 255, 0.4);
  outline-offset: 8px;
}

.hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ONDA BOTTOM */
.wave-bottom-hero {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 4;
}

.wave-bottom-hero svg {
  width: 100%;
  height: 70px;
}

/* RESPONSIVIDADE */
@media (max-width: 900px) {
  .hero-container {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .circle-frame {
    width: 280px;
    height: 280px;
  }
}
</style>