<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

/* ─── 1. FOTOS DO CARROSEL ─── */
const fotosEventos = ref([
  {
    url: 'https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=800',
    legenda: 'legenda'
  },
  {
    url: 'https://images.unsplash.com/photo-1513151233558-d860c5398176?w=800',
    legenda: 'legenda'
  },
  {
    url: 'https://images.unsplash.com/photo-1527529482837-4698179dc6ce?w=800',
    legenda: 'legenda'
  }
])

const currentSlide = ref(0)

const proxFoto = () => {
  currentSlide.value = (currentSlide.value + 1) % fotosEventos.value.length
}

const fotoAnterior = () => {
  currentSlide.value = (currentSlide.value - 1 + fotosEventos.value.length) % fotosEventos.value.length
}

let timer = null
onMounted(() => {
  timer = setInterval(proxFoto, 5000)
})
onUnmounted(() => {
  clearInterval(timer)
})

/* ─── 2. COMENTÁRIOS / AVALIAÇÕES ─── */
const listaComentarios = ref([
  {
    nome: 'nome',
    evento: 'acontecimento',
    estrelas: '⭐⭐⭐⭐⭐',
    texto: 'texto'
  },
   {
    nome: 'nome',
    evento: 'acontecimento',
    estrelas: '⭐⭐⭐⭐⭐',
    texto: 'texto'
  }
])
</script>

<template>
  <section id="testemunhos" class="testemunhos-section">
    
    <!-- ─── ONDA NO TOPO (Encaixa no fundo branco das Dúvidas) ─── -->
    <div class="wave-top-testemunhos">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,0L60,10.7C120,21,240,43,360,48C480,53,600,43,720,37.3C840,32,960,32,1080,42.7C1200,53,1320,75,1380,85.3L1440,96L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z" fill="#ffffff"/>
      </svg>
    </div>

    <div class="testemunhos-container">
      
      <!-- Cabeçalho -->
      <div class="testemunhos-header">
        <span class="testemunhos-badge">Galeria & Feedback</span>
        <h2 class="testemunhos-title">Momentos Que Marcam</h2>
        <p class="testemunhos-subtitle">Espreita a magia dos nossos eventos passados</p>
      </div>

      <!-- ─── CARROSEL DE FOTOS ─── -->
      <div class="carousel-wrapper">
        <div class="carousel-display">
          <img 
            :src="fotosEventos[currentSlide].url" 
            :alt="fotosEventos[currentSlide].legenda" 
            class="carousel-img"
          />
          <div class="carousel-caption">
            <p>{{ fotosEventos[currentSlide].legenda }}</p>
          </div>
        </div>

        <!-- Botões de Navegação -->
        <button class="nav-btn prev-btn" @click="fotoAnterior">❮</button>
        <button class="nav-btn next-btn" @click="proxFoto">❯</button>

        <!-- Indicadores (Pontinhos) -->
        <div class="carousel-dots">
          <span 
            v-for="(foto, index) in fotosEventos" 
            :key="index"
            class="dot"
            :class="{ 'active': currentSlide === index }"
            @click="currentSlide = index"
          ></span>
        </div>
      </div>

      <!-- ─── GRELHA DE COMENTÁRIOS ─── -->
      <div class="comentarios-grid">
        <div 
          v-for="(comentario, index) in listaComentarios" 
          :key="index"
          class="comentario-card"
        >
          <div class="card-stars">{{ comentario.estrelas }}</div>
          <p class="card-quote">"{{ comentario.texto }}"</p>
          <div class="card-author">
            <strong>{{ comentario.nome }}</strong>
            <span>{{ comentario.evento }}</span>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.testemunhos-section {
  background-color: #faf6ff; /* Fundo lilás suave */
  padding: 140px 24px 100px 24px; /* Padding extra no topo para a onda */
  position: relative;
  z-index: 5;
}

/* ─── ESTILO DA ONDA DO TOPO ─── */
.wave-top-testemunhos {
  position: absolute;
  top: -1px;
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 6;
}

.wave-top-testemunhos svg {
  width: 100%;
  height: 90px;
  display: block;
}

/* ─── RESTO DO DESIGN ─── */
.testemunhos-container {
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
  z-index: 7;
}

.testemunhos-header {
  text-align: center;
  margin-bottom: 50px;
}

.testemunhos-badge {
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

.testemunhos-title {
  font-size: 2.8rem;
  color: #2c3e50;
  font-weight: 800;
  margin-bottom: 8px;
}

.testemunhos-subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
}

/* CARROSEL */
.carousel-wrapper {
  position: relative;
  max-width: 800px;
  margin: 0 auto 70px auto;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(153, 126, 189, 0.15);
  background-color: #ffffff;
}

.carousel-display {
  position: relative;
  height: 420px;
  width: 100%;
}

.carousel-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: all 0.5s ease-in-out;
}

.carousel-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 20px 30px;
  background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(44, 62, 80, 0.8) 100%);
  color: #ffffff;
  font-weight: 600;
  font-size: 1.1rem;
}

.nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.85);
  border: none;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  font-size: 1.2rem;
  color: #2c3e50;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  z-index: 10;
}

.nav-btn:hover {
  background: #ffffff;
  color: #a87fff;
  transform: translateY(-50%) scale(1.1);
}

.prev-btn { left: 20px; }
.next-btn { right: 20px; }

.carousel-dots {
  position: absolute;
  bottom: 20px;
  right: 30px;
  display: flex;
  gap: 8px;
  z-index: 10;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: #a87fff;
  width: 24px;
  border-radius: 10px;
}

/* GRELHA COMENTÁRIOS */
.comentarios-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.comentario-card {
  background: #ffffff;
  padding: 32px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(153, 126, 189, 0.05);
  border: 1px solid rgba(168, 127, 255, 0.08);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-stars {
  font-size: 1.1rem;
  margin-bottom: 14px;
}

.card-quote {
  font-size: 1rem;
  color: #2c3e50;
  line-height: 1.6;
  font-style: italic;
  margin-bottom: 20px;
}

.card-author strong {
  display: block;
  color: #a87fff;
  font-size: 1.05rem;
}

.card-author span {
  font-size: 0.85rem;
  color: #7f8c8d;
}

@media (max-width: 768px) {
  .carousel-display { height: 280px; }
  .testemunhos-title { font-size: 2.2rem; }
  .wave-top-testemunhos svg { height: 50px; }
}
</style>