<script setup>
import { ref } from 'vue'

const flippedCards = ref({})

const toggleFlip = (index) => {
  flippedCards.value[index] = !flippedCards.value[index]
}
</script>

<template>
  <section id="servicos" class="servicos-section">
    
    <!-- ─── A ONDA DE TRANSIÇÃO (Encaixa perfeitamente no branco do Sobre) ─── -->
    <div class="wave-top-divider">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,0L60,10.7C120,21,240,43,360,48C480,53,600,43,720,37.3C840,32,960,32,1080,42.7C1200,53,1320,75,1380,85.3L1440,96L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z" fill="#ffffff"/>
      </svg>
    </div>

    <div class="servicos-container">
      <!-- Topo da secção -->
      <div class="servicos-content-top">
        <span class="servicos-badge">O que Oferecemos</span>
        <h2 class="servicos-title">Os Sonhos Que Tornamos Realidade</h2>       
        <p class="servicos-instruction">Clica nas cartas para descobrir a magia </p>
      </div>
      
      <!-- Grelha das Cartas em 3D -->
      <div class="servicos-content-pacs">
        
        <!-- CARTA 1 -->
        <div class="flip-card" :class="{ 'is-flipped': flippedCards[0] }" @click="toggleFlip(0)">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="card-img-wrapper">
                <img src="https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=500" alt="Animação Infantil" class="card-img">
                <div class="card-img-overlay"></div>
              </div>
              <div class="card-front-info">
                <span class="card-icon"></span>
                <h3>Animação Infantil</h3>
              </div>
            </div>
            <div class="flip-card-back">
              <span class="card-icon-back"></span>
              <h3>Animação Infantil</h3>
              <p>Modelagem de balões, pinturas faciais profissionais, jogos dinâmicos e muita música para pôr todos a dançar.</p>
              <span class="btn-voltar">Fechar ↩</span>
            </div>
          </div>
        </div>

        <!-- CARTA 2 -->
        <div class="flip-card" :class="{ 'is-flipped': flippedCards[1] }" @click="toggleFlip(1)">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="card-img-wrapper">
                <img src="https://images.unsplash.com/photo-1513151233558-d860c5398176?w=500" alt="Eventos Estilizados" class="card-img">
                <div class="card-img-overlay"></div>
              </div>
              <div class="card-front-info">
                <span class="card-icon"></span>
                <h3>Eventos Estilizados</h3>
              </div>
            </div>
            <div class="flip-card-back">
              <span class="card-icon-back"></span>
              <h3>Eventos Estilizados</h3>
              <p>Decoração temática completa, planeamento personalizado e festas com personagens vivas saídas dos contos de fadas.</p>
              <span class="btn-voltar">Fechar ↩</span>
            </div>
          </div>
        </div>

        <!-- CARTA 3 -->
        <div class="flip-card" :class="{ 'is-flipped': flippedCards[2] }" @click="toggleFlip(2)">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="card-img-wrapper">
                <img src="https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=500" alt="Oficinas Criativas" class="card-img">
                <div class="card-img-overlay"></div>
              </div>
              <div class="card-front-info">
                <span class="card-icon"></span>
                <h3>Oficinas Criativas</h3>
              </div>
            </div>
            <div class="flip-card-back">
              <span class="card-icon-back"></span>
              <h3>Oficinas Criativas</h3>
              <p>Atividades manuais e artísticas onde os mais pequenos dão asas à imaginação e criam as suas próprias recordações.</p>
              <span class="btn-voltar">Fechar ↩</span>
            </div>
          </div>
        </div>

      </div>
    </div>        
  </section>
</template>

<style scoped>
.servicos-section {
  background-color: #faf6ff; /* Lilás suave de fundo */
  padding: 140px 24px 100px 24px; /* Aumentado o padding topo para dar espaço à onda */
  position: relative;
}

/* ─── ESTILO DA ONDA NO TOPO ─── */
.wave-top-divider {
  position: absolute;
  top: -1px; /* Garante que morde o fundo branco do Sobre sem deixar linhas vazias */
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 5;
}

.wave-top-divider svg {
  width: 100%;
  height: 90px;
  display: block;
}

/* ─── RESTANTE DESIGN DOS SERVIÇOS ─── */
.servicos-container {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 6;
}

.servicos-content-top {
  text-align: center;
  margin-bottom: 60px;
}

.servicos-badge {
  display: inline-block;
  background-color: #f3e8ff;
  color: #a87fff;
  padding: 6px 16px;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 16px;
}

.servicos-title {
  font-size: 2.8rem;
  color: #2c3e50;
  font-weight: 800;
  letter-spacing: -1px;
  margin-bottom: 8px;
}

.servicos-instruction {
  font-size: 1rem;
  color: #7f8c8d;
  font-weight: 500;
}

.servicos-content-pacs {
  display: flex;
  justify-content: center;
  gap: 30px;
}

/* CARTAS 3D FLIP */
.flip-card {
  flex: 1;
  max-width: 360px;
  height: 420px;
  perspective: 1000px;
  cursor: pointer;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style: preserve-3d;
}

.flip-card.is-flipped .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 24px;
  box-shadow: 0 10px 30px rgba(153, 126, 189, 0.06);
  border: 1px solid rgba(168, 127, 255, 0.08);
  overflow: hidden;
}

.flip-card-front {
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
}

.card-img-wrapper {
  position: relative;
  width: 100%;
  height: 70%;
}

.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-img-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(180deg, rgba(0,0,0,0) 60%, rgba(153, 126, 189, 0.15) 100%);
}

.card-front-info {
  height: 30%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 16px;
}

.card-icon {
  font-size: 2rem;
  margin-bottom: 6px;
}

.card-front-info h3 {
  font-size: 1.3rem;
  color: #2c3e50;
  font-weight: 700;
  margin: 0;
}

.flip-card-back {
  background: #ffffff;
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 32px 24px;
  border: 2px solid #e8dbff;
}

.card-icon-back {
  font-size: 2.5rem;
  margin-bottom: 12px;
}

.flip-card-back h3 {
  font-size: 1.4rem;
  color: #a87fff;
  font-weight: 700;
  margin-bottom: 16px;
}

.flip-card-back p {
  font-size: 1rem;
  color: #606f7b;
  line-height: 1.6;
  margin-bottom: 24px;
}

.btn-voltar {
  font-size: 0.9rem;
  font-weight: 700;
  color: #7f8c8d;
  background-color: #faf6ff;
  padding: 6px 16px;
  border-radius: 20px;
  transition: all 0.2s ease;
}

.flip-card:hover .btn-voltar {
  color: #a87fff;
  background-color: #f3e8ff;
}

.flip-card:not(.is-flipped):hover .flip-card-inner {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(153, 126, 189, 0.12);
}

@media (max-width: 992px) {
  .servicos-content-pacs { flex-direction: column; align-items: center; }
  .flip-card { width: 100%; max-width: 340px; height: 380px; }
  .servicos-title { font-size: 2.2rem; }
  .wave-top-divider svg { height: 50px; }
}
</style>