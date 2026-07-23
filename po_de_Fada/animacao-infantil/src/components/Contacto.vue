<script setup>
import { ref } from 'vue'

const form = ref({
  nome: '',
  email: '',
  assunto: '',
  dataFesta: '',
  mensagem: ''
})

const enviado = ref(false)

const enviarFormulario = () => {
  if (form.value.nome && form.value.email && form.value.assunto && form.value.mensagem) {
    enviado.value = true
    setTimeout(() => {
      enviado.value = false
      form.value = { nome: '', email: '', assunto: '', dataFesta: '', mensagem: '' }
    }, 4000)
  }
}
</script>

<template>
  <section id="contacto" class="contacto-section">
    <div class="wave-top-contacto">
      <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <path d="M0,32L60,42.7C120,53,240,75,360,80C480,85,600,75,720,64C840,53,960,43,1080,48C1200,53,1320,75,1380,85.3L1440,96L1440,120L1380,120C1320,120,1200,120,1080,120C960,120,840,120,720,120C600,120,480,120,360,120C240,120,120,120,60,120L0,120Z" fill="#ffffff"/>
      </svg>
    </div>

    <div class="contacto-container">
      <div class="contacto-header">
        <span class="contacto-badge">Fala Connosco</span>
        <h2 class="contacto-title animate-fade-up">Entra em Contacto</h2>
        <p class="contacto-subtitle animate-fade-up-delay">Envia-nos uma mensagem e responderemos o mais breve possível</p>
      </div>

      <div class="contacto-grid">
        <div class="info-card">
          <h3>Contactos Diretos</h3>
          <p class="info-desc">Estamos disponíveis para esclarecer qualquer dúvida, pedir orçamentos ou agendar a tua festa.</p>

          <div class="info-list">
            <div class="info-item">
              <span class="item-icon"></span>
              <div>
                <strong>Zona de Atuação</strong>
                <p>Porto e Arredores (Deslocações sob consulta)</p>
              </div>
            </div>

            <div class="info-item">
              <span class="item-icon"></span>
              <div>
                <strong>Email</strong>
                <p>geral@podefada.pt</p>
              </div>
            </div>

            <div class="info-item">
              <span class="item-icon"></span>
              <div>
                <strong>Instagram</strong>
                <p>@podefada.animacao</p>
              </div>
            </div>
          </div>

          <div class="info-social-box">
            <p>Acompanha o nosso dia a dia e bastidores das festas! </p>
          </div>
        </div>

        <div class="form-card">
          <form @submit.prevent="enviarFormulario" class="fada-form">
            <div class="form-group">
              <label for="nome">O teu nome *</label>
              <input type="text" id="nome" v-model="form.nome" placeholder="Ex: Maria Silva" required />
            </div>

            <div class="form-group">
              <label for="email">O teu e-mail *</label>
              <input type="email" id="email" v-model="form.email" placeholder="maria@email.com" required />
            </div>

            <div class="form-group">
              <label for="assunto">Assunto *</label>
              <input type="text" id="assunto" v-model="form.assunto" placeholder="Ex: Pedido de Orçamento / Informações" required />
            </div>

            <div class="form-group">
              <label for="data">Data prevista do evento <span class="optional-tag">(Opcional)</span></label>
              <input type="date" id="data" v-model="form.dataFesta" />
            </div>

            <div class="form-group">
              <label for="mensagem">Mensagem *</label>
              <textarea id="mensagem" v-model="form.mensagem" rows="4" placeholder="Escreve aqui a tua mensagem..." required></textarea>
            </div>

            <button type="submit" class="btn-submit">Enviar Mensagem ✨</button>

            <transition name="fade">
              <div v-if="enviado" class="success-msg">
                ✨ Mensagem enviada com sucesso! Responderemos em breve.
              </div>
            </transition>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.contacto-section {
  background-color: #ffffff;
  padding: 120px 24px 80px 24px;
  position: relative;
  z-index: 5;
}

.wave-top-contacto {
  position: absolute;
  top: -80px;
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 6;
}

.wave-top-contacto svg {
  width: 100%;
  height: 80px;
  display: block;
}

.contacto-container {
  max-width: 1000px;
  margin: 0 auto;
}

.contacto-header {
  text-align: center;
  margin-bottom: 60px;
}

.contacto-badge {
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

.contacto-title {
  font-size: 2.8rem;
  color: #2c3e50;
  font-weight: 800;
  margin-bottom: 8px;
}

.contacto-subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
}

.contacto-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 40px;
}

.info-card {
  background: #faf6ff;
  padding: 40px;
  border-radius: 24px;
  border: 1px solid rgba(168, 127, 255, 0.12);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.info-card h3 {
  font-size: 1.5rem;
  color: #2c3e50;
  font-weight: 800;
  margin-bottom: 10px;
}

.info-desc {
  color: #7f8c8d;
  line-height: 1.6;
  margin-bottom: 30px;
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.info-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.item-icon {
  font-size: 1.4rem;
  background: #ffffff;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(168, 127, 255, 0.15);
}

.info-item strong {
  display: block;
  color: #2c3e50;
  font-size: 0.95rem;
}

.info-item p {
  color: #606f7b;
  font-size: 0.9rem;
  margin: 2px 0 0 0;
}

.info-social-box {
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px dashed rgba(168, 127, 255, 0.2);
  color: #a87fff;
  font-size: 0.88rem;
  font-weight: 600;
}

.form-card {
  background: #ffffff;
  padding: 40px;
  border-radius: 24px;
  box-shadow: 0 15px 35px rgba(153, 126, 189, 0.08);
  border: 1px solid #e8dbff;
}

.fada-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 0.9rem;
  font-weight: 700;
  color: #2c3e50;
}

.optional-tag {
  font-weight: 400;
  font-size: 0.8rem;
  color: #95a5a6;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 14px 18px;
  border-radius: 12px;
  border: 1.5px solid #f0e6ff;
  background: #faf8ff;
  font-size: 0.95rem;
  color: #2c3e50;
  outline: none;
  transition: all 0.3s ease;
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #a87fff;
  background: #ffffff;
  box-shadow: 0 0 0 4px rgba(168, 127, 255, 0.1);
}

.btn-submit {
  background: linear-gradient(135deg, #a87fff 0%, #8a53ff 100%);
  color: #ffffff;
  border: none;
  padding: 16px;
  border-radius: 50px;
  font-weight: 800;
  font-size: 1rem;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(168, 127, 255, 0.3);
  transition: all 0.3s ease;
  margin-top: 10px;
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 25px rgba(168, 127, 255, 0.4);
}

.success-msg {
  background: #e8f8f0;
  color: #1e7e48;
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 700;
  text-align: center;
}

@media (max-width: 768px) {
  .contacto-grid { grid-template-columns: 1fr; }
  .contacto-title { font-size: 2.2rem; }
}
</style>