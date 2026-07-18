<template>
  <!-- Toda a secção tem o id "sobre" para que os links da Navbar saibam onde rolar a página -->
  <section id="sobre" class="sobre-section">
    <div class="sobre-container">
      
      <!-- 1. COLUNA DA ESQUERDA: A FOTO COM DETALHE 3D -->
      <div class="sobre-image-side">
        <div class="image-wrapper">
          <!-- Esta div vazia é o retângulo lilás que fica desalinhado atrás da foto -->
          <div class="decor-card"></div>
          <!-- A foto principal (podes mudar o link para uma foto tua mais tarde) -->
          <img src="https://images.unsplash.com/photo-1516627145497-ae6968895b74?w=600" alt="Momentos mágicos Pó de Fada" class="sobre-img">
        </div>
      </div>

      <!-- 2. COLUNA DA DIREITA: OS TEXTOS E CRITÉRIOS -->
      <div class="sobre-content-side">
        <!-- Pequena etiqueta roxa de introdução -->
        <span class="sobre-badge">A Nossa História</span>
        
        <h2 class="sobre-title">Criamos memórias que duram para sempre</h2>
        
        <p class="sobre-text">
          A <strong>Pó de Fada</strong> nasceu do desejo de transformar festas infantis em verdadeiras viagens ao mundo da fantasia. Acreditamos que cada criança merece viver um dia mágico, onde a imaginação não tem limites e o sorriso é o único guia.
        </p>
        
        <p class="sobre-text">
          Com uma equipa apaixonada e experiente, levamos até ao teu evento atividades dinâmicas, pinturas faciais profissionais, modelagem de balões e oficinas criativas que encantam miúdos e graúdos.
        </p>

        <!-- A grelha com os 3 blocos de valores da marca -->
        <div class="valores-grid">
          <!-- Bloco 1 -->
          <div class="valor-card">
            <span class="valor-icon"></span>
            <h3>Criatividade</h3>
          </div>
          <!-- Bloco 2 -->
          <div class="valor-card">
            <span class="valor-icon"></span>
            <h3>Segurança</h3>
          </div>
          <!-- Bloco 3 -->
          <div class="valor-card">
            <span class="valor-icon"></span>
            <h3>Dedicação</h3>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
/* O fundo é branco total (#ffffff) para a onda do Hero desaparecer aqui dentro sem emendas */
.sobre-section {
  background-color: #ffffff; 
  padding: 100px 24px;
  position: relative;
}

/* O container limita a largura a 1200px para o texto não ficar espalhado nos monitores gigantes */
.sobre-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center; /* Alinha o meio da foto com o meio do texto */
  justify-content: space-between;
  gap: 80px; /* Espaço generoso de separação entre as duas colunas */
}

/* CONTROLOS DA FOTO (ESQUERDA) */
.sobre-image-side {
  flex: 1;
  display: flex;
  justify-content: center;
}

.image-wrapper {
  position: relative; /* Base de suporte para conseguirmos mover o fundo lilás */
  width: 100%;
  max-width: 400px;
}

/* O truque do efeito 3D: criamos um bloco lilás e empurramo-lo para a esquerda e para baixo */
.decor-card {
  position: absolute;
  top: 25px;
  left: -25px;
  width: 100%;
  height: 100%;
  background-color: #f3e8ff; /* Tom lilás pastel muito suave */
  border-radius: 24px;
  z-index: 1; /* Fica na camada de trás */
}

.sobre-img {
  position: relative;
  z-index: 2; /* Fica na camada da frente, tapando o decor-card */
  width: 100%;
  height: 460px;
  object-fit: cover; /* Garante que a imagem não fica distorcida ou esmagada */
  border-radius: 24px;
  box-shadow: 0 15px 35px rgba(153, 126, 189, 0.15); /* Sombra leve para dar peso */
}

/* CONTROLOS DO TEXTO (DIREITA) */
.sobre-content-side {
  flex: 1.2; /* Dá ligeiramente mais espaço à coluna de texto do que à da imagem */
  text-align: left;
}

.sobre-badge {
  display: inline-block;
  background-color: #f3e8ff;
  color: #a87fff; /* Texto roxo da tua identidade */
  padding: 6px 16px;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 20px;
}

.sobre-title {
  font-size: 2.8rem;
  color: #2c3e50;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 24px;
  letter-spacing: -1px;
}

.sobre-text {
  font-size: 1.1rem;
  color: #606f7b; /* Um cinzento escuro, muito mais confortável para ler do que o preto puro */
  line-height: 1.7; /* Espaçamento entre linhas para o texto respirar */
  margin-bottom: 20px;
}

/* OS VALORES (CARDS PEQUENOS) */
.valores-grid {
  display: flex;
  gap: 16px;
  margin-top: 36px;
}

.valor-card {
  flex: 1;
  background-color: #faf6ff; /* Fundo ligeiramente lilás */
  padding: 20px 12px;
  border-radius: 16px;
  text-align: center;
  border: 1px solid rgba(168, 127, 255, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Quando o utilizador passa o rato por cima de um valor, ele sobe suavemente */
.valor-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(168, 127, 255, 0.08);
}

.valor-icon {
  font-size: 1.8rem;
  display: inline-block;
  margin-bottom: 6px;
}

.valor-card h3 {
  font-size: 0.95rem;
  color: #2c3e50;
  font-weight: 700;
  margin: 0;
}

/* ─── RESPONSIVIDADE (ADAPTAÇÃO PARA TELEMÓVEL) ─── */
@media (max-width: 992px) {
  .sobre-container {
    flex-direction: column; /* Em ecrãs pequenos, mete a foto em cima e o texto por baixo */
    gap: 50px;
    padding: 0 12px;
  }

  .sobre-content-side {
    text-align: center; /* Centraliza os textos no telemóvel */
  }

  .sobre-title {
    font-size: 2.2rem;
  }

  .image-wrapper {
    max-width: 320px; /* Encolhe um pouco a foto para caber em qualquer telemóvel */
  }

  .sobre-img {
    height: 380px;
  }

  .valores-grid {
    flex-wrap: wrap; /* Se os 3 cartões não couberem lado a lado no telemóvel, eles saltam de linha automaticamente */
  }
}
</style>