<template>
  <nav class="navbar-container">
    <div class="navbar-floating">
      
      <!-- O Logotipo Redondo + Texto -->
      <a href="#" class="nav-logo">
        <img src="../assets/logo.png" alt="Logotipo Pó de Fada" class="nav-logo-img">
        <span class="nav-brand-text">Pó de Fada</span>
      </a>

      <!-- Links de Navegação com Linha Animada -->
      <div class="nav-menu">
        <a href="#sobre" class="nav-link">Sobre</a>
        <a href="#servicos" class="nav-link">Serviços</a>
        <a href="#duvidas" class="nav-link">Dúvidas</a>
        <a href="#testemunhos" class="nav-link">Testemunhos</a>
      </div>

      <!-- Botão Contactar com Brilho Shimmer -->
      <div class="nav-actions">
        <a href="#contacto" class="btn-nav-contactar">Contactar</a>
      </div>

    </div>
  </nav>
</template>

<style scoped>
/* ─── A ESTRUTURA GERAL (FLUTUANTE) ─── */
.navbar-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 20px 24px 0 24px; /* Afasta a barra do topo do ecrã */
  z-index: 1000;
  pointer-events: none; /* Garante que as margens vazias não bloqueiam cliques */
}

.navbar-floating {
  max-width: 1200px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.85); /* Efeito vidro translúcido */
  backdrop-filter: blur(12px); /* Desfoca o fundo com muita elegância */
  -webkit-backdrop-filter: blur(12px);
  padding: 12px 32px;
  border-radius: 100px; /* Transforma a barra numa pílula flutuante */
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 10px 30px rgba(153, 126, 189, 0.1); /* Sombra suave purpurina */
  border: 1px solid rgba(255, 255, 255, 0.6);
  pointer-events: auto; /* Devolve os cliques aos elementos internos */
}

/* ─── LOGOTIPO ─── */
.nav-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.nav-logo-img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 10px rgba(193, 217, 255, 0.5);
  display: block;
}

.nav-brand-text {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--cor-texto-escuro, #2c3e50);
  letter-spacing: -0.5px;
}

/* ─── LINKS DO MENU (LINHA ANIMADA) ─── */
.nav-menu {
  display: flex;
  gap: 32px;
}

.nav-link {
  position: relative;
  text-decoration: none;
  color: var(--cor-texto-escuro, #2c3e50);
  font-weight: 600;
  font-size: 1rem;
  padding: 6px 0;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #a87fff; /* Muda para um tom mágico ao pairar */
}

/* A linha mágica que nasce por baixo */
.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #c1d9ff, #e8dbff);
  transition: all 0.3s ease;
  transform: translateX(-50%);
  border-radius: 2px;
}

.nav-link:hover::after {
  width: 100%; /* Expande do centro para os lados */
}

/* ─── BOTÃO CONTACTAR PREMIUM ─── */
.btn-nav-contactar {
  position: relative;
  display: inline-block;
  background: linear-gradient(135deg, #e8dbff 0%, #c1d9ff 100%);
  color: var(--cor-texto-escuro, #2c3e50);
  text-decoration: none;
  padding: 10px 24px;
  border-radius: 50px;
  font-weight: 700;
  font-size: 0.95rem;
  box-shadow: 0 4px 15px rgba(193, 217, 255, 0.4);
  transition: all 0.3s ease;
  overflow: hidden;
}

/* Efeito Shimmer Mini no botão da Nav */
.btn-nav-contactar::after {
  content: '';
  position: absolute;
  top: 0;
  left: -150%;
  width: 50%;
  height: 100%;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.7) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: skewX(-20deg);
}

.btn-nav-contactar:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(193, 217, 255, 0.6);
}

.btn-nav-contactar:hover::after {
  animation: nav-shine 1.2s ease-in-out infinite;
}

@keyframes nav-shine {
  100% { left: 150%; }
}

/* RESPONSIVIDADE (Ajuste rápido para Mobile) */
@media (max-width: 768px) {
  .navbar-container {
    padding: 12px 12px 0 12px;
  }
  .navbar-floating {
    padding: 10px 20px;
  }
  .nav-menu {
    display: none; /* Temporariamente escondido no mobile até fazermos o menu hambúrguer */
  }
}
</style>