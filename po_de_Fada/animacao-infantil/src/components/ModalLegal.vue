<script setup>
defineProps({
  aberto: Boolean,
  titulo: String
})

const emit = defineEmits(['fechar'])
</script>

<template>
  <transition name="fade-modal">
    <div v-if="aberto" class="modal-overlay" @click.self="emit('fechar')">
      <div class="modal-card">
        
        <!-- CABEÇALHO DO MODAL -->
        <div class="modal-header">
          <h3>{{ titulo }}</h3>
          <button @click="emit('fechar')" class="btn-close" aria-label="Fechar">&times;</button>
        </div>

        <!-- CORPO DO TEXTO (ESTRUTURA BASE) -->
        <div class="modal-body">
          <p>
            Na <strong>Pó de Fada</strong>, respeitamos a tua privacidade. Esta estrutura garante que os teus dados estão protegidos de acordo com o RGPD.
          </p>

          <h4>1. Recolha de Dados</h4>
          <p>
            Os dados recolhidos através do formulário de contacto (Nome, E-mail, Assunto e Mensagem) destinam-se exclusivamente a responder a pedidos de informação e orçamentos.
          </p>

          <h4>2. Utilização das Informações</h4>
          <p>
            Não partilhamos, vendemos ou cedemos os teus dados pessoais a terceiros. As informações são utilizadas apenas para a comunicação direta entre a Pó de Fada e o cliente.
          </p>

          <h4>3. Direitos do Utilizador</h4>
          <p>
            Podes a qualquer momento solicitar o acesso, alteração ou eliminação dos teus dados pessoais enviando um e-mail para o nosso contacto principal.
          </p>
        </div>

        <!-- RODAPÉ DO MODAL -->
        <div class="modal-footer">
          <button @click="emit('fechar')" class="btn-entendido">Compreendi</button>
        </div>

      </div>
    </div>
  </transition>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(44, 62, 80, 0.6);
  backdrop-filter: blur(6px);
  z-index: 20000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-card {
  background: #ffffff;
  width: 100%;
  max-width: 550px;
  max-height: 80vh;
  border-radius: 24px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid rgba(168, 127, 255, 0.2);
}

.modal-header {
  padding: 20px 24px;
  background: #faf6ff;
  border-bottom: 1px solid #f0e6ff;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.3rem;
  font-weight: 800;
}

.btn-close {
  background: none;
  border: none;
  font-size: 1.8rem;
  color: #7f8c8d;
  cursor: pointer;
  line-height: 1;
  transition: color 0.2s ease;
}

.btn-close:hover {
  color: #a87fff;
}

.modal-body {
  padding: 24px;
  overflow-y: auto;
  color: #606f7b;
  font-size: 0.92rem;
  line-height: 1.6;
}

.modal-body h4 {
  color: #2c3e50;
  margin: 18px 0 6px 0;
  font-size: 1rem;
}

.modal-footer {
  padding: 16px 24px;
  border-top: 1px solid #f0e6ff;
  display: flex;
  justify-content: flex-end;
  background: #ffffff;
}

.btn-entendido {
  background: linear-gradient(135deg, #a87fff 0%, #8a53ff 100%);
  color: #ffffff;
  border: none;
  padding: 10px 24px;
  border-radius: 30px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(168, 127, 255, 0.3);
}

/* ANIMAÇÃO FADE */
.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.3s ease;
}

.fade-modal-enter-from,
.fade-modal-leave-to {
  opacity: 0;
}
</style>