# Claude Skills — Julio Flores

Skills personales para Claude Code y automatizaciones con IA.

---

## 🤖 Weekly AI Newsletter (automatización activa)

**Todos los domingos a las 20:00 h** recibes en tu correo un resumen semanal de las noticias más relevantes sobre inteligencia artificial empresarial.

### ¿Qué incluye?

- Resumen ejecutivo de la semana (bullet points clave)
- Noticias de **Google / DeepMind**
- Noticias de **Anthropic**
- Noticias de **OpenAI**
- Tendencias de adopción empresarial de IA
- Nuevos modelos y productos lanzados
- Tendencias emergentes a tener en el radar

Fuentes monitorizadas: Google AI Blog, OpenAI Blog, Anthropic News, MIT Technology Review, VentureBeat AI, TechCrunch AI, The Verge AI, Ars Technica.

El newsletter se genera automáticamente con **Claude Sonnet** y se envía vía Gmail.

---

### Configuración de secrets (paso obligatorio)

Para que la automatización funcione debes configurar 4 secrets en GitHub:

**Repositorio → Settings → Secrets and variables → Actions → New repository secret**

| Secret | Valor |
|--------|-------|
| `ANTHROPIC_API_KEY` | Tu API key de Anthropic (`sk-ant-...`) |
| `GMAIL_USER` | Tu dirección Gmail (p.ej. `juliofp578@gmail.com`) |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación de Gmail (ver abajo) |
| `RECIPIENT_EMAIL` | Email donde quieres recibir el newsletter |

#### Cómo obtener la contraseña de aplicación de Gmail

1. Ve a [myaccount.google.com/security](https://myaccount.google.com/security)
2. Activa la **Verificación en dos pasos** (si no la tienes)
3. En el buscador de la misma página escribe "contraseñas de aplicaciones"
4. Crea una nueva → elige "Correo" y "Otro (nombre personalizado)" → escribe "AI Newsletter"
5. Copia la contraseña de 16 caracteres que te genera → úsala como `GMAIL_APP_PASSWORD`

---

### Ejecución manual

Si quieres probar el newsletter sin esperar al domingo:

**Repositorio → Actions → 🤖 Weekly AI Newsletter → Run workflow → Run workflow**

---

### Horario

El cron está configurado a las `18:00 UTC` los domingos, que equivale a:
- **20:00 hora España (verano / CEST)**
- 19:00 hora España (invierno / CET)

---

## Skills disponibles

| Skill | Descripción | Comando de activación |
|-------|-------------|----------------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

## Instalación de skills

```bash
# Mac/Linux
cp *.skill ~/.claude/skills/

# Windows (PowerShell)
Copy-Item "*.skill" "$env:USERPROFILE\.claude\skills\"
```

---

> **Aviso legal**: las skills son para uso en sistemas propios o con autorización explícita del propietario. El uso no autorizado puede ser ilegal.
