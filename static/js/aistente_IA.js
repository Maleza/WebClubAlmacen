// chat.js - UI minimal para el frontend del chat
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('chat-form');
  const input = document.getElementById('message-input');
  const messages = document.getElementById('messages');
  const clearBtn = document.getElementById('clear-btn');
  const prompts = document.querySelectorAll('.prompt');
  const status = document.getElementById('assistant-status');

  // Añadir mensaje al DOM
  function addMessage(text, who='assistant', meta='') {
    const li = document.createElement('li');
    li.className = `message ${who}`;
    if(meta) li.innerHTML = `<div class="meta">${meta}</div><div class="text">${text}</div>`;
    else li.innerHTML = `<div class="text">${text}</div>`;
    messages.appendChild(li);
    messages.scrollTop = messages.scrollHeight - messages.clientHeight;
  }

  // Simular respuesta del asistente (placeholder)
  function simulateResponse(userText) {
    status.textContent = 'Escribiendo...';
    // mostrar indicador typing
    const typingLi = document.createElement('li');
    typingLi.className = 'message assistant';
    typingLi.innerHTML = `<div class="meta">Asistente</div><div class="text"><span class="typing"></span></div>`;
    messages.appendChild(typingLi);
    messages.scrollTop = messages.scrollHeight;

    // reemplazar typing con respuesta tras delay
    setTimeout(() => {
      typingLi.remove();
      // RESPUESTA SIMULADA: aquí puedes llamar a tu backend con fetch()
      const reply = generateMockReply(userText);
      addMessage(reply, 'assistant', 'Asistente');
      status.textContent = 'Conectado';
    }, 900 + Math.min(userText.length * 20, 1600));
  }

  // Generador de respuesta simple (placeholder)
  function generateMockReply(text) {
    // respuestas básicas para pruebas
    const t = text.toLowerCase();
    if (t.includes('beneficio')) return 'Actualmente hay descuentos con proveedores asociados durante este mes. ¿Quieres ver la lista?';
    if (t.includes('horario') || t.includes('cuando')) return 'Las reuniones se realizan el primer martes de cada mes a las 18:00.';
    if (t.includes('como') && t.includes('afiliar')) return 'Para afiliarte, completa el formulario de registro y luego contacta a soporte.';
    // respuesta por defecto
    return "Buen punto — puedo ayudarte a buscar eso. (Esta es una respuesta simulada; conecta el frontend a tu API para respuestas reales.)";
  }

  // Manejo submit
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;
    addMessage(text, 'user', 'Tú');
    input.value = '';
    // aquí podrías hacer fetch('/api/chat/', {method:'POST', body: JSON...})
    simulateResponse(text);
  });

  // Clear
  clearBtn.addEventListener('click', () => {
    messages.innerHTML = '';
    addMessage('Hola 👋 Soy el Asistente del Club Almacén. ¿En qué puedo ayudarte hoy?', 'assistant', 'Asistente');
  });

  // Quick prompts
  prompts.forEach(btn => {
    btn.addEventListener('click', () => {
      const text = btn.textContent.trim();
      input.value = text;
      input.focus();
    });
  });

  // Inicializar con mensaje de bienvenida
  addMessage('Hola 👋 Soy el Asistente del Club Almacén. ¿En qué puedo ayudarte hoy?', 'assistant', 'Asistente');

  // NOTA: para integrar IA real, en lugar de simulateResponse() haz:
  // fetch('/api/chat/', { method: 'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({message:text}) })
  //  .then(r=>r.json()).then(data=> addMessage(data.reply,'assistant'));
});
