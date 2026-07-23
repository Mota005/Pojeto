<template>
  <div class="fada-orb-container">
    
    <!-- BALÃO DE TEXTO EM GLASSMORPHISM -->
    <div class="magic-popover">
      <svg class="sparkle-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0L14.593 9.407L24 12L14.593 14.593L12 24L9.407 14.593L0 12L9.407 9.407L12 0Z" fill="url(#sparkle-grad)"/>
        <defs>
          <linearGradient id="sparkle-grad" x1="0" y1="0" x2="24" y2="24" gradientUnits="userSpaceOnUse">
            <stop stop-color="#FFD700"/>
            <stop offset="1" stop-color="#FFA500"/>
          </linearGradient>
        </defs>
      </svg>
      <span class="popover-text">Pedir Magia no WhatsApp</span>
    </div>

    <!-- BOTÃO ORBE DE CRISTAL -->
    <a 
      href="https://wa.me/351912345678?text=Olá!%20Quero%20levar%20a%20magia%20da%20Pó%20de%20Fada%20à%20minha%20festa!" 
      target="_blank" 
      rel="noopener noreferrer"
      class="crystal-orb-btn"
      aria-label="Contactar no WhatsApp"
    >
      <div class="light-dust d1"></div>
      <div class="light-dust d2"></div>
      <div class="light-dust d3"></div>

      <div class="crystal-core">
        <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" class="wa-svg">
          <path d="M16 2C8.268 2 2 8.268 2 16C2 18.868 2.868 21.536 4.364 23.75L2.5 29.5L8.436 27.678C10.58 29.046 13.194 29.846 16 29.846C23.732 29.846 30 23.578 30 15.846C30 8.114 23.732 2 16 2Z" fill="url(#wa-grad)"/>
          <path d="M22.88 19.34C22.5 19.15 20.64 18.23 20.29 18.1C19.94 17.97 19.69 17.91 19.44 18.29C19.19 18.67 18.47 19.52 18.25 19.77C18.03 20.02 17.81 20.05 17.43 19.86C17.05 19.67 15.83 19.27 14.38 17.98C13.25 16.97 12.49 15.73 12.27 15.35C12.05 14.97 12.25 14.77 12.44 14.58C12.61 14.41 12.82 14.13 13.01 13.91C13.2 13.69 13.26 13.53 13.39 13.28C13.52 13.03 13.45 12.81 13.36 12.62C13.27 12.43 12.52 10.59 12.21 9.84C11.9 9.11 11.59 9.21 11.36 9.2C11.15 9.19 10.9 9.19 10.65 9.19C10.4 9.19 10 9.28 9.65 9.66C9.3 10.04 8.31 10.97 8.31 12.87C8.31 14.77 9.69 16.6 9.88 16.85C10.07 17.1 12.6 20.98 16.47 22.65C17.39 23.05 18.11 23.29 18.67 23.47C19.59 23.76 20.43 23.72 21.09 23.62C21.83 23.51 23.37 22.69 23.69 21.79C24.01 20.89 24.01 20.13 23.91 19.97C23.82 19.8 23.26 19.53 22.88 19.34Z" fill="#ffffff"/>
          <defs>
            <linearGradient id="wa-grad" x1="2" y1="2" x2="30" y2="29.8" gradientUnits="userSpaceOnUse">
              <stop stop-color="#25D366"/>
              <stop offset="1" stop-color="#128C7E"/>
            </linearGradient>
          </defs>
        </svg>
      </div>

      <div class="ring-pulse"></div>
    </a>

  </div>
</template>

<style scoped>
.fada-orb-container {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 9999;
  display: flex;
  align-items: center;
  gap: 12px;
}

.magic-popover {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  padding: 10px 18px;
  border-radius: 50px;
  box-shadow: 0 10px 30px rgba(168, 127, 255, 0.18);
  border: 1px solid rgba(168, 127, 255, 0.3);
  display: flex;
  align-items: center;
  gap: 8px;
  animation: float-soft 3.5s ease-in-out infinite;
}

.sparkle-svg {
  width: 14px;
  height: 14px;
  animation: rotate-sparkle 4s linear infinite;
}

.popover-text {
  font-size: 0.88rem;
  font-weight: 800;
  color: #2c3e50;
  letter-spacing: -0.2px;
}

.crystal-orb-btn {
  position: relative;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}

.crystal-core {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffffff 0%, #f6eeff 50%, #e8dbff 100%);
  border: 1.5px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 10px 25px rgba(168, 127, 255, 0.3), inset 0 0 10px rgba(255, 255, 255, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  animation: orb-bounce 4s ease-in-out infinite;
}

.wa-svg {
  width: 32px;
  height: 32px;
  filter: drop-shadow(0 3px 6px rgba(37, 211, 102, 0.25));
}

.light-dust {
  position: absolute;
  border-radius: 50%;
  background: #ffd700;
  box-shadow: 0 0 8px #ffd700;
  pointer-events: none;
  z-index: 3;
}

.d1 { width: 5px; height: 5px; top: -2px; left: 12px; animation: dust-glow 2s infinite ease-in-out; }
.d2 { width: 4px; height: 4px; bottom: 4px; right: 2px; animation: dust-glow 2.8s infinite ease-in-out 0.5s; }
.d3 { width: 6px; height: 6px; top: 18px; right: -6px; animation: dust-glow 2.2s infinite ease-in-out 1s; }

.ring-pulse {
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  border-radius: 50%;
  border: 1.5px solid rgba(168, 127, 255, 0.4);
  z-index: 1;
  animation: ring-expand 3s infinite ease-out;
}

.fada-orb-container:hover .crystal-core {
  transform: scale(1.12) rotate(6deg);
  border-color: #a87fff;
  box-shadow: 0 14px 30px rgba(168, 127, 255, 0.45);
}

@keyframes orb-bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}

@keyframes float-soft {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}

@keyframes rotate-sparkle {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes dust-glow {
  0%, 100% { opacity: 0.2; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.4); }
}

@keyframes ring-expand {
  0% { transform: scale(0.9); opacity: 0.8; }
  100% { transform: scale(1.3); opacity: 0; }
}

@media (max-width: 768px) {
  .magic-popover { display: none; }
  .crystal-core { width: 52px; height: 52px; }
  .wa-svg { width: 28px; height: 28px; }
}
</style>