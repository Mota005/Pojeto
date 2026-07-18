<script setup>
import { ref } from 'vue'

// O CONTROLO DA ABERTURA: Guarda o número da pergunta que está aberta (null = todas fechadas)
const openIndex = ref(null)

const toggleDuvida = (index) => {
  // Se clicarmos na que já está aberta, ela fecha (volta a null). Se não, abre a nova.
  openIndex.value = openIndex.value === index ? null : index
}

/* ─── ENTRADA DE DADOS: ADICIONA AQUI AS TUAS PERGUNTAS NO FUTURO ─── */
const listaDuvidas = ref([
  {
    pergunta: 'Com que antecedência devo reservar a festa?',
    resposta: 'Recomendamos que faças a tua reserva com pelo menos 3 a 4 semanas de antecedência para garantir a disponibilidade da nossa equipa e dos materiais para o tema escolhido.'
  },
  {
    pergunta: 'Os materiais das pinturas faciais são seguros?',
    resposta: 'Absolutamente! Utilizamos apenas maquilhagem profissional à base de água, hipoalergénica e dermatologicamente testada, totalmente segura para a pele sensível das crianças e fácil de remover com água morna.'
  },
  {
    pergunta: 'Deslocam-se para fora da zona principal?',
    resposta: 'Sim! Levamos a magia da Pó de Fada a qualquer lado. Para eventos fora da nossa área base, aplicamos apenas uma taxa de deslocação sob consulta baseada nos quilómetros.'
  },
  {
    pergunta: 'O que acontece em caso de desistência ou imprevisto?',
    resposta: 'Sabemos que os imprevistos acontecem. Se precisares de adiar, fazemos o reagendamento sem custos num prazo de até 7 dias antes do evento, mediante a nossa disponibilidade.'
  }
])
</script>

<template>
  <section id="duvidas" class="duvidas-section">
    
    <!-- Onda no topo para cortar o fundo lilás da secção anterior -->
    <div class="wave-top-duvidas">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,0L60,10.7C120,21,240,43,360,48C480,53,600,43,720,37.3C840,32,960,32,1080,42.7C1200,53,1320,75,1380,85.3L1440,96L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z" fill="#ffffff"/>
      </svg>
    </div>

    <div class="duvidas-container">
      
      <!-- Cabeçalho -->
      <div class="duvidas-header">
        <span class="duvidas-badge">FAQ</span>
        <h2 class="duvidas-title">Dúvidas Frequentes</h2>
        <p class="duvidas-subtitle">Esclarece os pormenores e deixa a preocupação connosco</p>
      </div>

      <!-- Lista de Acordéons -->
      <div class="accordion-wrapper">
        <div 
          v-for="(item, index) in listaDuvidas" 
          :key="index"
          class="accordion-item"
          :class="{ 'is-open': openIndex === index }"
        >
          <!-- Pergunta (Botão Clicável) -->
          <button class="accordion-trigger" @click="toggleDuvida(index)">
            <span class="question-text">{{ item.pergunta }}</span>
            <span class="arrow-icon">✨</span>
          </button>

          <!-- Resposta (Animação Suave por CSS Grid) -->
          <div class="accordion-content">
            <div class="accordion-content-inner">
              <p>{{ item.resposta }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Bloco de Contacto Final (CTA) -->
      <div class="duvidas-footer-cta">
        <div class="cta-box">
          <div class="cta-text">
            <h3>Ainda ficaste com alguma questão por responder?</h3>
            <p>Não hesites! Entra em contacto connosco e planeamos tudo juntos.</p>
          </div>
          <a href="#contacto" class="btn-cta-contacto">
            Falar com a Fada ✉
          </a>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.duvidas-section {
  background-color: #ffffff; /* Fundo branco limpo */
  padding: 140px 24px 100px 24px;
  position: relative;
}

/* ONDA DO TOPO */
.wave-top-duvidas {
  position: absolute;
  top: -1px;
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 5;
  transform: rotate(180deg); /* Inverte o corte para morder os Serviços */
}

.wave-top-duvidas svg {
  width: 100%;
  height: 90px;
  display: block;
}

/* CONTAINER PRINCIPAL */
.duvidas-container {
  max-width: 800px; /* Mais estreito para o texto não ficar muito disperso */
  margin: 0 auto;
  position: relative;
  z-index: 6;
}

.duvidas-header {
  text-align: center;
  margin-bottom: 50px;
}

.duvidas-badge {
  display: inline-block;
  background-color: #f3e8ff;
  color: #a87fff;
  padding: 6px 16px;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 16px;
}

.duvidas-title {
  font-size: 2.8rem;
  color: #2c3e50;
  font-weight: 800;
  letter-spacing: -1px;
  margin-bottom: 10px;
}

.duvidas-subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
}

/* ESTRUTURA DO ACORDÉON */
.accordion-wrapper {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 60px;
}

.accordion-item {
  background-color: #faf6ff; /* Fundo suave lilás */
  border-radius: 18px;
  border: 1px solid rgba(168, 127, 255, 0.08);
  overflow: hidden;
  transition: all 0.3s ease;
}

.accordion-trigger {
  width: 100%;
  background: none;
  border: none;
  padding: 24px 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: left;
  cursor: pointer;
  outline: none;
}

.question-text {
  font-size: 1.15rem;
  font-weight: 700;
  color: #2c3e50;
  transition: color 0.3s ease;
}

.arrow-icon {
  font-size: 1.2rem;
  transition: transform 0.4s ease;
  display: inline-block;
}

/* Efeitos ao passar o rato (Hover) */
.accordion-item:hover {
  border-color: rgba(168, 127, 255, 0.25);
  background-color: #f6eeff;
}

/* ESTADO ABERTO (Ativado pelo Vue) */
.accordion-item.is-open {
  background-color: #ffffff;
  border-color: #e8dbff;
  box-shadow: 0 10px 30px rgba(153, 126, 189, 0.08);
}

.accordion-item.is-open .question-text {
  color: #a87fff; /* Pergunta ganha destaque de cor */
}

.accordion-item.is-open .arrow-icon {
  transform: rotate(180deg) scale(1.2); /* A varinha/estrela gira */
}

/* TRUQUE CSS ULTRA SUAVE PARA ANIMAR ALTURA AUTOMÁTICA */
.accordion-content {
  display: grid;
  grid-template-rows: 0fr; /* Altura 0 por padrão */
  transition: grid-template-rows 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.accordion-item.is-open .accordion-content {
  grid-template-rows: 1fr; /* Expande para o tamanho real do texto */
}

.accordion-content-inner {
  overflow: hidden; /* Corta o texto quando fechado */
}

.accordion-content-inner p {
  padding: 0 28px 24px 28px; /* Margem interna do texto */
  font-size: 1rem;
  color: #606f7b;
  line-height: 1.6;
  margin: 0;
}

/* ─── BLOCO DE CONTACTO FINAL (CTA) ─── */
.duvidas-footer-cta {
  margin-top: 50px;
}

.cta-box {
  background: linear-gradient(135deg, #fbf9ff 0%, #f3e8ff 100%);
  border: 1px dashed #c1d9ff;
  border-radius: 24px;
  padding: 32px 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
}

.cta-text h3 {
  font-size: 1.3rem;
  color: #2c3e50;
  font-weight: 700;
  margin: 0 0 6px 0;
}

.cta-text p {
  font-size: 1rem;
  color: #7f8c8d;
  margin: 0;
}

.btn-cta-contacto {
  background: linear-gradient(135deg, #a87fff 0%, #c1d9ff 100%);
  color: #ffffff;
  text-decoration: none;
  padding: 14px 28px;
  border-radius: 50px;
  font-weight: 700;
  font-size: 1rem;
  box-shadow: 0 6px 20px rgba(168, 127, 255, 0.25);
  white-space: nowrap;
  transition: all 0.3s ease;
}

.btn-cta-contacto:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(168, 127, 255, 0.35);
}

/* RESPONSIVIDADE (MOBILE) */
@media (max-width: 768px) {
  .duvidas-title { font-size: 2.2rem; }
  .cta-box {
    flex-direction: column;
    text-align: center;
    padding: 30px 20px;
  }
  .btn-cta-contacto { width: 100%; text-align: center; }
  .question-text { font-size: 1rem; }
}
</style>