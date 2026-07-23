<script setup>
import { ref } from 'vue'
import ModalLegal from './ModalLegal.vue'

const modalAberto = ref(false)
const modalTitulo = ref('')

const abrirPolitica = () => {
  modalTitulo.value = 'Política de Privacidade'
  modalAberto.value = true
}

const abrirTermos = () => {
  modalTitulo.value = 'Termos e Condições'
  modalAberto.value = true
}
</script>

<template>
  <footer class="fada-footer">
    
    <div class="wave-top-footer">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,0L60,10.7C120,21,240,43,360,48C480,53,600,43,720,37.3C840,32,960,32,1080,42.7C1200,53,1320,75,1380,85.3L1440,96L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z" fill="#ffffff"/>
      </svg>
    </div>

    <div class="footer-container">
      <div class="footer-grid">
        
        <!-- COLUNA 1: MARCA -->
        <div class="footer-col col-brand">
          <div class="brand-header">
            <span class="brand-sparkle">✨</span>
            <span class="brand-title">Pó de Fada</span>
          </div>
          <p class="brand-desc">
            Animação infantil e momentos inesquecíveis. Onde cada festa ganha vida com cor, gargalhadas e verdadeira magia.
          </p>
          
          <div class="social-links">
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="social-btn instagram" aria-label="Instagram">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="social-icon">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
              </svg>
            </a>

            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="social-btn facebook" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="social-icon">
                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
              </svg>
            </a>

            <a href="https://wa.me/351912345678" target="_blank" rel="noopener noreferrer" class="social-btn whatsapp" aria-label="WhatsApp">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="social-icon">
                <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
              </svg>
            </a>
          </div>
        </div>

        <!-- COLUNA 2: NAVEGAÇÃO -->
        <div class="footer-col">
          <h4 class="col-title">Navegação</h4>
          <ul class="footer-links">
            <li><a href="#hero">Início</a></li>
            <li><a href="#sobre">Sobre Nós</a></li>
            <li><a href="#servicos">Serviços & Festas</a></li>
            <li><a href="#duvidas">Dúvidas Frequentes</a></li>
            <li><a href="#contacto">Pedir Orçamento</a></li>
          </ul>
        </div>

        <!-- COLUNA 3: INFORMAÇÕES & LEGAL -->
        <div class="footer-col">
          <h4 class="col-title">Informações</h4>
          <ul class="info-list">
            <li>
              <strong>Zona Principal:</strong>
              <span>Porto e Arredores</span>
            </li>
            <li>
              <strong>Email:</strong>
              <a href="mailto:mariana.d.teixeira@hotmail.com">mariana.d.teixeira@hotmail.com</a>
            </li>
            <li>
              <!-- LINKS DE MODAL LEGAL -->
              <button @click="abrirPolitica" class="legal-btn">Política de Privacidade</button>
            </li>
            <li>
              <button @click="abrirTermos" class="legal-btn">Termos e Condições</button>
            </li>
          </ul>
        </div>

      </div>

      <!-- COPYRIGHT -->
      <div class="footer-bottom">
        <p>© 2026 <strong>Pó de Fada</strong>. Todos os direitos reservados.</p>
        <p class="love-tag">Feito com pós de fada e carinho ✨</p>
      </div>

    </div>

    <!-- COMPONENTE DO MODAL LEGAL -->
    <ModalLegal 
      :aberto="modalAberto" 
      :titulo="modalTitulo" 
      @fechar="modalAberto = false" 
    />

  </footer>
</template>

<style scoped>
.fada-footer {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 120px 24px 30px 24px;
  position: relative;
  z-index: 5;
}

.wave-top-footer {
  position: absolute;
  top: -1px;
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 6;
}

.wave-top-footer svg {
  width: 100%;
  height: 80px;
  display: block;
}

.footer-container {
  max-width: 1100px;
  margin: 0 auto;
  position: relative;
  z-index: 7;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.8fr 1fr 1.2fr;
  gap: 60px;
  margin-bottom: 60px;
}

.brand-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.brand-sparkle { font-size: 1.3rem; }

.brand-title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: -0.5px;
}

.brand-desc {
  color: #a0aec0;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 24px;
  max-width: 360px;
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-btn {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  transition: all 0.3s ease;
  text-decoration: none;
}

.social-icon { width: 20px; height: 20px; }

.social-btn:hover {
  background: #a87fff;
  border-color: #a87fff;
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(168, 127, 255, 0.4);
}

.col-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 20px;
}

.col-title::after {
  content: '';
  display: block;
  width: 30px;
  height: 2px;
  background: #a87fff;
  margin-top: 6px;
  border-radius: 2px;
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-links a {
  color: #a0aec0;
  text-decoration: none;
  font-size: 0.92rem;
  transition: all 0.25s ease;
}

.footer-links a:hover {
  color: #a87fff;
  padding-left: 6px;
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.info-list li strong {
  display: block;
  color: #ffffff;
  font-size: 0.85rem;
}

.info-list li span,
.info-list li a {
  color: #a0aec0;
  font-size: 0.9rem;
  text-decoration: none;
  word-break: break-all;
}

/* BOTAO PARA ABRIR O MODAL LEGAL */
.legal-btn {
  background: none;
  border: none;
  color: #a0aec0;
  font-size: 0.88rem;
  cursor: pointer;
  padding: 0;
  text-decoration: underline;
  transition: color 0.2s ease;
}

.legal-btn:hover {
  color: #a87fff;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #718096;
  font-size: 0.85rem;
}

.footer-bottom strong { color: #a0aec0; }
.love-tag { color: #a87fff; }

@media (max-width: 768px) {
  .footer-grid { grid-template-columns: 1fr; gap: 40px; }
  .footer-bottom { flex-direction: column; text-align: center; gap: 10px; }
}
</style>